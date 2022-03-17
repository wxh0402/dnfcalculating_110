import { builtinModules } from "module"
import { defineConfig, Plugin } from "vite"
import path from "path"
import vue from "@vitejs/plugin-vue"
import jsx from "@vitejs/plugin-vue-jsx"
import uncomponents from "unplugin-vue-components/vite"
import pkg from "../../package.json"
import unocss from "unocss/vite"
import resolve from "vite-plugin-resolve"

import { presetUno, presetIcons } from "unocss"

// https://vitejs.dev/config/
export default defineConfig({
  mode: process.env.NODE_ENV,
  root: __dirname,
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src")
    }
  },
  plugins: [
    unocss({
      rules: [
        [
          /^col-(\d?\d)$/,
          ([, o]) => {
            let span = Number(o)
            const val = `${(span * 100) / 24}%`
            return {
              flex: `0 0 ${val}`
            }
          }
        ]
      ],

      presets: [presetUno(), presetIcons()]
    }),
    uncomponents({
      dts: true,
      dirs: ["src/components/"],
      allowOverrides: true,

      directoryAsNamespace: true
    }),
    jsx(),
    vue(),
    resolveElectron(
      /**
       * Here you can specify other modules
       * 🚧 You have to make sure that your module is in `dependencies` and not in the` devDependencies`,
       *    which will ensure that the electron-builder can package it correctly
       * @example
       * {
       *   'electron-store': 'const Store = require("electron-store"); export default Store;',
       * }
       */
      {
        // sqlite3: 'const sqlite3 = require("sqlite3"); export default sqlite3;',
      }
    )
  ],

  optimizeDeps: {
    exclude: ["electron"]
  },
  base: "./",
  build: {
    sourcemap: true,
    outDir: "../../dist/renderer"
  },
  server: {
    host: pkg.env.VITE_DEV_SERVER_HOST,
    port: pkg.env.VITE_DEV_SERVER_PORT
  }
})

/**
 * For usage of Electron and NodeJS APIs in the Renderer process
 * @see https://github.com/caoxiemeihao/electron-vue-vite/issues/52
 */
export function resolveElectron(
  resolves: Parameters<typeof resolve>[0] = {}
): Plugin {
  const builtins = builtinModules.filter(t => !t.startsWith("_"))
  /**
   * @see https://github.com/caoxiemeihao/vite-plugins/tree/main/packages/resolve#readme
   */
  return resolve({
    electron: electronExport(),
    ...builtinModulesExport(builtins),
    ...resolves
  })

  function electronExport() {
    return `
/**
 * For all exported modules see https://www.electronjs.org/docs/latest/api/clipboard -> Renderer Process Modules
 */
const electron = require("electron");
const {
  clipboard,
  nativeImage,
  shell,
  contextBridge,
  crashReporter,
  ipcRenderer,
  webFrame,
  desktopCapturer,
  deprecate,
} = electron;

export {
  electron as default,
  clipboard,
  nativeImage,
  shell,
  contextBridge,
  crashReporter,
  ipcRenderer,
  webFrame,
  desktopCapturer,
  deprecate,
}
`
  }

  function builtinModulesExport(modules: string[]) {
    return modules
      .map(moduleId => {
        const nodeModule = require(moduleId)
        const requireModule = `const M = require("${moduleId}");`
        const exportDefault = `export default M;`
        const exportMembers =
          Object.keys(nodeModule)
            .map(attr => `export const ${attr} = M.${attr}`)
            .join(";\n") + ";"
        const nodeModuleCode = `
${requireModule}

${exportDefault}

${exportMembers}
`

        return { [moduleId]: nodeModuleCode }
      })
      .reduce((memo, item) => Object.assign(memo, item), {})
  }
}
