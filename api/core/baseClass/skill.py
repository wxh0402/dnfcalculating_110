from core.equipment.基础函数 import 武器冷却惩罚,当前等级

等级 = 当前等级 + 5

class 技能:
    名称 = ''
    备注 = ''
    所在等级 = 0
    等级上限 = 0
    等级 = 0
    基础等级 = 0
    等级溢出 = 0
    自定义描述 = 0
    学习间隔 = 1
    等级精通 = 60

    关联技能 = ['无']
    关联技能2 = ['无']
    关联技能3 = ['无']
    非关联技能 = ['无']
    非关联技能2 = ['无']
    非关联技能3 = ['无']
    冷却关联技能 = ['无']
    冷却关联技能2 = ['无']
    冷却关联技能3 = ['无']
    非冷却关联技能 = ['无']
    非冷却关联技能2 = ['无']
    非冷却关联技能3 = ['无']

    def 等级加成(self, x):
        if self.等级 != 0:
            if self.等级 + x > self.等级上限:
                self.等级 = self.等级上限
                if self.基础等级 != self.等级上限 and self.关联技能 != ['无']:
                    self.等级溢出 = 1
            else:
                self.等级 += x

    def 基础等级计算(self):
        pass

class 主动技能(技能):
    # 只扩展了技能的三条属性，第一条技能hit默认1,2、3条hit默认为0，需要手动赋值
    # 如果需要继续扩展，可以在各自职业类内继承后自行扩展，同时需要重写下等效百分比函数
    # 固伤在填写基础及成长的时候需要注意，技能面板/独立得到的成长及数值需要*100
    基础 = 0.0
    成长 = 0.0
    攻击次数 = 1.0
    基础2 = 0.0
    成长2 = 0.0
    攻击次数2 = 0.0
    基础3 = 0.0
    成长3 = 0.0
    攻击次数3 = 0.0
    CD = 0.0
    TP成长 = 0.0
    TP上限 = 0
    TP等级 = 0
    是否主动 = 1
    是否有伤害 = 1
    恢复 = 1.0
    倍率 = 1.0
    被动倍率 = 1.0
    基础释放次数 = 0
    演出时间 = 0
    是否有护石 = 0
    护石选项 = ['魔界']

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int(
                (self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 *
                 (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 *
                 (self.基础3 + self.成长3 * self.等级)) *
                (1 + self.TP成长 * self.TP等级) * self.倍率)

    def 等效CD(self, 武器类型, 输出类型):
        return round(self.CD / self.恢复 * 武器冷却惩罚(武器类型, 输出类型), 1)

    def 基础等级计算(self):
        if self.基础等级 == 0:
            # 契约等级+5
            self.基础等级 = min(int((等级 + 5 - self.所在等级) / self.学习间隔 + 1),
                            self.等级精通)


class 被动技能(技能):
    是否主动 = 0
    是否有伤害 = 0
    关联技能 = ['所有']

    def 基础等级计算(self):
        if self.基础等级 == 0:
            # 契约等级+5
            self.基础等级 = min(int((等级 + 5 - self.所在等级) / self.学习间隔 + 1),
                            self.等级精通)
