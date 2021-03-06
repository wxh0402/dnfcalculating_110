import { builtinModules } from "module"
import { defineConfig } from "vite"
import pkg from "../../package.json"

export default defineConfig({
  root: __dirname,
  build: {
    outDir: "../../dist/app/preload",
    lib: {
      entry: "index.ts",
      formats: ["cjs"],
      fileName: () => "[name].cjs"
    },
    sourcemap: process.env./* from mode option */ NODE_ENV == "development",
    minify: process.env./* from mode option */ NODE_ENV === "production",
    // emptyOutDir: true,
    rollupOptions: {
      external: ["electron", ...builtinModules, ...Object.keys(pkg.dependencies || {})]
    }
  }
})
