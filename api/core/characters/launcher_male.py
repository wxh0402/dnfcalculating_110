
from core.baseClass.skill import 技能
from core.baseClass.character import Character
from core.baseClass.skill import 主动技能, 被动技能


class 主动技能(主动技能):
    def 等效CD(self, **argv):
        # 重火器精通取消除觉醒之外的技能惩罚
        if self.所在等级 not in [50, 85, 100] and argv.get('武器类型', '') == '手炮':
            return round(super().等效CD(**argv) * 0.9, 1)  # 重火器精通
        else:
            return super().等效CD(**argv)

    def 基础等级计算(self):
        if self.基础等级 == 0:
            super().基础等级计算()
            if self.所在等级 not in [50, 85, 100] and self.是否主动 == 1:
                self.基础等级 = min(self.基础等级 + 1, self.等级上限)


class 技能0(主动技能):
    名称 = 'M137格林机枪'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [0, 60, 66, 72, 78, 85, 91, 97, 103, 109, 115, 121, 127, 134, 140, 146, 152, 158, 164, 170, 177, 183, 189, 195, 201, 207, 213, 220, 226, 232, 238, 244, 250, 256, 262, 269,
             275, 281, 287, 293, 299, 305, 312, 318, 324, 330, 336, 342, 348, 355, 361, 367, 373, 379, 385, 391, 397, 404, 410, 416, 422, 428, 434, 440, 447, 453, 459, 465, 471, 477, 483]
    hit0 = 30
    CD = 5.0
    TP成长 = 0.1
    TP上限 = 7

    MP = [10, 252]
    无色消耗 = 0


class 技能1(被动技能):
    名称 = '重火器精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    学习间隔 = 3
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.01 * self.等级, 5)

    def MP消耗量比率(self):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 - 0.03 * self.等级, 5)


class 技能2(主动技能):
    名称 = '加农炮'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [0, 1340, 1476, 1612, 1749, 1885, 2021, 2157, 2293, 2429, 2565, 2701, 2837, 2973, 3109, 3245, 3381, 3517, 3653, 3789, 3925, 4061, 4197, 4333, 4469, 4605, 4741, 4877, 5013, 5149, 5285, 5421, 5558, 5694, 5830, 5966,
             6102, 6238, 6374, 6510, 6646, 6782, 6918, 7054, 7190, 7326, 7462, 7598, 7734, 7870, 8006, 8142, 8278, 8414, 8550, 8686, 8822, 8958, 9094, 9230, 9366, 9503, 9639, 9775, 9911, 10047, 10183, 10319, 10455, 10591, 10727]
    hit0 = 2
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 7
    MP = [30, 280]
    无色消耗 = 0


class 技能3(主动技能):
    名称 = '反坦克炮'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [0, 618, 681, 743, 806, 869, 932, 994, 1057, 1120, 1183, 1245, 1308, 1371, 1434, 1496, 1559, 1622, 1685, 1747, 1810, 1873, 1936, 1998, 2061, 2124, 2187, 2249, 2312, 2375, 2437, 2500, 2563, 2626, 2688, 2751,
             2814, 2877, 2939, 3002, 3065, 3128, 3190, 3253, 3316, 3379, 3441, 3504, 3567, 3630, 3692, 3755, 3818, 3881, 3943, 4006, 4069, 4132, 4194, 4257, 4320, 4382, 4445, 4508, 4571, 4633, 4696, 4759, 4822, 4884, 4947]
    data1 = [0, 2473, 2724, 2975, 3226, 3477, 3728, 3979, 4230, 4481, 4732, 4983, 5234, 5485, 5736, 5987, 6238, 6489, 6740, 6991, 7242, 7493, 7744, 7995, 8246, 8497, 8748, 8999, 9249, 9500, 9751, 10002, 10253, 10504, 10755, 11006, 11257,
             11508, 11759, 12010, 12261, 12512, 12763, 13014, 13265, 13516, 13767, 14018, 14269, 14520, 14771, 15022, 15273, 15524, 15775, 16026, 16277, 16528, 16779, 17030, 17280, 17531, 17782, 18033, 18284, 18535, 18786, 19037, 19288, 19539, 19790]
    hit1 = 1
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 7

    MP = [40, 392]
    无色消耗 = 0


class 技能4(被动技能):
    名称 = '超动力补给包'
    所在等级 = 25
    等级上限 = 11
    基础等级 = 1
    学习间隔 = 3

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.09 + 0.01 * self.等级, 5)


class 技能5(主动技能):
    名称 = '激光炮'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [0, 3256, 3587, 3917, 4247, 4578, 4908, 5239, 5569, 5899, 6230, 6560, 6891, 7221, 7551, 7882, 8212, 8543, 8873, 9203, 9534, 9864, 10195, 10525, 10855, 11186, 11516, 11846, 12177, 12507, 12838, 13168, 13498, 13829, 14159, 14490, 14820,
             15150, 15481, 15811, 16142, 16472, 16802, 17133, 17463, 17794, 18124, 18454, 18785, 19115, 19446, 19776, 20106, 20437, 20767, 21098, 21428, 21758, 22089, 22419, 22749, 23080, 23410, 23741, 24071, 24401, 24732, 25062, 25393, 25723, 26053]
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 7

    MP = [61, 512]
    无色消耗 = 0


class 技能6(被动技能):
    名称 = '蓄电激光炮'
    所在等级 = 25
    等级上限 = 11
    基础等级 = 1
    学习间隔 = 2
    关联技能 = ['激光炮']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.45 + 0.05 * self.等级, 5)


class 技能7(主动技能):
    名称 = '聚焦喷火器'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [0, 294, 324, 354, 384, 414, 444, 473, 503, 533, 563, 593, 623, 653, 683, 713, 742, 772, 802, 832, 862, 892, 922, 952, 982, 1011, 1041, 1071, 1101, 1131, 1161, 1191, 1221, 1251, 1280, 1310, 1340,
             1370, 1400, 1430, 1460, 1490, 1519, 1549, 1579, 1609, 1639, 1669, 1699, 1729, 1759, 1788, 1818, 1848, 1878, 1908, 1938, 1968, 1998, 2028, 2057, 2087, 2117, 2147, 2177, 2207, 2237, 2267, 2297, 2326, 2356]
    hit0 = 29
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 7

    MP = [130, 980]
    无色消耗 = 0


class 技能8(主动技能):
    名称 = 'FM31榴弹发射器'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [0, 2322, 2557, 2793, 3028, 3264, 3499, 3735, 3971, 4206, 4442, 4677, 4913, 5148, 5384, 5620, 5855, 6091, 6326, 6562, 6797, 7033, 7268, 7504, 7740, 7975, 8211, 8446, 8682, 8917, 9153, 9389, 9624, 9860, 10095, 10331, 10566, 10802,
             11038, 11273, 11509, 11744, 11980, 12215, 12451, 12687, 12922, 13158, 13393, 13629, 13864, 14100, 14336, 14571, 14807, 15042, 15278, 15513, 15749, 15985, 16220, 16456, 16691, 16927, 17162, 17398, 17634, 17869, 18105, 18340, 18576]
    hit0 = 4
    CD = 15.0
    TP成长 = 0.20
    TP上限 = 1

    MP = [50, 630]
    无色消耗 = 0

    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 0.64 * 2


class 技能9(主动技能):
    名称 = 'FM92刺弹炮'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [0, 2326, 2562, 2798, 3034, 3270, 3506, 3742, 3978, 4214, 4450, 4686, 4922, 5158, 5394, 5630, 5866, 6102, 6338, 6574, 6810, 7046, 7282, 7518, 7754, 7990, 8226, 8462, 8698, 8934, 9170, 9406, 9642, 9878, 10114, 10351, 10587, 10823,
             11059, 11295, 11531, 11767, 12003, 12239, 12475, 12711, 12947, 13183, 13419, 13655, 13891, 14127, 14363, 14599, 14835, 15071, 15307, 15543, 15779, 16015, 16251, 16487, 16723, 16959, 17195, 17431, 17667, 17903, 18139, 18375, 18611]
    hit0 = 5
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5

    MP = [164, 1376]
    无色消耗 = 1


class 技能10(主动技能):
    名称 = '量子爆弹'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [0, 2862, 3152, 3443, 3733, 4023, 4314, 4604, 4894, 5185, 5475, 5766, 6056, 6346, 6637, 6927, 7218, 7508, 7798, 8089, 8379, 8669, 8960, 9250, 9541, 9831, 10121, 10412, 10702, 10993, 11283, 11573, 11864, 12154, 12444, 12735, 13025,
             13316, 13606, 13896, 14187, 14477, 14767, 15058, 15348, 15639, 15929, 16219, 16510, 16800, 17091, 17381, 17671, 17962, 18252, 18542, 18833, 19123, 19414, 19704, 19994, 20285, 20575, 20865, 21156, 21446, 21737, 22027, 22317, 22608, 22898]
    hit0 = 1

    data1 = [0, 9064, 9983, 10903, 11822, 12742, 13661, 14581, 15500, 16420, 17339, 18259, 19178, 20098, 21018, 21937, 22857, 23776, 24696, 25615, 26535, 27454, 28374, 29293, 30213, 31133, 32052, 32972, 33891, 34811, 35730, 36650, 37569, 38489, 39408,
             40328, 41247, 42167, 43087, 44006, 44926, 45845, 46765, 47684, 48604, 49523, 50443, 51362, 52282, 53202, 54121, 55041, 55960, 56880, 57799, 58719, 59638, 60558, 61477, 62397, 63316, 64236, 65156, 66075, 66995, 67914, 68834, 69753, 70673, 71592, 72512]
    hit1 = 1

    感电data0 = [0, 12, 12, 13, 15, 15, 16, 17, 18, 19, 21, 22, 23, 24, 24, 25, 27, 28, 29, 30, 32, 33, 34, 35, 35, 36, 38, 39, 40, 41, 42, 44, 45, 45,
               46, 47, 49, 50, 51, 52, 53, 55, 56, 56, 57, 58, 59, 61, 62, 63, 64, 66, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 76, 78, 79, 80, 81, 83, 84, 85, 86]
    感电hit0 = 1

    CD = 18.0
    TP成长 = 0.10
    TP上限 = 5

    MP = [164, 1376]
    无色消耗 = 1

    是否有护石 = 1

    def 装备护石(self):
        self.hit0 = 0
        self.hit1 *= 0.20 * 9
        self.感电hit0 *= 0.20 * 9


class 技能11(主动技能):
    名称 = 'X1压缩量子炮'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [0, 26602, 29301, 32000, 34699, 37398, 40096, 42795, 45494, 48193, 50892, 53591, 56289, 58988, 61687, 64386, 67085, 69784, 72482, 75181, 77880, 80579, 83278, 85977, 88675, 91374, 94073, 96772, 99471, 102170, 104868, 107567, 110266, 112965, 115664, 118363, 121061,
             123760, 126459, 129158, 131857, 134556, 137254, 139953, 142652, 145351, 148050, 150749, 153447, 156146, 158845, 161544, 164243, 166942, 169640, 172339, 175038, 177737, 180436, 183135, 185833, 188532, 191231, 193930, 196629, 199328, 202026, 204725, 207424, 210123, 212822]
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5

    MP = [350, 2940]
    无色消耗 = 2

    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.2768


class 技能12(被动技能):
    名称 = '卫星定位'
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.075 + 0.015 * self.等级, 5)


class 技能13(主动技能):
    名称 = '卫星射线'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40
    data0 = [0, 4495, 5537, 6580, 7622, 8665, 9707, 10749, 11792, 12834, 13877, 14919, 15961, 17004, 18046, 19089, 20131, 21173, 22216, 23258, 24301, 25343, 26385, 27428, 28470, 29513, 30555, 31598, 32640, 33682, 34725, 35767, 36810, 37852, 38894, 39937,
             40979, 42022, 43064, 44106, 45149, 46191, 47234, 48276, 49318, 50361, 51403, 52446, 53488, 54530, 55573, 56615, 57658, 58700, 59743, 60785, 61827, 62870, 63912, 64955, 65997, 67039, 68082, 69124, 70167, 71209, 72251, 73294, 74336, 75379, 76421]
    hit0 = 1
    data1 = [0, 1676, 2065, 2454, 2843, 3232, 3621, 4009, 4398, 4787, 5176, 5565, 5954, 6342, 6731, 7120, 7509, 7898, 8287, 8675, 9064, 9453, 9842, 10231, 10620, 11008, 11397, 11786, 12175, 12564, 12953, 13341, 13730, 14119, 14508, 14897, 15286,
             15674, 16063, 16452, 16841, 17230, 17619, 18007, 18396, 18785, 19174, 19563, 19952, 20340, 20729, 21118, 21507, 21896, 22285, 22673, 23062, 23451, 23840, 24229, 24618, 25006, 25395, 25784, 26173, 26562, 26951, 27339, 27728, 28117, 28506]
    hit1 = 8.4 / 0.2
    CD = 145
    倍率 = 1.1  # 9级以上

    MP = [881, 5288]
    无色消耗 = 5


class 技能14(主动技能):
    名称 = '等离子放射器'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40
    data0 = [0, 1793, 1975, 2156, 2338, 2520, 2702, 2884, 3066, 3248, 3430, 3612, 3794, 3976, 4157, 4339, 4521, 4703, 4885, 5067, 5249, 5431, 5613, 5795, 5977, 6159, 6340, 6522, 6704, 6886, 7068, 7250, 7432, 7614, 7796, 7978, 8160,
             8341, 8523, 8705, 8887, 9069, 9251, 9433, 9615, 9797, 9979, 10161, 10342, 10524, 10706, 10888, 11070, 11252, 11434, 11616, 11798, 11980, 12162, 12344, 12525, 12707, 12889, 13071, 13253, 13435, 13617, 13799, 13981, 14163, 14345]
    hit0 = 12
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5

    MP = [400, 1120]
    无色消耗 = 1

    是否有护石 = 1

    def 装备护石(self, x):
        self.倍率 *= 1.25
        self.CD *= 0.88


class 技能15(主动技能):
    名称 = 'FM92SW刺弹炮'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [0, 7567, 8335, 9103, 9870, 10638, 11406, 12174, 12941, 13709, 14477, 15244, 16012, 16780, 17548, 18315, 19083, 19851, 20619, 21386, 22154, 22922, 23690, 24457, 25225, 25993, 26760, 27528, 28296, 29064, 29831, 30599, 31367, 32135, 32902, 33670,
             34438, 35205, 35973, 36741, 37509, 38276, 39044, 39812, 40580, 41347, 42115, 42883, 43651, 44418, 45186, 45954, 46721, 47489, 48257, 49025, 49792, 50560, 51328, 52096, 52863, 53631, 54399, 55167, 55934, 56702, 57470, 58237, 59005, 59773, 60541]
    hit0 = 4

    data1 = [0, 886, 976, 1066, 1156, 1245, 1335, 1425, 1515, 1605, 1695, 1785, 1875, 1965, 2055, 2145, 2235, 2324, 2414, 2504, 2594, 2684, 2774, 2864, 2954, 3044, 3134, 3224, 3313, 3403, 3493, 3583, 3673, 3763, 3853,
             3943, 4033, 4123, 4213, 4303, 4392, 4482, 4572, 4662, 4752, 4842, 4932, 5022, 5112, 5202, 5292, 5382, 5471, 5561, 5651, 5741, 5831, 5921, 6011, 6101, 6191, 6281, 6371, 6461, 6550, 6640, 6730, 6820, 6910, 7000, 7090]
    hit1 = 12

    # 灼烧攻击力,在点TP之后删除
    data2 = [0, 28, 31, 34, 36, 39, 42, 45, 48, 51, 54, 56, 59, 62, 65, 67, 71, 74, 76, 79, 82, 85, 87, 90, 94, 96, 99, 102, 105, 107, 110, 113, 116, 119, 122, 125, 127, 130,
             133, 135, 138, 142, 145, 147, 150, 153, 155, 158, 161, 165, 167, 170, 173, 175, 178, 181, 184, 187, 190, 193, 195, 198, 201, 204, 206, 210, 213, 215, 218, 221, 224]
    # 灼烧8次
    hit2 = 0

    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5

    MP = [800, 1680]
    无色消耗 = 2

    是否有护石 = 1

    def 装备护石(self, x):
        self.倍率 *= 1.305


class 技能16(被动技能):
    名称 = '重火器改良'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.02 * self.等级, 5)


class 技能17(主动技能):
    名称 = '地脉震荡器'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [0, 2495, 2748, 3001, 3254, 3507, 3760, 4013, 4267, 4520, 4773, 5026, 5279, 5532, 5785, 6038, 6292, 6545, 6798, 7051, 7304, 7557, 7810, 8063, 8317, 8570, 8823, 9076, 9329, 9582, 9835, 10089, 10342, 10595, 10848, 11101, 11354,
             11607, 11860, 12114, 12367, 12620, 12873, 13126, 13379, 13632, 13885, 14139, 14392, 14645, 14898, 15151, 15404, 15657, 15911, 16164, 16417, 16670, 16923, 17176, 17429, 17682, 17936, 18189, 18442, 18695, 18948, 19201, 19454, 19707, 19961]
    hit0 = 1

    data1 = [0, 8732, 9618, 10504, 11390, 12276, 13162, 14048, 14934, 15820, 16706, 17592, 18478, 19364, 20250, 21136, 22022, 22908, 23794, 24680, 25566, 26452, 27338, 28223, 29109, 29995, 30881, 31767, 32653, 33539, 34425, 35311, 36197, 37083, 37969,
             38855, 39741, 40627, 41513, 42399, 43285, 44171, 45057, 45943, 46829, 47714, 48600, 49486, 50372, 51258, 52144, 53030, 53916, 54802, 55688, 56574, 57460, 58346, 59232, 60118, 61004, 61890, 62776, 63662, 64548, 65434, 66320, 67205, 68091, 68977, 69863]
    hit1 = 1

    data2 = [0, 1871, 2061, 2251, 2440, 2630, 2820, 3010, 3200, 3390, 3579, 3769, 3959, 4149, 4339, 4529, 4719, 4908, 5098, 5288, 5478, 5668, 5858, 6047, 6237, 6427, 6617, 6807, 6997, 7187, 7376, 7566, 7756, 7946, 8136, 8326, 8516,
             8705, 8895, 9085, 9275, 9465, 9655, 9844, 10034, 10224, 10414, 10604, 10794, 10984, 11173, 11363, 11553, 11743, 11933, 12123, 12312, 12502, 12692, 12882, 13072, 13262, 13452, 13641, 13831, 14021, 14211, 14401, 14591, 14780, 14970]
    hit2 = 1

    data3 = [0, 4366, 4809, 5252, 5695, 6138, 6581, 7024, 7467, 7910, 8353, 8796, 9239, 9682, 10125, 10568, 11011, 11454, 11897, 12340, 12783, 13226, 13669, 14111, 14554, 14997, 15440, 15883, 16326, 16769, 17212, 17655, 18098, 18541, 18984, 19427,
             19870, 20313, 20756, 21199, 21642, 22085, 22528, 22971, 23414, 23857, 24300, 24743, 25186, 25629, 26072, 26515, 26958, 27401, 27844, 28287, 28730, 29173, 29616, 30059, 30502, 30945, 31388, 31831, 32274, 32717, 33160, 33602, 34045, 34488, 34931]
    hit3 = 6

    data4 = [0, 23080, 25421, 27762, 30104, 32445, 34787, 37128, 39470, 41811, 44153, 46494, 48835, 51177, 53518, 55860, 58201, 60543, 62884, 65226, 67567, 69909, 72250, 74591, 76933, 79274, 81616, 83957, 86299, 88640, 90982, 93323, 95665, 98006, 100347, 102689, 105030,
             107372, 109713, 112055, 114396, 116738, 119079, 121420, 123762, 126103, 128445, 130786, 133128, 135469, 137811, 140152, 142494, 144835, 147176, 149518, 151859, 154201, 156542, 158884, 161225, 163567, 165908, 168250, 170591, 172932, 175274, 177615, 179957, 182298, 184640]
    hit4 = 1

    CD = 40.0

    MP = [580, 4500]
    无色消耗 = 3

    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.3324


class 技能18(主动技能):
    名称 = 'MSC7'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40
    data0 = [0, 6295, 6934, 7572, 8211, 8850, 9488, 10127, 10766, 11404, 12043, 12682, 13320, 13959, 14597, 15236, 15875, 16513, 17152, 17791, 18429, 19068, 19707, 20345, 20984, 21623, 22261, 22900, 23539, 24177, 24816, 25455, 26093, 26732, 27371, 28009,
             28648, 29287, 29925, 30564, 31203, 31841, 32480, 33119, 33757, 34396, 35035, 35673, 36312, 36951, 37589, 38228, 38867, 39505, 40144, 40783, 41421, 42060, 42699, 43337, 43976, 44615, 45253, 45892, 46531, 47169, 47808, 48447, 49085, 49724, 50363]
    hit0 = 1

    data1 = [0, 56658, 62406, 68154, 73902, 79650, 85398, 91146, 96894, 102642, 108390, 114138, 119885, 125633, 131381, 137129, 142877, 148625, 154373, 160121, 165869, 171617, 177365, 183113, 188861, 194609, 200357, 206105, 211853, 217601, 223349, 229097, 234845, 240593, 246341, 252089,
             257836, 263584, 269332, 275080, 280828, 286576, 292324, 298072, 303820, 309568, 315316, 321064, 326812, 332560, 338308, 344056, 349804, 355552, 361300, 367048, 372796, 378544, 384292, 390040, 395787, 401535, 407283, 413031, 418779, 424527, 430275, 436023, 441771, 447519, 453267]
    hit1 = 1

    CD = 45.0

    MP = [580, 4500]
    无色消耗 = 5

    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.35


class 技能19(主动技能):
    名称 = '毁灭射线'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40
    data0 = [0, 7025, 8654, 10283, 11912, 13541, 15170, 16799, 18428, 20057, 21686, 23315, 24944, 26573, 28202, 29831, 31460, 33090, 34719, 36348, 37977, 39606, 41235, 42864, 44493, 46122, 47751, 49380, 51009, 52638, 54267, 55896, 57525, 59154, 60783, 62412,
             64041, 65670, 67299, 68929, 70558, 72187, 73816, 75445, 77074, 78703, 80332, 81961, 83590, 85219, 86848, 88477, 90106, 91735, 93364, 94993, 96622, 98251, 99880, 101509, 103139, 104768, 106397, 108026, 109655, 111284, 112913, 114542, 116171, 117800, 119429]
    data1 = [0, 105378, 129814, 154250, 178686, 203121, 227557, 251993, 276428, 300864, 325300, 349735, 374171, 398607, 423043, 447478, 471914, 496350, 520785, 545221, 569657, 594092, 618528, 642964, 667399, 691835, 716271, 740707, 765142, 789578, 814014, 838449, 862885, 887321, 911756, 936192, 960628,
             985064, 1009499, 1033935, 1058371, 1082806, 1107242, 1131678, 1156113, 1180549, 1204985, 1229421, 1253856, 1278292, 1302728, 1327163, 1351599, 1376035, 1400470, 1424906, 1449342, 1473778, 1498213, 1522649, 1547085, 1571520, 1595956, 1620392, 1644827, 1669263, 1693699, 1718135, 1742570, 1767006, 1791442]

    hit0 = 10
    hit1 = 1

    CD = 180.0

    MP = [2500, 8000]
    无色消耗 = 5


class 技能20(被动技能):
    名称 = '连锁卫星'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能21(主动技能):
    名称 = 'MLDRS95发射器'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40
    CD = 60.0
    data0 = [0, 2091, 2303, 2515, 2727, 2939, 3151, 3364, 3576, 3788, 4000, 4212, 4424, 4636, 4849, 5061, 5273, 5485, 5697, 5909, 6122, 6334, 6546, 6758, 6970, 7182, 7394, 7607, 7819, 8031, 8243, 8455, 8667, 8879, 9092, 9304, 9516, 9728,
             9940, 10152, 10365, 10577, 10789, 11001, 11213, 11425, 11637, 11850, 12062, 12274, 12486, 12698, 12910, 13122, 13335, 13547, 13759, 13971, 14183, 14395, 14608, 14820, 15032, 15244, 15456, 15668, 15880, 16093, 16305, 16517, 16729]
    data1 = [0, 94103, 103650, 113196, 122743, 132290, 141837, 151383, 160930, 170477, 180023, 189570, 199117, 208664, 218210, 227757, 237304, 246851, 256397, 265944, 275491, 285037, 294584, 304131, 313678, 323224, 332771, 342318, 351865, 361411, 370958, 380505, 390051, 399598, 409145,
             418692, 428238, 437785, 447332, 456879, 466425, 475972, 485519, 495065, 504612, 514159, 523706, 533252, 542799, 552346, 561893, 571439, 580986, 590533, 600079, 609626, 619173, 628720, 638266, 647813, 657360, 666907, 676453, 686000, 695547, 705093, 714640, 724187, 733734, 743280, 752827]

    hit0 = 15
    hit1 = 1

    MP = [773, 6000]
    无色消耗 = 7


class 技能22(主动技能):
    名称 = '裂核轨道炮'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40
    data0 = [0, 9662, 11902, 14143, 16383, 18624, 20864, 23105, 25345, 27586, 29826, 32067, 34307, 36548, 38787, 41029, 43268, 45509, 47749, 49990, 52230, 54471, 56712, 58952, 61193, 63433, 65674, 67914, 70155, 72395, 74636, 76876, 79117, 81357, 83598, 85838, 88079,
             90319, 92560, 94800, 97041, 99281, 101522, 103762, 106003, 108244, 110484, 112725, 114965, 117206, 119445, 121687, 123926, 126167, 128407, 130648, 132888, 135129, 137369, 139610, 141850, 144091, 146331, 148572, 150812, 153053, 155293, 157534, 159775, 162015, 164256]
    data1 = [0, 193242, 238051, 282862, 327671, 372482, 417291, 462100, 506911, 551720, 596531, 641340, 686151, 730960, 775770, 820580, 865389, 910199, 955009, 999819, 1044629, 1089439, 1134248, 1179058, 1223868, 1268678, 1313488, 1358297, 1403108, 1447917, 1492728, 1537537, 1582346, 1627157, 1671966, 1716777,
             1761586, 1806396, 1851206, 1896016, 1940826, 1985635, 2030445, 2075255, 2120065, 2164875, 2209685, 2254494, 2299304, 2344114, 2388924, 2433734, 2478543, 2523354, 2568163, 2612974, 2657783, 2702592, 2747403, 2792212, 2837023, 2881832, 2926642, 2971452, 3016262, 3061072, 3105881, 3150691, 3195501, 3240311, 3285121]
    data2 = [0, 24155, 29756, 35357, 40959, 46559, 52161, 57762, 63364, 68965, 74565, 80167, 85768, 91370, 96971, 102571, 108173, 113774, 119376, 124977, 130578, 136179, 141780, 147382, 152983, 158584, 164185, 169787, 175388, 180989, 186591, 192191, 197793, 203394, 208996, 214597,
             220197, 225799, 231400, 237002, 242603, 248203, 253805, 259406, 265008, 270609, 276210, 281811, 287413, 293014, 298615, 304216, 309817, 315419, 321020, 326622, 332222, 337823, 343425, 349026, 354628, 360228, 365829, 371431, 377032, 382634, 388234, 393836, 399437, 405038, 410640]

    hit0 = 5
    hit1 = 1
    hit2 = 10

    CD = 290.0

    MP = [4027, 8054]
    无色消耗 = 15


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'launcher_male'
        self.名称 = '重霄·枪炮师'
        self.角色 = '神枪手(男)'

        self.职业 = '枪炮师'
        # 用来筛CP武器的
        self.转职 = '枪炮师(男)'
        self.武器选项 = ['手炮']
        self.输出类型选项 = ['物理百分比']
        self.防具精通属性 = ['力量']
        self.类型 = '物理百分比'
        self.武器类型 = '手炮'
        self.防具类型 = '重甲'
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
        self.buff = 1.957

        super().__init__()

    def 职业特殊计算(self):
        k = self.get_skill_by_name('重火器精通').MP消耗量比率()
        for i in self.技能栏:
            if i.是否主动 == 1:
                i.MP = [int(i.MP[0] * k), int(i.MP[1] * k)]
