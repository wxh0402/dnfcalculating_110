#看看就行, 计算细节通用的数据

##############增幅################

# 增幅系数 = [0, 1, 2, 3, 4, 6, 8, 10, 12, 13, 17, 33, 50, 67, 108, 150, 192, 267, 342, 417, 500, 583, 667, 750, 833, 917, 1000, 1083, 1167, 1250, 1333, 1417]
# 增幅系数_HF = [0, 1, 2, 3, 4, 6, 8, 10, 22, 28, 35, 42, 50, 67, 108, 150, 192, 267, 342, 417, 500, 583, 667, 750, 833, 917, 1000, 1083, 1167, 1250, 1333, 1417]
增幅系数 = (0, 1, 2, 3, 4, 6, 8, 10, 22, 28, 35, 42, 50, 67, 108, 150, 192, 267,
        342, 417, 500, 583, 667, 750, 833, 917, 1000, 1083, 1167, 1250, 1333,
        1417)
增幅成长系数 = {'稀有': 1, '神器': 1.3, '勇者': 1.1, '传说': 1.4, '史诗': 1.5, '神话': 1.6}
增幅品级加分 = {'稀有': 45, '神器': 45, '勇者': 45, '传说': 46, '史诗': 46, '神话': 46}
# 增幅品级底数 = {'稀有': 5, '神器': 6, '勇者': 5, '传说': 6, '史诗': 7, '神话': 8}
# 增幅品级底数_HF = {'稀有': 10, '神器': 11, '勇者': 10, '传说': 11, '史诗': 12, '神话': 13}
增幅品级底数 = {'稀有': 10, '神器': 11, '勇者': 10, '传说': 11, '史诗': 12, '神话': 13}


def 增幅计算(装备等级, 品质, 强化等级, 版本='GF'):
    if 版本 == 'GF':
        if 品质 == "智慧产物":
            return 0
        #     return int((装备等级 + 增幅品级加分[品质]) * 增幅成长系数[品质] * 增幅系数[强化等级] / 100 - 0.00000001) + 增幅品级底数[品质]
        # else:
        return int((装备等级 + 增幅品级加分[品质]) * 增幅成长系数[品质] * 增幅系数[强化等级] / 100 -
                   0.00000001) + 增幅品级底数[品质] + (0 if 强化等级 < 12 else 5)


###########特殊装备&勋章###########

耳环强化系数 = (0, 83, 124, 166, 207, 248, 314, 370, 426, 482, 621, 970, 1455, 1941,
          2911, 4043, 5175, 7116, 9056, 10997, 13099, 15363, 17627, 19891,
          22155, 24420, 26684, 28948, 31212, 33476, 35740, 38004)
左右强化系数 = (0, 60, 90, 120, 150, 180, 210, 247, 285, 322, 360, 675, 1013, 1350,
          2025, 2813, 3600, 4950, 6300, 7650, 9113, 10688, 12263, 13838, 15413,
          16988, 18563, 20138, 21713, 23288, 24863, 26438)
勋章强化系数 = (0, 100, 120, 144, 173, 208, 250, 300, 320, 360, 400, 610, 1220, 2440,
          2684, 2952, 3838, 4989, 6486, 8432, 10962)
特殊成长系数 = {
    '普通': 0.4,
    '高级': 0.7,
    '稀有': 1,
    '神器': 1.25,
    '传说': 1.35,
    '史诗': 1.45,
    '神话': 1.55
}
特殊品级加分 = {'普通': 24, '高级': 30, '稀有': 26, '神器': 28, '传说': 29, '史诗': 30, '神话': 31}


def 耳环计算(装备等级, 品质, 强化等级):
    if 品质 == "智慧产物":
        return 0
    return int((装备等级 + 特殊品级加分[品质]) / 2400 * 特殊成长系数[品质] * 耳环强化系数[强化等级])


def 左右计算(装备等级, 品质, 强化等级):
    if 品质 == "智慧产物":
        return 0
    return int((装备等级 + 特殊品级加分[品质]) / 2400 * 特殊成长系数[品质] * 左右强化系数[强化等级])


def 勋章计算(装备等级, 品质, 强化等级):
    return int((装备等级 + 特殊品级加分[品质]) / 2400 * 特殊成长系数[品质] * 勋章强化系数[强化等级])


###############武器###############

武器强化系数 = (0, 2, 2.6, 3.6, 4.7, 5.8, 6.9, 8.2, 11, 14.6, 18.7, 26.9, 36.7, 43,
          49.2, 55.4, 61.7, 68, 74.3, 80.6, 86.9, 93.2, 99.5, 105.8, 112.1,
          118.3, 124.6, 130.9, 137.1, 143.4, 149.7, 156.0)
武器锻造系数 = (0, 2, 3, 4, 6, 8, 13, 18, 25, 32, 41)
武器成长系数 = {
    '普通': 0.4,
    '高级': 0.7,
    '稀有': 1,
    '神器': 1.25,
    '勇者': 1.1,
    '传说': 1.35,
    '史诗': 1.45,
    '神话': 1.55
}
武器品级加分 = {
    '普通': 8,
    '高级': 8,
    '稀有': 10,
    '神器': 12,
    '勇者': 11,
    '传说': 13,
    '史诗': 14,
    '神话': 15
}
武器类型系数 = {
    '短剑': (1.095, 1.115),
    '太刀': (1.095, 1.105),
    '钝器': (1.11, 1.095),
    '巨剑': (1.12, 1.09),
    '光剑': (1.093, 1.09),
    '手套': (1.095, 1.115),
    '臂铠': (1.12, 1.09),
    '爪': (1.1, 1.1),
    '拳套': (1.105, 1.095),
    '东方棍': (1.095, 1.1),
    '左轮枪': (1.087, 1.077),
    '自动手枪': (1.064, 1.094),
    '步枪': (1.1, 1.085),
    '手炮': (1.106, 1.064),
    '手弩': (1.075, 1.085),
    '矛': (1.12, 1.085),
    '棍棒': (1.108, 1.09),
    '魔杖': (1.09, 1.11),
    '法杖': (1.095, 1.12),
    '扫把': (1.1, 1.11),
    '十字架': (1.1, 1.095),
    '念珠': (1.09, 1.115),
    '图腾': (1.105, 1.09),
    '镰刀': (1.105, 1.105),
    '战斧': (1.12, 1.085),
    '匕首': (1.09, 1.089),
    '双剑': (1.102, 1.08),
    '手杖': (1.081, 1.115),
    '苦无': (1.09, 1.11),
    '长枪': (1.105, 1.09),
    '战戟': (1.12, 1.085),
    '光枪': (1.095, 1.115),
    '暗矛': (1.095, 1.105),
    '长刀': (1.108, 1.09),
    '小太刀': (1.1, 1.1),
    '重剑': (1.12, 1.09),
    '源力剑': (1.095, 1.115)
}


def 武器强化计算(装备等级, 品质, 强化等级, 武器类型, 类型):
    武器系数 = (武器类型系数[武器类型][0 if 类型 == '物理' else 1])
    return int((装备等级 + 武器品级加分[品质]) / 8 * 武器成长系数[品质] * 武器强化系数[强化等级] * 武器系数)


def 锻造计算(装备等级, 品质, 锻造等级):
    return round((装备等级 + 武器品级加分[品质]) / 8 * 武器成长系数[品质] * 武器锻造系数[锻造等级])


def 锻造四维(装备等级, 品质, 锻造等级):
    return round((装备等级 + 武器品级加分[品质]) / 80 * 武器成长系数[品质] * 武器锻造系数[锻造等级])


# 武器冷却惩罚系数 = {
#     '短剑': (1, 1.05, 1),
#     '太刀': (0.95, 1, 1),
#     '钝器': (1.05, 1, 1),
#     '巨剑': (1.1, 1, 1),
#     '光剑': (0.9, 1, 1),
#     '手套': (0.9, 1.05, 1),
#     '臂铠': (1.1, 1, 1),
#     '爪': (1, 1, 1),
#     '拳套': (0.9, 1, 1),
#     '东方棍': (1, 1, 1),
#     '左轮枪': (1, 1, 1),
#     '自动手枪': (0.9, 1, 1),
#     '步枪': (1.05, 1, 1),
#     '手炮': (1.1, 1, 1),
#     '手弩': (0.9, 1, 1),
#     '矛': (1.05, 0.95, 1),
#     '棍棒': (1, 1, 1),
#     '魔杖': (0.95, 1, 1),
#     '法杖': (1, 1.1, 1),
#     '扫把': (1 ,1, 1),
#     '十字架': (0.95, 1, 1),
#     '念珠': (0.95, 1.05, 1),
#     '图腾': (1, 0.95, 1),
#     '镰刀': (0.95, 1, 1),
#     '战斧': (1.1, 0.9, 1),
#     '匕首': (0.9, 0.95, 1),
#     '双剑': (1.1, 0.9, 1),
#     '手杖': (1, 1.1, 1),
#     '苦无': (1, 1.05, 1),
#     '长枪': (1.05, 1, 1),
#     '战戟': (1.1, 0.9, 1),
#     '光枪': (1, 1.05, 1),
#     '暗矛': (0.95, 1, 1),
#     '长刀': (1.05, 1, 1),
#     '小太刀': (1, 1, 1),
#     '重剑': (1.1, 1, 1),
#     '源力剑': (1, 1.05, 1]}

武器冷却惩罚系数 = {
    '短剑': (1, 1, 1),
    '太刀': (0.95, 0.95, 1),
    '钝器': (1, 1, 1),
    '巨剑': (1.05, 1, 1),
    '光剑': (0.9, 1, 1),
    '手套': (0.9, 1, 1),
    '臂铠': (1.05, 1, 1),
    '爪': (1, 1, 1),
    '拳套': (0.9, 1, 1),
    '东方棍': (1, 1, 1),
    '左轮枪': (0.95, 1, 1),
    '自动手枪': (0.9, 1, 1),
    '步枪': (1, 1, 1),
    '手炮': (1.05, 1, 1),
    '手弩': (0.9, 1, 1),
    '矛': (1, 0.95, 1),
    '棍棒': (0.95, 1, 1),
    '魔杖': (0.95, 1, 1),
    '法杖': (1, 1.05, 1),
    '扫把': (1, 1, 1),
    '十字架': (1, 0.95, 1),
    '念珠': (0.95, 1.05, 1),
    '图腾': (1, 0.95, 1),
    '镰刀': (0.95, 1, 1),
    '战斧': (1.05, 0.9, 1),
    '匕首': (0.9, 0.95, 1),
    '双剑': (1.05, 0.9, 1),
    '手杖': (1, 1.05, 1),
    '苦无': (1, 1, 1),
    '长枪': (1, 1, 1),
    '战戟': (1.1, 0.9, 1),
    '光枪': (1, 1, 1),
    '暗矛': (0.9, 0.9, 1),
    '长刀': (1, 1, 1),
    '小太刀': (0.95, 1, 1),
    '重剑': (1.05, 1, 1),
    '源力剑': (1, 1, 1)
}

MP系数 = {
    '短剑': (1, 1.15, 1),
    '太刀': (0.95, 1.05, 1),
    '钝器': (1.1, 0.95, 1),
    '巨剑': (1.2, 0.9, 1),
    '光剑': (0.9, 1, 1),
    '手套': (0.95, 1.15, 1),
    '臂铠': (1.2, 0.9, 1),
    '爪': (1, 1, 1),
    '拳套': (1.05, 0.95, 1),
    '东方棍': (0.95, 1, 1),
    '左轮枪': (1, 0.9, 1),
    '自动手枪': (0.7, 1.1, 1),
    '步枪': (1.1, 0.95, 1),
    '手炮': (1.25, 0.75, 1),
    '手弩': (0.9, 1, 1),
    '矛': (1.1, 0.95, 1),
    '棍棒': (1, 1, 1),
    '魔杖': (0.95, 1, 1),
    '法杖': (1, 1.1, 1),
    '扫把': (1, 1, 1),
    '十字架': (1, 0.95, 1),
    '念珠': (0.9, 1.15, 1),
    '图腾': (1.05, 0.9, 1),
    '镰刀': (0.95, 1, 1),
    '战斧': (1.2, 0.85, 1),
    '匕首': (1, 0.9, 1),
    '双剑': (1.2, 0.8, 1),
    '手杖': (0.95, 1.15, 1),
    '苦无': (1, 1.1, 1),
    '长枪': (1.1, 1, 1),
    '战戟': (1.2, 0.9, 1),
    '光枪': (1, 1.15, 1),
    '暗矛': (0.95, 1.05, 1),
    '长刀': (1.1, 1, 1),
    '小太刀': (1, 1, 1),
    '重剑': (1.2, 0.9, 1),
    '源力剑': (1, 1.15, 1)
}


def 武器冷却惩罚(武器类型, 输出类型, 版本='GF'):
    类型系数 = (0 if 输出类型 == '物理百分比' else (1 if 输出类型 == '魔法百分比' else 2))
    if 版本 == 'GF':
        return 武器冷却惩罚系数[武器类型][类型系数]
    # else:
    #     return 武器冷却惩罚系数_HF[武器类型][类型系数]


def 武器MP系数(武器类型, 输出类型, 版本='GF') -> float:
    类型系数 = (0 if 输出类型 == '物理百分比' else (1 if 输出类型 == '魔法百分比' else 2))
    if 版本 == 'GF':
        return MP系数[武器类型][类型系数]

#################防具################


部位系数 = {'上衣': 0.30, '头肩': 0.20, '下装': 0.25, '腰带': 0.10, '鞋': 0.15}
品级加分 = {'稀有': 5, '神器': 8, '勇者': 11, '传说': 14, '史诗': 17, '智慧产物': 17, '神话': 18}


def 精通计算(装备等级, 品质, 强化等级, 部位):
    return round((20 + 2.5 * (装备等级 + 品级加分[品质] + int(强化等级 / 3))) * 部位系数[部位], 2)


def 精通体力(装备等级, 品质, 强化等级, 部位):
    return round((4 + (装备等级 + 品级加分[品质] + int(强化等级 / 3))) * 部位系数[部位], 2)


def 精通精神(装备等级, 品质, 强化等级, 部位):
    return 精通体力(装备等级, 品质, 强化等级, 部位) * 2


def 精通智力(装备等级, 品质, 强化等级, 部位):
    return 精通体力(装备等级, 品质, 强化等级, 部位) * 2


#############角色基础属性##############

当前等级 = 110

角色基础系数 = {
    '魔枪士': (4.6, 4.6, 4.4, 4.4, 7, 7, 5, 5),
    '格斗家(女)': (5, 5, 4, 4, 7.5, 7.5, 4.5, 4.5),
    '格斗家(男)': (5, 5, 4, 4, 7.5, 7.5, 4.5, 4.5),
    '枪剑士': (4.6, 4.6, 4.4, 4.4, 7, 7, 5, 5),
    '神枪手(女)': (4.5, 4.5, 4.5, 4.5, 6.5, 6.5, 5.5, 5.5),
    '神枪手(男)': (4.5, 4.5, 4.5, 4.5, 6.5, 6.5, 5.5, 5.5),
    '守护者': (4.8, 4.8, 4.2, 4.2, 7, 7, 5, 5),
    '魔法师(女)': (4, 4, 5, 5, 4.5, 4.5, 7.5, 7.5),
    '魔法师(男)': (3.5, 4, 5.5, 5, 4, 4.5, 8, 7.5),
    '暗夜使者': (5, 4, 5, 4, 7.5, 5.5, 6.5, 4.5),
    '缔造者': (4, 4, 5, 5, 4.5, 4.5, 7.5, 7.5),
    '黑暗武士': (4.8, 4.8, 4.2, 4.2, 7.5, 7.5, 4.5, 4.5),
    '鬼剑士(男)': (4.8, 4.8, 4.2, 4.2, 7.5, 7.5, 4.5, 4.5),
    '鬼剑士(女)': (4.6, 4.6, 4.4, 4.4, 7, 7, 5, 5),
    '圣职者(男)': (4.7, 4.8, 4, 4.5, 6.5, 6.5, 4.5, 6.5),
    '圣职者(女)': (4.7, 4.8, 4, 4.5, 6.5, 6.5, 4.5, 6.5)
}

职业基础数据 = {
    '征战者-魔枪士': (5.5, 5.5, 3.5, 3.5),
    '决战者-魔枪士': (5, 5, 4, 4),
    '狩猎者-魔枪士': (3, 4.5, 6, 4.5),
    '暗枪士-魔枪士': (3.5, 3.5, 5.5, 5.5),
    '气功师-格斗家(女)': (3.5, 3.5, 5.5, 5.5),
    '散打-格斗家(女)': (5.5, 5.5, 3.5, 3.5),
    '街霸-格斗家(女)': (5, 4, 5, 4),
    '柔道家-格斗家(女)': (5, 6, 3.5, 3.5),
    '气功师-格斗家(男)': (3.5, 3.5, 5.5, 5.5),
    '散打-格斗家(男)': (5.5, 5.5, 3.5, 3.5),
    '街霸-格斗家(男)': (5, 4, 5, 4),
    '柔道家-格斗家(男)': (5, 6, 3.5, 3.5),
    '暗刃-枪剑士': (5.5, 5.5, 3.5, 3.5),
    '特工-枪剑士': (5, 5, 4, 4),
    '战线佣兵-枪剑士': (5.2, 5, 3.5, 4.3),
    '源能专家-枪剑士': (3.5, 3.5, 5.5, 5.5),
    '漫游枪手-神枪手(女)': (5.5, 5.5, 3.5, 3.5),
    '枪炮师-神枪手(女)': (5.5, 5.5, 3.5, 3.5),
    '机械师-神枪手(女)': (3.5, 3.5, 5.5, 5.5),
    '弹药专家-神枪手(女)': (4.7, 4.3, 4.7, 4.3),
    '漫游枪手-神枪手(男)': (5.5, 5.5, 3.5, 3.5),
    '枪炮师-神枪手(男)': (5.5, 5.5, 3.5, 3.5),
    '机械师-神枪手(男)': (3.5, 3.5, 5.5, 5.5),
    '弹药专家-神枪手(男)': (4.7, 4.3, 4.7, 4.3),
    '合金战士-神枪手(男)': (5.5, 5.5, 3.5, 3.5),
    '精灵骑士-守护者': (5, 5, 4, 4),
    '混沌魔灵-守护者': (3.5, 3.5, 5.5, 5.5),
    '帕拉丁-守护者': (5, 5.5, 2, 5.5),
    '龙骑士-守护者': (5, 5, 4, 4),
    '元素师-魔法师(女)': (3.5, 3.5, 5.5, 5.5),
    '召唤师-魔法师(女)': (3.8, 3.7, 5.3, 5.2),
    '战斗法师-魔法师(女)': (5, 4, 5, 4),
    '魔道学者-魔法师(女)': (4.5, 4, 5.2, 4.3),
    '小魔女-魔法师(女)': (4.7, 4.8, 5.5, 4.5),
    '元素爆破师-魔法师(男)': (3.5, 3.5, 5.5, 5.5),
    '冰结师-魔法师(男)': (3.5, 3.7, 5.5, 5.2),
    '血法师-魔法师(男)': (5.5, 5.5, 3.5, 3.5),
    '逐风者-魔法师(男)': (5.5, 5.2, 3.5, 3.8),
    '次元行者-魔法师(男)': (3.5, 3.5, 5.5, 5.5),
    '刺客-暗夜使者': (5.3, 4.5, 4.2, 4),
    '死灵术士-暗夜使者': (4.7, 3.5, 5.3, 4.5),
    '忍者-暗夜使者': (4.5, 3.5, 5.5, 4.5),
    '影舞者-暗夜使者': (5.5, 4.5, 4, 4),
    '缔造者-魔法师(女)': (4, 4, 5, 5),
    '黑暗武士-鬼剑士(男)': (4.8, 4.8, 4.2, 4.2),
    '剑魂-鬼剑士(男)': (5, 5, 4, 4),
    '鬼泣-鬼剑士(男)': (3.5, 3.5, 5.5, 5.5),
    '狂战士-鬼剑士(男)': (5.5, 5.5, 3.5, 3.5),
    '阿修罗-鬼剑士(男)': (3, 4.5, 6, 4.5),
    '剑影-鬼剑士(男)': (5, 5, 4, 4),
    '刃影-鬼剑士(女)': (5, 5, 4, 4),
    '驭剑士-鬼剑士(女)': (5, 5, 4, 4),
    '暗殿骑士-鬼剑士(女)': (3.5, 3.5, 5.5, 5.5),
    '契魔者-鬼剑士(女)': (5.5, 5.5, 3.5, 3.5),
    '流浪武士-鬼剑士(女)': (5.5, 5.5, 3.5, 3.5),
    '圣骑士-圣职者(男)': (3.5, 5.5, 3.5, 5.5),
    '蓝拳圣使-圣职者(男)': (5.2, 5, 3.9, 3.9),
    '驱魔师-圣职者(男)': (5, 4, 5, 4),
    '复仇者-圣职者(男)': (3.5, 3.5, 5.5, 5.5),
    '圣骑士-圣职者(女)': (3.5, 5.5, 5.5, 3.5),
    '异端审判者-圣职者(女)': (5.2, 5, 3.5, 4.3),
    '巫女-圣职者(女)': (3.5, 3.5, 5.5, 5.5),
    '诱魔者-圣职者(女)': (3.5, 3.5, 5.5, 5.5)
}


def 获取基础属性(角色, 职业):

    角色数据 = 角色基础系数[角色]
    职业数据 = 职业基础数据[职业 + '-' + 角色]

    唤醒 = (275 if 当前等级 >= 75 else (145 if 当前等级 >= 15 else 0))

    力量 = int(角色数据[4] + 角色数据[0] * min(14, 当前等级 - 1) +
             职业数据[0] * max(当前等级 - 15, 0) + 唤醒 + 2.1 * min(71, 当前等级))
    体力 = int(角色数据[5] + 角色数据[1] * min(14, 当前等级 - 1) +
             职业数据[1] * max(当前等级 - 15, 0) + 唤醒 + 2.0 * min(71, 当前等级))
    智力 = int(角色数据[6] + 角色数据[2] * min(14, 当前等级 - 1) +
             职业数据[2] * max(当前等级 - 15, 0) + 唤醒 + 2.1 * min(71, 当前等级))
    精神 = int(角色数据[7] + 角色数据[3] * min(14, 当前等级 - 1) +
             职业数据[3] * max(当前等级 - 15, 0) + 唤醒 + 2.0 * min(71, 当前等级))
    return (力量, 体力, 智力, 精神)


刀魂之卡赞 = (
    0, 31, 40, 48, 58, 67, 79, 90, 103, 116, 131, 145, 161, 178, 194, 212, 230,
    250, 270, 292, 313
)

部位列表 = ("上衣", "头肩", "下装", "腰带", "鞋", "手镯", "项链", "戒指", "耳环", "辅助装备", "魔法石",
        "武器")

# 成长词条系数 = (0, 3, 5, 8, 10, 13, 16, 18, 21, 24, 34, 37, 40, 43, 46, 49, 51, 54, 56, 59, 74, 76, 79, 81, 84, 86, 88, 91, 93, 96, 109, 111, 113, 116,
#          118, 121, 123, 125, 128, 130, 143, 145, 148, 150, 152, 154, 156, 159, 161, 163, 174, 176, 178, 179, 181, 183, 185, 187, 188, 190, 199,
#          201, 203, 205, 207, 209, 211, 212, 214)
成长词条系数 = (1, 1.01892, 1.03812, 1.05768, 1.07686, 1.09614, 1.1154, 1.13486, 1.15418, 1.26578, 1.28468, 1.3041, 1.3234, 1.3427, 1.36208, 1.3813,
          1.40074, 1.41972, 1.43918, 1.55052, 1.56816, 1.58616, 1.60396, 1.62204, 1.63958, 1.65724, 1.67526, 1.69302, 1.71112, 1.80742, 1.8252, 1.84296,
          1.86088, 1.87846, 1.89654, 1.9142, 1.93186, 1.94984, 1.96764, 2.06414, 2.0803, 2.09704, 2.11324, 2.12946, 2.14578, 2.16194, 2.17854, 2.19482,
          2.2111, 2.29274, 2.3062, 2.3197, 2.33266, 2.34618, 2.35954, 2.37302, 2.38652, 2.39946, 2.41298, 2.47978, 2.49322, 2.50642, 2.5202, 2.53286,
          2.54646, 2.55958, 2.57322, 2.58672)

奶成长词条系数 = (1, 1.01834, 1.03676, 1.05584, 1.07516, 1.09344, 1.11238, 1.13132, 1.14816, 1.26002, 1.27924, 1.2976, 1.31664, 1.33548, 1.35444, 1.373,
           1.3918, 1.4106, 1.42932, 1.53966, 1.55648, 1.57312, 1.58962, 1.6064, 1.62306, 1.63986, 1.65576, 1.67272, 1.68978, 1.78562, 1.80212, 1.81902,
           1.83572, 1.85234, 1.86822, 1.88566, 1.90222, 1.91894, 1.93568, 2.03164, 2.04828, 2.0649, 2.08066, 2.09816, 2.11488, 2.13158, 2.14828, 2.16476,
           2.1816, 2.2628, 2.27512, 2.2873, 2.30012, 2.31294, 2.3254, 2.33782, 2.35032, 2.36264, 2.37524, 2.44208, 2.45452, 2.46678, 2.47964, 2.49128,
           2.5036, 2.5161, 2.52948, 2.54194)


# 目前仅有60级内的词条数据


# def 成长词条计算(基础, 等级):
#    return int(基础 * (1 + 成长词条系数[min(68, 等级 - 1)] / 134.75))
#
#
# def 奶成长词条计算(基础, 等级):
#    if 基础 in [489,494,499,504,509]:
#        return int(基础 * (1 + 成长词条系数[min(68, 等级 - 1)] / 134.75))
#    else:
#        return int(基础 * (1 + 奶成长词条系数[min(68, 等级 - 1)] / 312))


def 成长词条计算(基础, 等级):
    return round(134.73 * round(基础 / 134.73, 2) * 成长词条系数[min(68, 等级 - 1)])


def 奶成长词条计算(基础, 等级):
    if 基础 in [489, 494, 499, 504, 509]:
        return round(134.73 * round(基础 / 134.73, 2) * 成长词条系数[min(68, 等级 - 1)])
    else:
        return round(159.97 * round(基础 / 159.97, 2) * 成长词条系数[min(68, 等级 - 1)])
