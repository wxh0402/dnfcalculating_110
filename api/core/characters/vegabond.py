
from core.baseClass.skill import 技能
from core.baseClass.character import Character
from core.baseClass.skill import 主动技能, 被动技能


class 技能0(被动技能):
    名称 = '返本归元'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.16 + 0.04 * self.等级, 5)


class 技能1(被动技能):
    名称 = '三花聚顶'
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.065 + 0.02 * self.等级, 5)


class 技能2(被动技能):
    名称 = '七星耀华'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能3(被动技能):
    名称 = '剑仙之境'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能4(主动技能):
    名称 = '四象引'
    所在等级 = 20

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 7.0
    TP成长 = 0.10
    TP上限 = 7
    data0 = [0, 3928, 4331, 4714, 5118, 5520, 5912, 6314, 6718, 7120, 7511, 7913, 8306, 8700, 9102, 9504, 9897, 10300, 10702, 11104, 11490, 11889, 12292, 12686, 13087, 13489, 13882, 14285, 14685, 15068, 15473, 15875, 16278, 16669, 17073, 17474, 17867,
             18261, 18663, 19056, 19458, 19861, 20263, 20655, 21058, 21458, 21844, 22247, 22647, 23039, 23443, 23845, 24239, 24640, 25042, 25434, 25828, 26230, 26634, 27028, 27428, 27830, 28213, 28617, 29019, 29423, 29812, 30216, 30618, 31010, 31412]
    MP = [20, 250]


class 技能5(主动技能):
    名称 = '一花渡江'
    所在等级 = 25

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 5.0
    TP成长 = 0.10
    TP上限 = 7
    data0 = [0, 1191, 1311, 1432, 1552, 1674, 1794, 1915, 2036, 2157, 2277, 2398, 2520, 2640, 2761, 2881, 3003, 3123, 3244, 3365, 3486, 3606, 3727, 3848, 3969, 4089, 4211, 4332, 4452, 4573, 4694, 4815, 4935, 5057, 5177,
             5298, 5418, 5540, 5660, 5781, 5902, 6023, 6144, 6264, 6386, 6506, 6627, 6747, 6869, 6989, 7110, 7230, 7352, 7473, 7593, 7715, 7835, 7956, 8076, 8198, 8318, 8439, 8559, 8681, 8801, 8922, 9043, 9164, 9285, 9405, 9527]
    hit0 = 3
    MP = [40, 300]


class 技能6(主动技能):
    名称 = '樱落斩'
    所在等级 = 25

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 7.0
    TP成长 = 0.10
    TP上限 = 7
    data0 = [0, 463, 507, 556, 603, 656, 698, 750, 795, 842, 893, 936, 986, 1033, 1082, 1127, 1175, 1226, 1269, 1320, 1367, 1414, 1462, 1510, 1558, 1604, 1653, 1700, 1747, 1798, 1842, 1891, 1940, 1986, 2035, 2080,
             2130, 2177, 2223, 2272, 2319, 2366, 2414, 2464, 2507, 2559, 2606, 2655, 2701, 2747, 2798, 2842, 2891, 2937, 2985, 3036, 3079, 3130, 3177, 3225, 3270, 3319, 3368, 3414, 3462, 3509, 3557, 3608, 3651, 3702, 3750]
    data1 = [0, 619, 680, 742, 805, 871, 933, 994, 1061, 1124, 1188, 1247, 1317, 1378, 1440, 1504, 1569, 1631, 1692, 1757, 1822, 1888, 1949, 2012, 2076, 2139, 2201, 2265, 2330, 2395, 2455, 2523, 2584, 2647, 2710, 2775,
             2839, 2899, 2965, 3027, 3093, 3156, 3221, 3282, 3345, 3408, 3472, 3536, 3601, 3662, 3728, 3792, 3853, 3917, 3979, 4045, 4106, 4170, 4234, 4299, 4363, 4427, 4490, 4551, 4616, 4678, 4743, 4810, 4869, 4934, 4997]
    data2 = [0, 176, 194, 212, 229, 250, 266, 286, 303, 320, 338, 356, 375, 394, 410, 430, 447, 466, 485, 503, 519, 539, 556, 577, 595, 609, 630, 647, 666, 683, 701, 720, 739, 755, 775, 792, 812,
             830, 848, 865, 883, 900, 920, 936, 955, 974, 992, 1010, 1028, 1045, 1066, 1083, 1100, 1121, 1137, 1154, 1174, 1189, 1209, 1228, 1246, 1266, 1284, 1300, 1319, 1337, 1356, 1373, 1390, 1411, 1427]
    data3 = [0, 1230, 1357, 1482, 1609, 1741, 1860, 1992, 2119, 2247, 2374, 2498, 2626, 2752, 2878, 3010, 3135, 3264, 3387, 3516, 3640, 3770, 3896, 4022, 4154, 4273, 4405, 4533, 4658, 4787, 4910, 5039, 5165, 5291, 5423,
             5550, 5676, 5802, 5927, 6055, 6183, 6309, 6434, 6566, 6687, 6819, 6944, 7072, 7203, 7324, 7455, 7578, 7707, 7836, 7962, 8090, 8214, 8341, 8467, 8595, 8724, 8847, 8979, 9099, 9231, 9359, 9484, 9615, 9736, 9867, 9993]
    hit0 = 1
    hit1 = 1
    hit2 = 8
    hit3 = 1

    MP = [35, 350]


class 技能7(主动技能):
    名称 = '圆舞斩'
    所在等级 = 30

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 11.0
    TP成长 = 0.10
    TP上限 = 7
    data0 = [0, 2960, 3261, 3562, 3862, 4158, 4460, 4761, 5061, 5363, 5662, 5964, 6265, 6560, 6862, 7162, 7463, 7764, 8065, 8367, 8666, 8965, 9263, 9564, 9866, 10165, 10467, 10767, 11067, 11366, 11667, 11969, 12266, 12567, 12871, 13169, 13469,
             13768, 14071, 14370, 14671, 14973, 15273, 15572, 15869, 16170, 16471, 16772, 17074, 17374, 17675, 17970, 18271, 18572, 18873, 19174, 19474, 19776, 20077, 20376, 20672, 20976, 21275, 21574, 21877, 22178, 22478, 22778, 23077, 23379, 23678]
    data1 = [0, 1774, 1956, 2134, 2314, 2496, 2675, 2854, 3036, 3214, 3394, 3578, 3755, 3933, 4116, 4297, 4474, 4657, 4837, 5015, 5195, 5376, 5553, 5736, 5916, 6094, 6277, 6456, 6635, 6816, 6997, 7175, 7356, 7535, 7713, 7896, 8076,
             8259, 8437, 8617, 8796, 8977, 9156, 9340, 9515, 9697, 9878, 10056, 10235, 10418, 10596, 10776, 10959, 11136, 11317, 11498, 11677, 11855, 12039, 12220, 12396, 12579, 12758, 12937, 13117, 13298, 13476, 13658, 13837, 14016, 14198]
    data2 = [0, 1066, 1171, 1284, 1389, 1498, 1606, 1715, 1821, 1929, 2038, 2148, 2253, 2361, 2469, 2579, 2685, 2793, 2900, 3013, 3120, 3228, 3335, 3443, 3552, 3662, 3768, 3876, 3985, 4093, 4199, 4307, 4416, 4526, 4634,
             4742, 4849, 4956, 5062, 5172, 5280, 5389, 5496, 5606, 5713, 5820, 5927, 6035, 6143, 6253, 6362, 6469, 6575, 6688, 6794, 6903, 7012, 7120, 7227, 7335, 7444, 7551, 7658, 7768, 7876, 7983, 8090, 8200, 8308, 8415, 8521]
    hit0 = 1
    # 无法抓取敌人无冲撞攻击力
    hit1 = 0
    hit2 = 1

    MP = [70, 400]

    形态 = ['非抓', '抓取']

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == '非抓':
            self.hit0 = 1
            self.hit1 = 0
            self.hit2 = 1
        if 形态 == '抓取':
            self.hit0 = 2
            self.hit1 = 0
            self.hit2 = 0


class 技能8(主动技能):
    名称 = '碎岩裂地掌'
    所在等级 = 30

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 12.0
    演出时间 = 0.5
    TP成长 = 0.10
    TP上限 = 7
    data0 = [0, 6371, 7014, 7661, 8307, 8954, 9600, 10248, 10893, 11542, 12186, 12833, 13478, 14126, 14770, 15418, 16061, 16711, 17354, 18006, 18650, 19295, 19942, 20588, 21235, 21878, 22527, 23169, 23817, 24462, 25112, 25757, 26405, 27048, 27696, 28340,
             28989, 29633, 30281, 30924, 31575, 32220, 32867, 33512, 34160, 34805, 35451, 36096, 36740, 37389, 38033, 38684, 39327, 39974, 40621, 41266, 41913, 42559, 43204, 43851, 44495, 45146, 45790, 46439, 47082, 47729, 48375, 49023, 49666, 50316, 50959]
    MP = [60, 390]


class 技能9(主动技能):
    名称 = '游龙掌'
    所在等级 = 35

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 12.0
    演出时间 = 1
    TP成长 = 0.10
    TP上限 = 5
    data0 = [int(i*1.051)for i in [0, 838, 927, 1016, 1096, 1184, 1273, 1362, 1444, 1533, 1622, 1708, 1789, 1876, 1967, 2053, 2139, 2229, 2312, 2401, 2487, 2575, 2659, 2747, 2838, 2923, 3004, 3094, 3183, 3268, 3355, 3445, 3528, 3615, 3702, 3791,
                                   3875, 3960, 4053, 4138, 4220, 4307, 4395, 4483, 4571, 4654, 4744, 4831, 4918, 4999, 5090, 5176, 5265, 5354, 5437, 5523, 5610, 5699, 5785, 5869, 5955, 6046, 6131, 6215, 6304, 6391, 6477, 6560, 6651, 6740, 6825]]

    hit0 = 10
    MP = [10, 900]


class 技能10(主动技能):
    名称 = '乱花葬'
    所在等级 = 35

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 25.0
    演出时间 = 1
    TP成长 = 0.10
    TP上限 = 5
    data0 = [int(i*1.054)for i in [0, 320, 370, 421, 472, 523, 575, 625, 676, 727, 778, 830, 880, 931, 982, 1033, 1085, 1135, 1186, 1237, 1288, 1340, 1390, 1441, 1492, 1543, 1594, 1645, 1696, 1747, 1798, 1849, 1900, 1951, 2002, 2053,
                                   2104, 2155, 2205, 2257, 2308, 2359, 2410, 2460, 2512, 2563, 2614, 2665, 2715, 2767, 2818, 2868, 2920, 2970, 3022, 3073, 3123, 3175, 3225, 3277, 3328, 3378, 3430, 3480, 3532, 3583, 3633, 3685, 3735, 3787, 3838]]
    data1 = [int(i*1.054)for i in [0, 3184, 3692, 4199, 4707, 5215, 5723, 6231, 6739, 7246, 7754, 8261, 8769, 9277, 9784, 10292, 10801, 11308, 11816, 12323, 12831, 13339, 13846, 14354, 14861, 15370, 15878, 16385, 16893, 17401, 17908, 18416, 18923, 19431, 19940, 20447,
                                   20955, 21463, 21970, 22478, 22985, 23493, 24001, 24508, 25017, 25525, 26032, 26540, 27047, 27555, 28063, 28570, 29078, 29587, 30094, 30602, 31109, 31617, 32125, 32632, 33140, 33647, 34156, 34664, 35171, 35679, 36186, 36694, 37202, 37709, 38217]]
    data2 = [int(i*1.054)for i in [0, 515, 597, 679, 760, 842, 925, 1007, 1089, 1171, 1254, 1336, 1417, 1499, 1582, 1664, 1746, 1828, 1911, 1993, 2074, 2156, 2238, 2321, 2403, 2485, 2567, 2650, 2731, 2813, 2895, 2977, 3060, 3142, 3224, 3306,
                                   3388, 3470, 3552, 3634, 3717, 3799, 3881, 3963, 4044, 4127, 4209, 4291, 4373, 4456, 4538, 4620, 4701, 4783, 4866, 4948, 5030, 5112, 5195, 5277, 5358, 5440, 5523, 5605, 5687, 5769, 5852, 5934, 6016, 6097, 6179]]
    data3 = [int(i*1.054)for i in [0, 5074, 5882, 6692, 7500, 8308, 9118, 9926, 10736, 11544, 12353, 13162, 13971, 14780, 15589, 16398, 17207, 18015, 18825, 19633, 20443, 21251, 22059, 22869, 23677, 24487, 25295, 26105, 26913, 27722, 28531, 29340, 30149, 30958, 31766, 32576,
                                   33384, 34194, 35002, 35812, 36620, 37428, 38238, 39046, 39856, 40664, 41473, 42282, 43091, 43900, 44709, 45518, 46327, 47135, 47945, 48753, 49563, 50371, 51179, 51989, 52797, 53607, 54415, 55224, 56033, 56842, 57651, 58460, 59269, 60078, 60886]]
    hit0 = 6
    hit1 = 1
    hit2 = 5
    hit3 = 1

    是否有护石 = 1

    MP = [100, 1400]
    无色消耗 = 1

    def 装备护石(self):
        self.hit0 = 6+4
        self.hit1 = 1
        self.hit2 = 5+4
        self.hit3 = 1
        self.倍率 *= 1.07


class 技能11(主动技能):
    名称 = '回天璇鸣剑'
    所在等级 = 40

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 20.0
    演出时间 = 1
    TP成长 = 0.10
    TP上限 = 5
    data0 = [int(i*1.053)for i in [0, 3132, 3433, 3778, 4099, 4400, 4699, 5045, 5345, 5665, 5989, 6312, 6611, 6911, 7258, 7579, 7878, 8224, 8523, 8824, 9167, 9468, 9791, 10089, 10436, 10733, 11057, 11380, 11702, 12002, 12303, 12646, 12946, 13268, 13615, 13915, 14212,
                                   14513, 14859, 15181, 15481, 15825, 16124, 16425, 16747, 17070, 17393, 17692, 18037, 18337, 18660, 18983, 19303, 19603, 19948, 20249, 20549, 20893, 21216, 21517, 21861, 22162, 22461, 22806, 23105, 23427, 23774, 24074, 24372, 24718, 25017]]
    data1 = [int(i*1.053)for i in [0, 9126, 10051, 10979, 11906, 12829, 13758, 14680, 15608, 16536, 17459, 18382, 19312, 20234, 21162, 22089, 23012, 23942, 24865, 25792, 26720, 27642, 28570, 29493, 30422, 31351, 32275, 33197, 34124, 35046, 35975, 36899, 37828, 38754, 39678,
                                   40605, 41529, 42456, 43385, 44308, 45236, 46159, 47087, 48014, 48938, 49862, 50791, 51713, 52640, 53568, 54492, 55420, 56342, 57270, 58199, 59122, 60046, 60972, 61901, 62826, 63753, 64678, 65603, 66525, 67455, 68378, 69304, 70233, 71156, 72085, 73008]]
    power1 = 1.05
    hit0 = 1
    hit1 = 1

    MP = [70, 860]
    无色消耗 = 1


class 技能12(主动技能):
    名称 = '湮烈掌'
    所在等级 = 40

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    data0 = [int(i*1.051)for i in [0, 1589, 1750, 1911, 2072, 2233, 2396, 2557, 2718, 2879, 3040, 3201, 3363, 3524, 3686, 3847, 4008, 4169, 4331, 4492, 4653, 4814, 4975, 5136, 5298, 5459, 5620, 5781, 5942, 6105, 6266, 6428, 6589, 6750, 6911, 7073, 7234,
                                   7395, 7556, 7717, 7878, 8040, 8201, 8362, 8523, 8684, 8845, 9007, 9168, 9329, 9490, 9651, 9813, 9975, 10136, 10297, 10458, 10619, 10780, 10943, 11104, 11265, 11426, 11587, 11748, 11910, 12071, 12232, 12393, 12555, 12716]]
    data1 = [int(i*1.051)for i in [0, 11126, 12255, 13385, 14513, 15641, 16771, 17899, 19029, 20157, 21286, 22415, 23543, 24671, 25802, 26930, 28059, 29187, 30316, 31446, 32574, 33702, 34832, 35960, 37090, 38218, 39348, 40476, 41604, 42735, 43863, 44991, 46120, 47248, 48378,
                                   49507, 50635, 51764, 52893, 54021, 55151, 56279, 57409, 58537, 59665, 60796, 61924, 63053, 64181, 65309, 66440, 67568, 68697, 69825, 70954, 72083, 73212, 74341, 75470, 76598, 77727, 78857, 79986, 81114, 82242, 83371, 84501, 85629, 86758, 87886, 89016]]
    hit0 = 3
    hit1 = 1

    是否有护石 = 1

    MP = [350, 3000]
    无色消耗 = 1

    def 装备护石(self):
        self.hit0 = 1+3.11
        self.hit1 = 1+0.27


class 技能13(主动技能):
    名称 = '花舞千魂杀'
    所在等级 = 45

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5
    data0 = [int(i*1.052)for i in [0, 10944, 12088, 13170, 14317, 15485, 16590, 17755, 18855, 19992, 21131, 22242, 23398, 24513, 25669, 26816, 27908, 29059, 30166, 31302, 32458, 33572, 34711, 35854, 36977, 38109, 39256, 40385, 41529, 42619, 43759, 44902, 46006, 47164, 48273,
                                   49419, 50556, 51679, 52838, 53958, 55085, 56229, 57333, 58469, 59605, 60728, 61868, 63016, 64119, 65266, 66393, 67607, 68751, 69892, 71035, 72156, 73279, 74440, 75572, 76684, 77829, 78965, 80093, 81248, 82379, 83504, 84639, 85796, 86935, 88055, 89212]]
    data1 = [int(i*1.052)for i in [0, 1504, 1661, 1816, 1971, 2131, 2286, 2444, 2595, 2753, 2912, 3062, 3221, 3374, 3532, 3691, 3842, 4001, 4153, 4307, 4466, 4620, 4775, 4934, 5094, 5245, 5404, 5558, 5718, 5866, 6025, 6181, 6333, 6492, 6643, 6801,
                                   6956, 7114, 7270, 7429, 7583, 7740, 7893, 8051, 8207, 8360, 8519, 8674, 8827, 8985, 9139, 9309, 9467, 9620, 9778, 9935, 10087, 10246, 10403, 10554, 10713, 10874, 11024, 11185, 11343, 11494, 11651, 11811, 11964, 12118, 12280]]
    data2 = [int(i*1.052)for i in [0, 6018, 6650, 7254, 7887, 8519, 9139, 9769, 10383, 11013, 11635, 12251, 12883, 13503, 14132, 14765, 15370, 16002, 16611, 17235, 17865, 18480, 19101, 19735, 20364, 20973, 21607, 22230, 22863, 23462, 24098, 24727, 25332, 25963, 26575, 27206,
                                   27827, 28460, 29092, 29705, 30325, 30956, 31568, 32192, 32824, 33439, 34066, 34698, 35303, 35934, 36557, 37222, 37854, 38475, 39104, 39735, 40349, 40980, 41612, 42218, 42846, 43478, 44100, 44732, 45359, 45975, 46607, 47238, 47859, 48473, 49120]]
    hit0 = 1
    hit1 = 2
    hit2 = 1
    无色消耗 = 2
    MP = [130, 2100]

    是否有护石 = 1

    def 装备护石(self):
        self.hit0 = 1+1.33
        self.hit1 = 0
        self.hit2 = 0


class 技能14(主动技能):
    名称 = '花开寒影'
    所在等级 = 50

    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    CD = 145
    data0 = [0, 7218, 8891, 10565, 12238, 13912, 15587, 17259, 18933, 20606, 22280, 23955, 25627, 27301, 28974, 30649, 32323, 33995, 35669, 37342,
             39017, 40689, 42363, 44037, 45713, 47386, 49060, 50732, 52407, 54081, 55754, 57428, 59100, 60775, 62449, 64122, 65796, 67469, 69143, 70817, 72490]
    data1 = [0, 1109, 1368, 1624, 1883, 2140, 2397, 2653, 2913, 3169, 3427, 3684, 3942, 4200, 4456, 4715, 4972, 5229, 5487, 5745, 6001,
             6259, 6518, 6774, 7032, 7290, 7547, 7805, 8062, 8319, 8576, 8835, 9091, 9349, 9607, 9864, 10120, 10380, 10636, 10893, 11153]
    data2 = [0, 45931, 56580, 67231, 77883, 88533, 99183, 109835, 120485, 144249, 155967, 167681, 179397, 191113, 202828, 214545, 226259, 237976, 249690, 261407, 273124,
             284838, 296554, 308268, 319986, 331702, 343416, 355134, 366849, 378564, 390281, 401995, 413712, 425427, 437143, 448860, 460574, 472291, 484006, 495721, 507439]

    hit0 = 1
    hit1 = 13
    hit2 = 1

    MP = [1500, 12232]
    无色消耗 = 5


class 技能15(主动技能):
    名称 = '啸空十字斩'
    所在等级 = 60

    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    data0 = [int(i*1.054)for i in [0, 5188, 5715, 6241, 6767, 7294, 7820, 8346, 8872, 9399, 9926, 10451, 10978, 11504, 12030, 12555, 13082, 13609, 14135, 14661, 15187, 15714, 16238, 16765, 17292, 17818, 18344, 18871, 19397, 19924, 20449, 20977, 21504, 22030, 22556, 23082,
                                   23609, 24135, 24660, 25187, 25713, 26240, 26766, 27292, 27819, 28345, 28871, 29398, 29924, 30451, 30978, 31503, 32030, 32554, 33081, 33607, 34134, 34659, 35186, 35713, 36239, 36765, 37292, 37818, 38345, 38870, 39397, 39924, 40450, 40976, 41502]]
    data1 = [int(i*1.054)for i in [0, 6053, 6666, 7281, 7894, 8508, 9123, 9737, 10349, 10964, 11579, 12193, 12807, 13421, 14035, 14649, 15262, 15878, 16490, 17104, 17720, 18334, 18947, 19562, 20175, 20790, 21404, 22017, 22632, 23246, 23860, 24473, 25087, 25701, 26316, 26930,
                                   27543, 28158, 28771, 29386, 30000, 30613, 31228, 31842, 32456, 33070, 33683, 34297, 34913, 35527, 36140, 36755, 37369, 37984, 38596, 39210, 39825, 40439, 41053, 41667, 42281, 42894, 43508, 44123, 44736, 45351, 45965, 46580, 47192, 47806, 48421]]
    data2 = [int(i*1.054)for i in [0, 6918, 7619, 8321, 9022, 9725, 10425, 11128, 11830, 12533, 13233, 13936, 14637, 15338, 16041, 16742, 17444, 18145, 18848, 19550, 20251, 20953, 21656, 22356, 23059, 23760, 24462, 25164, 25866, 26567, 27268, 27971, 28674, 29374, 30076, 30779,
                                   31479, 32182, 32883, 33585, 34287, 34989, 35691, 36392, 37094, 37797, 38496, 39199, 39902, 40601, 41305, 42005, 42707, 43409, 44111, 44813, 45514, 46216, 46919, 47619, 48321, 49024, 49724, 50427, 51128, 51831, 52532, 53234, 53936, 54637, 55339]]
    hit0 = 1
    hit1 = 1
    hit2 = 1

    是否有护石 = 1

    无色消耗 = 1
    MP = [450, 1200]

    def 装备护石(self):
        self.hit0 = 1
        self.hit1 = 0
        self.hit2 = 1.88
        self.CDR *= 0.80
        self.倍率 *= 1.09


class 技能16(主动技能):
    名称 = '如来神掌'
    所在等级 = 70

    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    data0 = [int(i*1.055)for i in [0, 13098, 14427, 15758, 17085, 18414, 19741, 21073, 22399, 23730, 25061, 26386, 27715, 29043, 30374, 31703, 33030, 34362, 35687, 37018, 38348, 39676, 41004, 42331, 43664, 44993, 46319, 47650, 48977, 50307, 51632, 52965, 54294, 55622, 56953, 58281,
                                   59608, 60935, 62267, 63595, 64923, 66254, 67583, 68910, 70237, 71570, 72897, 74224, 75555, 76884, 78212, 79540, 80871, 82198, 83526, 84858, 86185, 87513, 88844, 90173, 91499, 92829, 94159, 95486, 96814, 98147, 99474, 100801, 102130, 103462, 104788]]
    data1 = [int(i*1.055)for i in [0, 19648, 21641, 23635, 25628, 27623, 29610, 31606, 33598, 35593, 37586, 39580, 41572, 43568, 45560, 47551, 49546, 51538, 53533, 55525, 57520, 59512, 61507, 63496, 65491, 67483, 69478, 71469, 73464, 75457, 77452, 79446, 81436, 83430, 85422, 87417, 89409,
                                   91405, 93397, 95392, 97380, 99375, 101367, 103361, 105354, 107350, 109343, 111337, 113329, 115319, 117313, 119306, 121302, 123295, 125289, 127281, 129276, 131268, 133259, 135251, 137247, 139238, 141234, 143226, 145220, 147214, 149204, 151198, 153192, 155187, 157178]]
    hit0 = 1
    hit1 = 1

    MP = [800, 1700]
    无色消耗 = 2

    是否有护石 = 1

    def 装备护石(self):
        self.hit0 = 1 + 1.71 + 0.45
        self.hit1 = 0


class 技能17(主动技能):
    名称 = '莲花剑舞'
    所在等级 = 75

    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    CD = 40.0
    data0 = [int(i*1.052)for i in [0, 2717, 2992, 3268, 3545, 3819, 4095, 4370, 4647, 4921, 5197, 5473, 5749, 6023, 6300, 6575, 6852, 7129, 7404, 7677, 7954, 8229, 8503, 8783, 9058, 9332, 9606, 9882, 10157, 10433, 10712, 10986, 11260, 11538, 11811, 12087, 12362,
                                   12640, 12914, 13192, 13466, 13741, 14015, 14295, 14570, 14844, 15122, 15395, 15670, 15947, 16225, 16498, 16775, 17050, 17324, 17602, 17875, 18153, 18430, 18705, 18978, 19253, 19530, 19805, 20082, 20358, 20634, 20907, 21184, 21459, 21733]]
    data1 = [int(i*1.052)for i in [0, 4075, 4488, 4901, 5315, 5728, 6144, 6556, 6969, 7382, 7795, 8209, 8623, 9037, 9449, 9863, 10277, 10689, 11103, 11518, 11932, 12343, 12756, 13173, 13586, 13997, 14413, 14827, 15237, 15653, 16066, 16481, 16889, 17304, 17717, 18129,
                                   18545, 18958, 19373, 19784, 20198, 20614, 21027, 21438, 21853, 22268, 22678, 23093, 23508, 23921, 24333, 24749, 25162, 25574, 25988, 26401, 26816, 27228, 27642, 28055, 28470, 28882, 29295, 29709, 30123, 30536, 30949, 31365, 31774, 32189, 32603]]
    data2 = [int(i*1.052)for i in [0, 4075, 4488, 4901, 5315, 5728, 6144, 6556, 6969, 7382, 7795, 8209, 8623, 9037, 9449, 9863, 10277, 10689, 11103, 11518, 11932, 12343, 12756, 13173, 13586, 13997, 14413, 14827, 15237, 15653, 16066, 16481, 16889, 17304, 17717, 18129,
                                   18545, 18958, 19373, 19784, 20198, 20614, 21027, 21438, 21853, 22268, 22678, 23093, 23508, 23921, 24333, 24749, 25162, 25574, 25988, 26401, 26816, 27228, 27642, 28055, 28470, 28882, 29295, 29709, 30123, 30536, 30949, 31365, 31774, 32189, 32603]]
    data3 = [int(i*1.052)for i in [0, 16301, 17956, 19609, 21264, 22917, 24570, 26224, 27877, 29532, 31185, 32839, 34492, 36146, 37800, 39454, 41109, 42760, 44414, 46067, 47724, 49378, 51028, 52683, 54339, 55992, 57644, 59298, 60953, 62605, 64259, 65913, 67568, 69221, 70875, 72528, 74182,
                                   75836, 77490, 79142, 80796, 82451, 84106, 85759, 87411, 89067, 90717, 92371, 94028, 95682, 97335, 98989, 100644, 102296, 103949, 105603, 107255, 108910, 110564, 112217, 113872, 115528, 117179, 118832, 120485, 122140, 123793, 125448, 127103, 128757, 130410]]
    hit0 = 2
    hit1 = 2
    hit2 = 2
    hit3 = 2

    是否有护石 = 1

    无色消耗 = 3
    MP = [800, 6000]

    def 装备护石(self):
        self.倍率 *= 1.33


class 技能18(主动技能):
    名称 = '樱花劫'
    所在等级 = 80

    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    CD = 45.0
    data0 = [int(i*1.053)for i in [0, 64519, 71064, 77606, 84153, 90698, 97245, 103790, 110336, 116880, 123428, 129972, 136519, 143063, 149607, 156153, 162700, 169244, 175792, 182334, 188881, 195427, 201972, 208519, 215064, 221607, 228153, 234698, 241246, 247789, 254336, 260880, 267428, 273972, 280519, 287062,
                                   293608, 300152, 306699, 313244, 319789, 326335, 332881, 339427, 345973, 352516, 359064, 365608, 372150, 378697, 385242, 391788, 398335, 404880, 411424, 417972, 424516, 431063, 437607, 444152, 450696, 457244, 463788, 470334, 476878, 483425, 489971, 496516, 503062, 509608, 516153]]

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self):
        self.倍率 *= 1.3
        self.CDR *= 0.9

    无色消耗 = 5
    MP = [580, 4500]


class 技能19(主动技能):
    名称 = '飞花逐月'
    所在等级 = 85

    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    CD = 180.0
    data0 = [int(x*1.09723) for x in [0, 3322, 4092, 4862, 5633, 6403, 7173, 7944, 8711, 9483, 10254, 11024, 11793, 12563, 13335, 14105, 14873, 15646, 16413, 17184, 17956, 18724, 19496, 20267, 21033, 21806, 22576, 23345, 24116, 24886, 25657, 26426, 27196, 27966, 28737, 29508,
                                      30280, 31046, 31817, 32588, 33358, 34128, 34899, 35667, 36439, 37209, 37979, 38749, 39520, 40288, 41059, 41829, 42600, 43369, 44141, 44909, 45679, 46452, 47219, 47990, 48762, 49529, 50301, 51072, 51842, 52613, 53382, 54151, 54922, 55691, 56463]]
    data1 = [int(x*1.09723) for x in [0, 69749, 85921, 102096, 118267, 134441, 150617, 166789, 182963, 199135, 215308, 231483, 247656, 263830, 280002, 296178, 312352, 328523, 344698, 360870, 377046, 393217, 409391, 425565, 441739, 457912, 474085, 490260, 506434, 522604, 538781, 554953, 571125, 587298, 603473, 619648,
                                      635821, 651995, 668167, 684340, 700515, 716687, 732860, 749034, 765208, 781385, 797555, 813728, 829901, 846076, 862249, 878423, 894598, 910768, 926942, 943113, 959290, 975463, 991637, 1007811, 1023985, 1040159, 1056329, 1072502, 1088676, 1104851, 1121025, 1137197, 1153372, 1169546, 1185715]]
    hit0 = 23
    hit1 = 1

    无色消耗 = 10
    MP = [2500, 5000]


class 技能20(主动技能):
    名称 = '落英惊鸿掌'
    所在等级 = 95

    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    CD = 60.0
    data0 = [0, 10545, 11615, 12684, 13754, 14824, 15894, 16964, 18034, 19103, 20173, 21243, 22313, 23383, 24453, 25522, 26592, 27662, 28732, 29802,
             30871, 31941, 33011, 34081, 35151, 36221, 37290, 38360, 39430, 40500, 41570, 42639, 43709, 44779, 45849, 46919, 47989, 49058, 50128, 51198, 52268]
    data1 = [0, 5272, 5807, 6342, 6877, 7412, 7947, 8482, 9017, 9551, 10086, 10621, 11156, 11691, 12226, 12761, 13296, 13831, 14366, 14901, 15435,
             15970, 16505, 17040, 17575, 18110, 18645, 19180, 19715, 20250, 20785, 21319, 21854, 22389, 22924, 23459, 23994, 24529, 25064, 25599, 26134]
    data2 = [0, 73817, 81306, 88794, 96283, 103772, 111261, 118749, 126238, 133727, 141216, 148704, 156193, 163682, 171171, 178659, 186148, 193637, 201125, 208614, 216103,
             223592, 231080, 238569, 246058, 253547, 261035, 268524, 276013, 283501, 290990, 298479, 305968, 313456, 320945, 328434, 335923, 343411, 350900, 358389, 365878]

    hit0 = 1
    hit1 = 4
    hit2 = 1

    无色消耗 = 7
    MP = [773, 6000]


class 技能21(主动技能):
    名称 = '轻云出月风静夜'
    所在等级 = 100

    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    CD = 290.0
    data0 = [int(x*1.095) for x in [0, 384840, 474079, 563317, 652556, 741794, 831033, 920271, 1009510, 1098748, 1187987, 1277225, 1366464, 1455702, 1544941, 1634179, 1723418, 1812656, 1901895, 1991133, 2080372,
                                    2169610, 2258849, 2348087, 2437326, 2526564, 2615803, 2705041, 2794280, 2883518, 2972757, 3061995, 3151234, 3240472, 3329711, 3418949, 3508188, 3597426, 3686665, 3775903, 3865142]]
    无色消耗 = 15
    MP = [4028, 8056]


class 技能22(被动技能):
    名称 = '光剑掌握'
    所在等级 = 15
    等级上限 = 1
    基础等级 = 1
    关联技能 = ['无']
    冷却关联技能 = ['所有']
    非冷却关联技能 = ['花开寒影', '飞花逐月', '轻云出月风静夜']

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '光剑':
            return 1.0
        else:
            return 0.9


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'vegabond'
        self.名称 = '极诣·流浪武士'
        self.角色 = '鬼剑士(女)'
        self.角色类型 = '输出'
        self.职业 = '流浪武士'
        self.武器选项 = ['光剑', '巨剑', '钝器', '太刀', '短剑']
        self.输出类型选项 = ['物理百分比']
        self.防具精通属性 = ['力量']
        self.类型 = '物理百分比'
        self.武器类型 = '光剑'
        self.防具类型 = '皮甲'
        技能列表 = []
        技能序号 = {}
        i = 0
        while i >= 0:
            try:
                tem = eval('技能'+str(i)+'()')
                tem.基础等级计算()
                技能序号[tem.名称] = i
                技能列表.append(tem)
                i += 1
            except:
                i = -1
        self.技能栏 = 技能列表
        self.技能序号 = 技能序号
        self.buff = 2.25

        super().__init__()

    def 职业特殊计算(self):
        # 默认105光剑
        from core.baseClass.equipment import equ
        from core.equipment.基础函数 import 武器强化计算
        temp = equ.get_equ_by_id(98)
        物理攻击力 = 武器强化计算(temp.等级, temp.品质, self.打造详情.get("副武器", {"cursed_number": 0}).get('cursed_number', 0), temp.类型,
                       '物理')

        self.基础属性加成(物理攻击力=int((物理攻击力+temp.物理攻击力)*0.1), 力量=int(temp.力量*0.1))
