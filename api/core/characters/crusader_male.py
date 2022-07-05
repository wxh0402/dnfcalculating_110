
from copy import deepcopy
from typing import List

from core.baseClass.buffer.property import *
from core.baseClass.character import Character


class 男圣骑士护石0:
    def __init__(self):
        self.name = '绝对壁垒'
        self.skill = '圣光球'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.06)
        pass


class 男圣骑士护石1:
    def __init__(self):
        self.name = '附庸的生命'
        self.skill = '忏悔之锤'

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.06)


class 男圣骑士护石2:
    def __init__(self):
        self.name = '米歇尔的审判'
        self.skill = '正义审判'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.04)


class 男圣骑士护石3:
    def __init__(self):
        self.name = '圣光奇袭'
        self.skill = '圣光突袭'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.08)


class 男圣骑士护石4:
    def __init__(self):
        self.name = '神圣操控'
        self.skill = '神圣之矛'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.04)


class 男圣骑士护石5:
    def __init__(self):
        self.name = '天堂结界'
        self.skill = '圣佑结界'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.08)


class 男圣骑士护石6:
    def __init__(self):
        self.name = '神圣守护'
        self.skill = '神圣之光'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.06)


男圣骑士护石组合 = (男圣骑士护石0(), 男圣骑士护石1(), 男圣骑士护石2(),
            男圣骑士护石3(), 男圣骑士护石4(), 男圣骑士护石5(), 男圣骑士护石6())


class 神启·圣骑士技能0(辅助职业被动技能):
    名称 = '守护恩赐'
    所在等级 = 15
    等级精通 = 50
    等级上限 = 60
    学习间隔 = 3
    额外体精 = 0
    站街生效 = 1

    体力 = [0, 20, 24, 28, 32, 36, 41, 46, 51, 57, 63, 69, 75, 81, 88, 95, 103, 111, 119, 127, 135, 144, 153, 163, 172, 182, 192, 203, 213, 224, 235, 247,
          259, 271, 283, 295, 309, 322, 335, 349, 363, 377, 391, 407, 421, 437, 453, 469, 485, 501, 518, 532, 548, 564, 580, 596, 611, 627, 643, 659, 675]
    精神 = [0, 54, 58, 62, 66, 70, 75, 80, 85, 91, 97, 103, 109, 115, 122, 129, 137, 145, 153, 161, 169, 178, 187, 197, 206, 216, 226, 237, 247, 258, 269,
          281, 293, 305, 317, 329, 343, 356, 369, 383, 397, 411, 425, 441, 455, 471, 487, 503, 519, 535, 552, 566, 582, 598, 614, 630, 645, 661, 677, 693, 709]

    def 体力加成(self):
        return self.体力[self.等级] + self.额外体精 + self.进图加成

    def 精神加成(self):
        return self.精神[self.等级] + self.额外体精 + self.进图加成

    def 结算统计(self, context: Buffer):
        return [0, 0, 0, self.体力加成(), self.精神加成()]
        # 智力 体力 精神  力量  智力  物攻  魔攻 独立


class 神启·圣骑士技能1(辅助职业主动技能):
    名称 = '圣光十字'
    所在等级 = 25
    等级精通 = 50
    等级上限 = 60
    学习间隔 = 2
    三攻 = [0, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
          33, 34, 35, 36, 37, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]

    def 三攻加成(self):
        return self.三攻[self.等级]

    def 结算统计(self, context):
        return [0, self.三攻加成(), 0, 0, 0]


class 神启·圣骑士技能2(辅助职业主动技能):
    名称 = '荣誉祝福'
    所在等级 = 30
    等级精通 = 10
    等级上限 = 40
    学习间隔 = 3

    BUFF力智per = 1.0
    BUFF三攻per = 1.0

    BUFF力智 = 0
    BUFF三攻 = 0

    倍率 = 1.0

    三攻 = [round(i*1.02) for i in [0, 43, 44, 46, 48, 49, 51, 53, 54, 56, 58, 59, 61, 63, 64, 66, 68, 69, 71, 73, 75,
                                  76, 78, 80, 81, 83, 85, 86, 88, 90, 91, 93, 95, 96, 98, 100, 101, 103, 105, 106, 109]]
    力智 = [round(i*1.04) for i in [0, 164, 175, 186, 198, 209, 219, 230, 241, 253, 264, 275, 286, 298, 309, 320, 330, 341, 353, 364,
                                  375, 386, 398, 409, 420, 431, 441, 453, 464, 475, 486, 498, 509, 520, 531, 543, 553, 564, 575, 586, 598]]

    def 结算统计(self, context: Buffer):
        buffer_power = context.BUFF量()

        新词条倍率 = (((self.适用数值 + 4348) / 620 + 1) *
                 (buffer_power + 3488) * 0.0000357) if buffer_power > 0 else 0

        新词条力智 = 新词条倍率 * (self.力智[self.等级])
        新词条三攻 = 新词条倍率 * (self.三攻[self.等级])

        旧词条力智 = ((self.适用数值)/620 + 1) * \
            (self.力智[self.等级]+self.BUFF力智) * self.BUFF力智per

        旧词条三攻 = ((self.适用数值)/620 + 1) * \
            (self.三攻[self.等级]+self.BUFF三攻) * self.BUFF三攻per

        倍率 = self.倍率

        力智 = int((新词条力智 + 旧词条力智) * 倍率)
        三攻 = int((新词条三攻 + 旧词条三攻) * 倍率)

        return [力智, 三攻, 0, 0, 0]


class 神启·圣骑士技能3(辅助职业主动技能):
    名称 = '守护徽章'
    所在等级 = 25
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 2
    增幅倍率 = 0.15
    数值 = [0, 24, 26, 28, 31, 33, 35, 38, 40, 43, 46, 49, 51, 55, 58, 61, 64, 67, 71, 75, 78, 82,
          85, 89, 93, 97, 101, 106, 110, 114, 119, 123, 128, 133, 137, 142, 147, 152, 157, 163, 167]

    def 体精加成(self):
        return int(self.数值[self.等级] * (1 + self.增幅倍率))

    def 结算统计(self, context: Buffer):
        return [0, 0, 0, self.体精加成(), self.体精加成()]


class 神启·圣骑士技能4(辅助职业被动技能):
    名称 = '信念光环'
    所在等级 = 48
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 3
    额外体精 = 0
    力智 = [0, 40, 48, 58, 67, 77, 87, 98, 109, 120, 133, 144, 157, 171, 184, 198, 212, 226, 242, 258, 273,
          290, 306, 323, 341, 359, 378, 397, 416, 436, 456, 476, 498, 518, 541, 562, 586, 609, 632, 654, 678]
    体精 = [0, 31, 38, 45, 53, 60, 68, 76, 85, 94, 104, 113, 123, 134, 144, 154, 166, 177, 189, 202, 213,
          226, 239, 253, 266, 281, 296, 310, 325, 341, 356, 372, 389, 405, 423, 439, 458, 476, 494, 511, 530]

    def 力智加成(self):
        return self.力智[self.等级]

    def 体精加成(self):
        return self.体精[self.等级] + self.额外体精

    def 结算统计(self, context: Buffer):
        return [self.力智加成(), 0, 0, self.体精加成(), self.体精加成()]


class 神启·圣骑士技能5(辅助职业觉醒技能):
    名称 = '天启之珠'
    pass


class 神启·圣骑士技能6(辅助职业主动技能):
    名称 = '神圣洗礼：信仰之翼'
    所在等级 = 85
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 5
    体精 = [0, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45, 47, 50, 52, 55, 57, 60,
          62, 65, 67, 70, 72, 75, 77, 80, 82, 85, 87, 90, 92, 95, 97, 100, 102, 105, 107, 110]

    def 体精加成(self):
        return self.体精[self.等级] * 24

    def 结算统计(self, context: Buffer):
        return [0, 0, 0, self.体精加成(), self.体精加成()]


class 神启·圣骑士技能7(辅助职业被动技能):
    名称 = '神之代行者'
    所在等级 = 95
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 3
    站街生效 = 1
    体精 = [0, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340,
          350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550]

    def 体精加成(self):
        return self.体精[self.等级]

    def 结算统计(self, context: Buffer):
        return [0, 0, 0,  self.体精加成(), self.体精加成()]
        # 力智 三攻 智力 体精


class 神启·圣骑士技能8(辅助职业三觉技能):
    名称 = '生命礼赞：神威'
    关联技能 = ['神圣洗礼：信仰之翼']
    pass


class classChange(Character):
    def __init__(self):

        self.技能序号 = {}
        技能栏 = []
        i = 0
        while i >= 0:
            try:
                skill: 辅助职业技能 = eval("神启·圣骑士技能"+str(i)+"()")
                skill.技能序号 = i
                名称 = skill.名称
                self.技能序号[名称] = i
                if skill.所在等级 == 30:
                    名称 = 'BUFF'
                elif skill.所在等级 == 50:
                    名称 = '一次觉醒'
                elif skill.所在等级 == 85:
                    名称 = '二次觉醒'
                elif skill.所在等级 == 100:
                    名称 = '三次觉醒'
                skill.基础等级计算()
                技能栏.append(skill)
                self.技能序号[名称] = i
                i += 1
            except:
                i = -1
        self.技能栏 = 技能栏
        self.buff = 1.70
        self.护石技能 = [i.skill for i in 男圣骑士护石组合]

        self.实际名称 = 'crusader_male'
        self.名称 = '神启·圣骑士'
        self.角色 = '圣职者(男)'

        self.类型 = '辅助'
        self.职业 = '圣骑士'
        self.转职 = '圣骑士(男)'
        self.武器选项 = ['十字架']
        self.输出类型选项 = ['魔法固伤']
        self.防具精通属性 = ['体力', '精神']
        self.武器类型 = '十字架'
        self.防具类型 = '板甲'
        self.适用属性 = '体力'
        super().__init__()

    def 护石计算(self):
        for 护石 in 男圣骑士护石组合:
            if 护石.skill in self.护石栏:
                护石.effect(self)

    def 职业特殊计算(self):
        for skill in self.技能栏:
            data = skill.结算统计(self)
            info = []

            if(data[3] > 0):
                info.append({
                    'type': '体力',
                    'info': [data[3]],
                    'percent': False
                })
            if(data[4] > 0):
                info.append({
                    'type': '精神',
                    'info': [data[4]],
                    'percent': False
                })
            self.skills_passive[skill.名称]['info'] = info
        pass
