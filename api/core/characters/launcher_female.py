
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
    名称 = 'M3喷火器'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [0, 218, 240, 263, 284, 306, 329, 350, 373, 395, 416, 439, 461, 483, 506, 528, 550, 572, 595, 616, 638, 661, 682, 705, 727, 748, 771, 794, 816, 838, 860, 882, 904, 927, 948, 970, 993, 1014,
             1037, 1059, 1080, 1104, 1126, 1148, 1170, 1192, 1214, 1236, 1259, 1280, 1302, 1325, 1346, 1369, 1392, 1413, 1436, 1458, 1480, 1502, 1524, 1546, 1568, 1591, 1612, 1634, 1657, 1678, 1702, 1724, 1745]
    hit0 = 14
    CD = 7.0
    TP成长 = 0.1
    TP上限 = 7

    MP = [45, 392]
    无色消耗 = 0

    def 等效百分比(self, **argv):
        self.hit0 = 14 + (1 if self.TP等级 >= 5 else 0)  # 5级以上TP能多打一段
        return super().等效百分比(**argv)


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
    data0 = [0, 1179, 1298, 1419, 1538, 1656, 1777, 1896, 2017, 2136, 2255, 2375, 2495, 2615, 2735, 2853, 2973, 3093, 3213, 3333, 3451, 3572, 3691, 3812, 3931, 4050, 4170, 4289, 4410, 4529, 4649, 4768, 4888, 5008, 5127,
             5247, 5366, 5486, 5606, 5726, 5845, 5965, 6084, 6205, 6324, 6443, 6563, 6682, 6802, 6922, 7042, 7162, 7280, 7400, 7520, 7640, 7760, 7879, 7998, 8119, 8238, 8359, 8477, 8596, 8717, 8836, 8957, 9075, 9195, 9315, 9434]
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
    data0 = [0, 180, 197, 214, 234, 251, 270, 287, 305, 325, 342, 360, 378, 397, 415, 434, 451, 469, 489, 506, 524, 542, 560, 579, 597, 615, 634, 653, 669, 687, 706, 724, 743, 761, 778, 798, 816,
             833, 851, 870, 888, 906, 925, 942, 962, 980, 996, 1015, 1033, 1052, 1070, 1089, 1106, 1126, 1143, 1160, 1179, 1198, 1216, 1234, 1252, 1270, 1289, 1307, 1324, 1342, 1362, 1379, 1398, 1415, 1433]
    data1 = [0, 935, 1030, 1126, 1221, 1317, 1410, 1506, 1601, 1696, 1791, 1887, 1980, 2075, 2170, 2265, 2361, 2455, 2551, 2645, 2741, 2836, 2931, 3026, 3120, 3216, 3310, 3405, 3500, 3595, 3690, 3786, 3879, 3975, 4071,
             4165, 4261, 4355, 4451, 4546, 4641, 4735, 4830, 4925, 5021, 5115, 5209, 5304, 5400, 5496, 5590, 5686, 5781, 5876, 5971, 6066, 6160, 6255, 6350, 6445, 6540, 6634, 6730, 6825, 6921, 7015, 7111, 7206, 7300, 7395, 7489]
    hit1 = 3
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 7

    MP = [40, 392]
    无色消耗 = 0


class 技能4(被动技能):
    名称 = 'APG63'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    学习间隔 = 3

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.14 + 0.01 * self.等级, 5)


class 技能5(主动技能):
    名称 = '激光炮'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [0, 3020, 3327, 3634, 3941, 4246, 4553, 4860, 5166, 5474, 5780, 6086, 6393, 6698, 7005, 7312, 7619, 7926, 8231, 8538, 8845, 9151, 9457, 9764, 10071, 10378, 10683, 10990, 11296, 11604, 11911, 12216, 12523, 12829, 13136, 13442, 13749,
             14056, 14363, 14668, 14975, 15281, 15589, 15896, 16201, 16508, 16814, 17121, 17427, 17734, 18041, 18346, 18653, 18960, 19266, 19574, 19879, 20186, 20493, 20799, 21106, 21411, 21719, 22026, 22331, 22638, 22945, 23251, 23558, 23864, 24171]
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
            return round(1.25+0.05 * self.等级, 5)


class 技能7(主动技能):
    名称 = '聚焦喷火器'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [0, 250, 277, 302, 327, 352, 379, 404, 429, 454, 481, 506, 531, 557, 583, 608, 633, 659, 685, 710, 735, 761, 786, 812, 837, 863, 888, 914, 939, 965, 990, 1016, 1041, 1067, 1092, 1118, 1144, 1169,
             1194, 1220, 1246, 1271, 1296, 1322, 1348, 1373, 1398, 1424, 1450, 1475, 1500, 1526, 1552, 1577, 1602, 1627, 1654, 1679, 1704, 1728, 1754, 1780, 1805, 1830, 1856, 1882, 1907, 1933, 1958, 1984, 2009]
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
    data0 = [0, 1027, 1133, 1236, 1340, 1444, 1550, 1654, 1759, 1862, 1966, 2070, 2176, 2280, 2385, 2488, 2592, 2696, 2801, 2906, 3011, 3114, 3218, 3322, 3427, 3532, 3637, 3741, 3844, 3948, 4053, 4158, 4263, 4367, 4470,
             4574, 4679, 4783, 4889, 4993, 5096, 5200, 5305, 5409, 5515, 5619, 5722, 5826, 5931, 6035, 6141, 6245, 6347, 6452, 6556, 6661, 6765, 6871, 6973, 7078, 7182, 7287, 7391, 7497, 7599, 7704, 7808, 7913, 8017, 8122, 8225]
    hit0 = 8
    CD = 15.0
    TP成长 = 0.20
    TP上限 = 1

    MP = [50, 630]
    无色消耗 = 0

    是否有护石 = 1

    def 装备护石(self):
        self.基础施放次数 = 4
        self.hit0 = 2
        self.倍率 *= 1.27
        self.CD = 4


class 技能9(主动技能):
    名称 = 'FM92mk2榴弹'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [0, 1335, 1471, 1606, 1742, 1878, 2012, 2149, 2284, 2419, 2555, 2690, 2826, 2961, 3097, 3232, 3369, 3503, 3640, 3775, 3909, 4046, 4182, 4316, 4453, 4588, 4722, 4859, 4994, 5131, 5265, 5401, 5537, 5672, 5807, 5944,
             6078, 6213, 6350, 6485, 6620, 6756, 6892, 7027, 7163, 7298, 7434, 7569, 7705, 7841, 7976, 8111, 8248, 8382, 8517, 8654, 8788, 8925, 9060, 9196, 9331, 9467, 9602, 9738, 9873, 10008, 10144, 10279, 10416, 10552, 10686]
    hit0 = 8
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

    data0 = [0, 860, 947, 1035, 1122, 1210, 1295, 1383, 1471, 1558, 1646, 1733, 1821, 1909, 1995, 2083, 2169, 2257, 2344, 2431, 2519, 2606, 2694, 2781, 2869, 2954, 3042, 3129, 3217, 3305, 3392, 3480, 3566, 3654, 3742,
             3828, 3916, 4003, 4090, 4177, 4265, 4353, 4440, 4528, 4615, 4701, 4788, 4876, 4964, 5051, 5139, 5225, 5313, 5401, 5488, 5574, 5662, 5749, 5836, 5924, 6012, 6099, 6187, 6273, 6361, 6447, 6535, 6622, 6710, 6798, 6884]
    hit0 = 1

    data1 = [0, 9896, 10901, 11905, 12909, 13914, 14918, 15920, 16925, 17930, 18933, 19938, 20943, 21945, 22950, 23954, 24958, 25963, 26967, 27970, 28974, 29979, 30983, 31987, 32992, 33994, 34999, 36004, 37007, 38012, 39017, 40019, 41024, 42027, 43032,
             44037, 45041, 46043, 47048, 48052, 49056, 50061, 51066, 52068, 53073, 54076, 55081, 56086, 57088, 58093, 59097, 60101, 61106, 62110, 63113, 64117, 65122, 66126, 67130, 68135, 69137, 70142, 71147, 72150, 73155, 74160, 75162, 76166, 77171, 78175, 79179]
    hit1 = 1

    感电data0 = [0, 10, 10, 10, 10, 10, 10, 11, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 19, 19, 20, 21, 21, 22, 23, 23, 24, 25, 25, 26, 27, 27, 28, 29, 30,
               30, 31, 32, 32, 33, 34, 34, 35, 36, 36, 37, 38, 39, 39, 40, 41, 41, 42, 43, 43, 44, 45, 45, 46, 47, 47, 48, 49, 50, 50, 51, 52, 52, 53, 54, 54]
    感电hit0 = 1

    CD = 18.0
    TP成长 = 0.10
    TP上限 = 5

    MP = [164, 1376]
    无色消耗 = 1

    是否有护石 = 1

    def 装备护石(self):
        self.hit0 = 0
        self.hit1 = 0.16 * 8 * 1.14
        self.感电hit0 *= 0.16 * 8 * 1.14
        self.CDR *= 0.9


class 技能11(主动技能):
    名称 = 'X1压缩量子炮'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [0, 22755, 25064, 27372, 29680, 31988, 34298, 36606, 38915, 41223, 43532, 45840, 48149, 50457, 52765, 55073, 57383, 59692, 62000, 64309, 66617, 68926, 71234, 73543, 75850, 78160, 80469, 82777, 85086, 87394, 89703, 92011, 94320, 96627, 98936, 101246, 103554,
             105863, 108171, 110480, 112788, 115097, 117405, 119713, 122021, 124331, 126640, 128948, 131257, 133565, 135874, 138182, 140491, 142798, 145107, 147417, 149725, 152034, 154342, 156651, 158959, 161268, 163575, 165884, 168192, 170502, 172811, 175119, 177428, 179736, 182045]
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5

    MP = [350, 2940]
    无色消耗 = 2

    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.18
        self.CDR *= 0.88


class 技能12(被动技能):
    名称 = '超温重火器'
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.04 + 0.02 * self.等级, 5)


class 技能13(主动技能):
    名称 = '远古粒子炮'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40
    data0 = [0, 5693, 7013, 8333, 9654, 10974, 12293, 13614, 14934, 16254, 17576, 18896, 20217, 21537, 22856, 24177, 25497, 26817, 28138, 29458, 30778, 32099, 33418, 34738, 36059, 37379, 38699, 40020, 41340, 42659, 43980, 45300, 46621, 47941, 49261, 50582,
             51902, 53221, 54543, 55863, 57184, 58504, 59824, 61145, 62465, 63784, 65105, 66425, 67745, 69066, 70386, 71706, 73026, 74346, 75666, 76987, 78307, 79627, 80948, 82268, 83587, 84908, 86228, 87549, 88869, 90189, 91510, 92831, 94151, 95471, 96791]
    hit0 = 0
    data1 = [0, 6619, 8154, 9690, 11226, 12761, 14296, 15831, 17367, 18902, 20437, 21971, 23506, 25041, 26577, 28112, 29648, 31183, 32718, 34253, 35788, 37324, 38859, 40395, 41929, 43464, 44999, 46534, 48069, 49605, 51140, 52675, 54210, 55746, 57282, 58817,
             60352, 61887, 63421, 64956, 66491, 68027, 69563, 71098, 72633, 74168, 75703, 77239, 78774, 80309, 81844, 83378, 84914, 86449, 87985, 89520, 91055, 92590, 94125, 95660, 97196, 98732, 100267, 101802, 103336, 104871, 106406, 107942, 109477, 111012, 112547]
    hit1 = 10
    CD = 145

    MP = [1000, 8400]
    无色消耗 = 5


class 技能14(主动技能):
    名称 = '等离子放射器'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40
    data0 = [0, 560, 617, 674, 731, 787, 845, 901, 957, 1015, 1071, 1129, 1186, 1242, 1299, 1357, 1413, 1470, 1527, 1584, 1641, 1698, 1754, 1812, 1869, 1924, 1982, 2038, 2096, 2152, 2209, 2266, 2324, 2379, 2437, 2494,
             2551, 2608, 2665, 2721, 2779, 2836, 2891, 2949, 3005, 3063, 3119, 3176, 3233, 3291, 3346, 3404, 3461, 3518, 3574, 3632, 3688, 3746, 3803, 3858, 3916, 3974, 4030, 4086, 4143, 4200, 4258, 4313, 4371, 4428, 4485]
    hit0 = 37
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5

    MP = [400, 1120]
    无色消耗 = 1

    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 0.85
        self.CDR *= 0.60


class 技能15(主动技能):
    名称 = 'FM92mk2SW榴弹'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [0, 4137, 4557, 4975, 5397, 5816, 6237, 6655, 7076, 7495, 7916, 8335, 8756, 9174, 9595, 10014, 10435, 10854, 11275, 11693, 12114, 12533, 12953, 13373, 13794, 14212, 14632, 15052, 15472, 15892, 16312, 16731, 17150, 17571, 17989, 18411,
             18830, 19250, 19669, 20090, 20508, 20929, 21349, 21768, 22188, 22608, 23027, 23448, 23868, 24287, 24707, 25127, 25548, 25967, 26387, 26807, 27225, 27646, 28065, 28486, 28905, 29326, 29744, 30164, 30584, 31004, 31424, 31844, 32263, 32683, 33103]
    hit0 = 8

    data1 = [0, 205, 226, 248, 268, 287, 309, 330, 351, 372, 392, 413, 435, 454, 476, 497, 517, 538, 559, 580, 602, 620, 642, 663, 684, 706, 726, 746, 768, 789, 809, 831, 850, 872, 892, 913, 935, 956,
             975, 997, 1018, 1040, 1060, 1079, 1101, 1122, 1143, 1164, 1185, 1205, 1227, 1246, 1268, 1289, 1309, 1330, 1351, 1372, 1394, 1414, 1433, 1455, 1476, 1498, 1518, 1538, 1560, 1581, 1601, 1623, 1643]
    hit1 = 24

    # 灼烧攻击力,在点TP之后删除
    data2 = [0, 28, 31, 34, 36, 39, 42, 45, 48, 51, 53, 56, 59, 62, 65, 68, 70, 73, 76, 79, 82, 85, 87, 90, 93, 96, 99, 102, 104, 107, 110, 113, 116, 119, 121, 124, 127, 130,
             133, 136, 138, 141, 144, 147, 150, 153, 155, 158, 161, 164, 167, 170, 172, 175, 178, 181, 184, 187, 189, 192, 195, 198, 201, 204, 206, 209, 212, 215, 218, 221, 223]
    # 灼烧8次
    hit2 = 0

    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5

    MP = [800, 1680]
    无色消耗 = 2

    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.27
        self.CDR *= 0.9


class 技能16(被动技能):
    名称 = '重武装改造'
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
    名称 = 'FSC7'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [0, 2528, 2785, 3041, 3297, 3554, 3810, 4066, 4323, 4580, 4835, 5093, 5348, 5606, 5863, 6118, 6375, 6632, 6887, 7144, 7402, 7656, 7914, 8171, 8427, 8684, 8941, 9197, 9453, 9711, 9966, 10223, 10480, 10736, 10992, 11249, 11505,
             11761, 12020, 12275, 12532, 12787, 13045, 13301, 13557, 13814, 14071, 14326, 14583, 14840, 15096, 15353, 15611, 15866, 16123, 16380, 16635, 16892, 17149, 17404, 17661, 17918, 18173, 18432, 18689, 18944, 19201, 19457, 19713, 19970, 20226]
    hit0 = 1

    data1 = [0, 4803, 5292, 5779, 6266, 6752, 7239, 7728, 8214, 8703, 9189, 9678, 10163, 10650, 11139, 11626, 12114, 12601, 13089, 13575, 14062, 14550, 15037, 15525, 16012, 16501, 16987, 17475, 17962, 18449, 18937, 19424, 19911, 20398, 20886, 21373,
             21862, 22349, 22836, 23322, 23809, 24298, 24784, 25273, 25759, 26248, 26733, 27221, 27709, 28196, 28684, 29171, 29659, 30145, 30633, 31120, 31607, 32095, 32583, 33071, 33557, 34045, 34532, 35020, 35507, 35994, 36481, 36968, 37456, 37944, 38432]
    hit1 = 10

    CD = 40.0

    MP = [777, 6021]
    无色消耗 = 3

    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 0.64
        self.CDR = 18
        self.基础施放次数 = 1.0
        # self.恢复 = 1.0


class 技能18(主动技能):
    名称 = 'PT15原始型压缩炮'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40
    data0 = [0, 63187, 69596, 76007, 82417, 88827, 95237, 101649, 108059, 114469, 120879, 127290, 133699, 140110, 146520, 152931, 159340, 165751, 172162, 178571, 184981, 191392, 197803, 204212, 210624, 217034, 223443, 229854, 236265, 242675, 249085, 255495, 261906, 268315, 274726, 281136,
             287547, 293956, 300367, 306777, 313187, 319598, 326009, 332419, 338829, 345239, 351650, 358059, 364470, 370880, 377291, 383700, 390111, 396522, 402931, 409341, 415752, 422164, 428573, 434984, 441394, 447803, 454214, 460625, 467035, 473445, 479855, 486266, 492675, 499086, 505496]
    CD = 45.0

    MP = [580, 4500]
    无色消耗 = 5

    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.35


class 技能19(主动技能):
    名称 = '火力全开'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40
    data0 = [0, 1172, 1444, 1715, 1988, 2259, 2532, 2804, 3076, 3347, 3620, 3892, 4164, 4436, 4707, 4979, 5252, 5524, 5795, 6067, 6339, 6611, 6884, 7156, 7427, 7700, 7972, 8243, 8515, 8787, 9059, 9332, 9603, 9875, 10147, 10419, 10690, 10963,
             11235, 11507, 11779, 12050, 12323, 12595, 12866, 13138, 13411, 13683, 13955, 14227, 14498, 14771, 15043, 15315, 15586, 15859, 16130, 16402, 16675, 16947, 17218, 17490, 17762, 18035, 18306, 18578, 18850, 19123, 19395, 19665, 19938]
    data1 = [0, 2930, 3610, 4288, 4969, 5648, 6329, 7009, 7689, 8367, 9050, 9729, 10409, 11090, 11767, 12448, 13130, 13809, 14488, 15168, 15848, 16528, 17210, 17889, 18567, 19249, 19929, 20607, 21287, 21968, 22647, 23329, 24008, 24688, 25368, 26047,
             26726, 27408, 28088, 28767, 29448, 30126, 30808, 31488, 32166, 32845, 33527, 34207, 34886, 35567, 36246, 36927, 37608, 38287, 38965, 39647, 40326, 41006, 41687, 42367, 43046, 43726, 44406, 45087, 45766, 46446, 47125, 47807, 48487, 49164, 49845]
    data2 = [0, 36438, 44888, 53337, 61787, 70237, 78686, 87135, 95586, 104035, 112484, 120935, 129384, 137834, 146283, 154733, 163183, 171632, 180081, 188532, 196980, 205429, 213879, 222329, 230778, 239228, 247677, 256128, 264577, 273026, 281476, 289926, 298375, 306825, 315274, 323724,
             332174, 340623, 349074, 357523, 365972, 374422, 382872, 391321, 399771, 408220, 416670, 425120, 433569, 442020, 450468, 458917, 467367, 475816, 484266, 492716, 501165, 509614, 518065, 526514, 534963, 543413, 551863, 560313, 568762, 577212, 585662, 594111, 602560, 611011, 619460]

    hit0 = 50
    hit1 = 20
    hit2 = 1
    CD = 180.0

    MP = [2500, 8000]
    无色消耗 = 5


class 技能20(被动技能):
    名称 = 'Pandora_01'
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
    名称 = 'UHT-03爆炎喷火器'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40
    CD = 60.0
    data0 = [0, 4697, 5176, 5651, 6128, 6606, 7082, 7557, 8033, 8511, 8988, 9465, 9941, 10418, 10895, 11372, 11849, 12324, 12801, 13278, 13756, 14230, 14709, 15185, 15660, 16138, 16616, 17091, 17567, 18045, 18520, 18998, 19475, 19952, 20428, 20905,
             21382, 21857, 22333, 22813, 23287, 23766, 24241, 24718, 25194, 25672, 26149, 26625, 27101, 27579, 28054, 28530, 29008, 29484, 29962, 30439, 30914, 31391, 31867, 32346, 32821, 33297, 33776, 34252, 34728, 35206, 35681, 36159, 36634, 37114, 37588]
    hit0 = 24

    MP = [773, 6000]
    无色消耗 = 7


class 技能22(主动技能):
    名称 = '制胜·最终兵器'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40
    data0 = [0, 15927, 19622, 23317, 27009, 30704, 34398, 38091, 41785, 45478, 49172, 52867, 56559, 60254, 63949, 67641, 71335, 75029, 78723, 82416, 86112, 89805, 93498, 97193, 100885, 104580, 108273, 111967, 115661, 119355, 123048, 126742, 130437, 134130, 137824, 141518, 145211,
             148905, 152600, 156293, 159987, 163680, 167373, 171067, 174761, 178456, 182150, 185844, 189537, 193230, 196924, 200618, 204313, 208006, 211700, 215393, 219088, 222781, 226475, 230169, 233862, 237556, 241251, 244943, 248638, 252333, 256024, 259719, 263413, 267107, 270801]
    data1 = [0, 3982, 4906, 5830, 6752, 7676, 8600, 9523, 10447, 11369, 12293, 13217, 14140, 15064, 15988, 16910, 17834, 18758, 19680, 20604, 21527, 22451, 23375, 24298, 25221, 26145, 27068, 27992, 28916, 29839, 30762, 31685, 32609, 33533, 34457, 35379,
             36303, 37226, 38150, 39074, 39997, 40920, 41843, 42767, 43691, 44615, 45537, 46461, 47384, 48308, 49232, 50154, 51078, 52002, 52925, 53849, 54771, 55695, 56619, 57542, 58466, 59390, 60312, 61236, 62160, 63083, 64006, 64929, 65853, 66777, 67700]
    data2 = [0, 9557, 11773, 13991, 16205, 18423, 20639, 22855, 25071, 27287, 29503, 31721, 33935, 36153, 38369, 40585, 42801, 45017, 47233, 49449, 51667, 53883, 56099, 58316, 60531, 62747, 64964, 67181, 69397, 71613, 73829, 76045, 78262, 80478, 82694, 84910, 87127,
             89343, 91560, 93776, 95992, 98208, 100424, 102640, 104857, 107074, 109290, 111506, 113722, 115938, 118154, 120370, 122588, 124804, 127020, 129236, 131452, 133668, 135886, 138102, 140318, 142534, 144750, 146966, 149183, 151399, 153614, 155832, 158048, 160264, 162481]
    data3 = [0, 7964, 9811, 11658, 13505, 15352, 17199, 19045, 20893, 22739, 24586, 26434, 28280, 30127, 31974, 33821, 35667, 37514, 39361, 41209, 43056, 44902, 46750, 48597, 50442, 52289, 54137, 55984, 57830, 59677, 61524, 63371, 65218, 67064, 68912, 70759, 72605,
             74453, 76300, 78146, 79993, 81840, 83687, 85534, 87380, 89228, 91075, 92923, 94769, 96615, 98462, 100308, 102156, 104003, 105849, 107697, 109544, 111390, 113237, 115085, 116931, 118778, 120626, 122472, 124319, 126166, 128013, 129860, 131706, 133553, 135401]

    hit0 = 5
    hit1 = 5
    hit2 = 10
    hit3 = 25

    CD = 290.0

    MP = [4028, 12889]
    无色消耗 = 15


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'launcher_female'
        self.名称 = '重霄·枪炮师'
        self.角色 = '神枪手(女)'

        self.职业 = '枪炮师'
        # 用来筛CP武器的
        self.转职 = '枪炮师(女)'
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
