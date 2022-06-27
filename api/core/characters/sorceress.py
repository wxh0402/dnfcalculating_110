

from core.baseClass.skill import 技能
from core.baseClass.character import Character
from core.baseClass.skill import 主动技能, 被动技能


class 技能0(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    关联技能 = ['念珠连射']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)


class 技能1(主动技能):
    名称 = '罪业加身'
    所在等级 = 10
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 252]
    data0 = [int(i*1.085*1.0) for i in [0, 2014, 2220, 2424, 2628, 2832, 3037, 3242, 3446, 3651, 3854, 4059, 4263, 4468, 4672, 4877, 5080, 5285, 5492, 5695, 5900, 6104, 6308, 6514, 6718, 6922, 7126, 7331, 7535, 7740, 7944, 8148, 8352, 8557, 8762, 8966,
                                  9171, 9374, 9579, 9784, 9989, 10194, 10398, 10602, 10807, 11012, 11215, 11420, 11623, 11829, 12034, 12237, 12442, 12646, 12851, 13055, 13260, 13463, 13668, 13872, 14077, 14282, 14487, 14691, 14895, 15101, 15304, 15509, 15714, 15917, 16123]]
    hit0 = 1
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 7


class 技能2(主动技能):
    名称 = '唤雷符'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 252]
    data0 = [int(i*1.085*1.206) for i in [0, 1721, 1895, 2070, 2245, 2420, 2594, 2769, 2944, 3118, 3293, 3468, 3641, 3816, 3992, 4166, 4340, 4516, 4689, 4865, 5039, 5212, 5389, 5563, 5738, 5911, 6087, 6262, 6437, 6610, 6786, 6961, 7134, 7309, 7484,
                                  7660, 7834, 8008, 8182, 8357, 8532, 8707, 8880, 9055, 9231, 9405, 9580, 9754, 9930, 10104, 10278, 10452, 10628, 10802, 10977, 11151, 11325, 11502, 11676, 11849, 12025, 12200, 12374, 12548, 12723, 12897, 13073, 13248, 13422, 13596, 13771]]
    hit0 = 1
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 7


class 技能3(主动技能):
    名称 = '念珠连射'
    备注 = '(TP为基础精通)'
    所在等级 = 15
    等级上限 = 1
    基础等级 = 1
    MP = [1, 1]
    # 计算得出的百分比
    data0 = [0,1.085*132.41]
    hit0 = 6
    CD = 0.0
    TP成长 = 0.10
    TP上限 = 5


class 技能4(主动技能):
    名称 = '木槵子经'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [30, 252]
    data0 = [int(i*1.085*1.119) for i in [0, 267, 295, 323, 350, 377, 404, 432, 459, 486, 513, 541, 567, 595, 621, 650, 677, 704, 731, 759, 786, 813, 840, 867, 895, 921, 949, 977, 1004, 1031, 1058, 1085, 1113, 1140, 1167, 1194, 1221, 1249, 1275, 1303, 1331, 1358, 1385, 1412, 1440, 1467, 1494, 1521, 1549, 1575, 1603, 1630, 1658, 1685, 1712, 1739, 1767, 1794, 1821, 1848, 1875, 1903, 1930, 1957, 1985, 2012, 2039, 2066, 2094, 2121, 2148]]
    hit0 = 6
    CD = 4.0
    TP成长 = 0.10
    TP上限 = 7


class 技能5(主动技能):
    名称 = '束灵符'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [40, 300]
    data0 = [int(i*1.085*1.211) for i in [0, 2352, 2590, 2829, 3067, 3306, 3545, 3783, 4022, 4261, 4499, 4738, 4976, 5215, 5454, 5692, 5931, 6169, 6408, 6647, 6885, 7124, 7363, 7601, 7840, 8078, 8317, 8556, 8794, 9033, 9272, 9510, 9749, 9987, 10226, 10465, 10703, 10942, 11180, 11419, 11658, 11896, 12135, 12374, 12612, 12851, 13089, 13328, 13567, 13805, 14044, 14283, 14521, 14760, 14998, 15237, 15476, 15714, 15953, 16191, 16430, 16669, 16907, 17146, 17385, 17623, 17862, 18100, 18339, 18578, 18816]]
    hit0 = 1
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 7


class 技能6(主动技能):
    名称 = '驱邪咒'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [35, 350]
    data0 = [int(i*1.085*1.209) for i in [0, 268, 296, 323, 350, 377, 405, 432, 459, 487, 514, 541, 568, 596, 623, 650, 678, 705, 732, 759, 787, 814, 841, 869, 896, 923, 950, 978, 1005, 1032, 1059, 1087, 1114, 1141, 1169, 1196, 1223, 1250, 1278, 1305, 1332, 1360, 1387, 1414, 1441, 1469, 1496, 1523, 1550, 1578, 1605, 1632, 1660, 1687, 1714, 1741, 1769, 1796, 1823, 1851, 1878, 1905, 1932, 1960, 1987, 2014, 2041, 2069, 2096, 2123, 2151]]
    hit0 = 20
    CD = 12.0
    TP上限 = 7
    TP倍率 = [1, 1.2377, 1.3499, 1.4626, 1.5748, 1.6875, 1.8002, 1.9124]

    def TP加成(self):
        TP倍率 = [1, 1.2377, 1.3499, 1.4626, 1.5748, 1.6875, 1.8002, 1.9124]
        return TP倍率[self.TP等级]


class 技能7(被动技能):
    名称 = '祈雨祭'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)


class 技能8(主动技能):
    名称 = '和合之玉'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [150, 420]
    data0 = [int(i*1.085*1.211) for i in [0, 3996, 4401, 4806, 5212, 5617, 6023, 6428, 6833, 7239, 7644, 8050, 8455, 8860, 9266, 9671, 10077, 10482, 10887, 11293, 11698, 12104, 12509, 12914, 13320, 13725, 14131, 14536, 14941, 15347, 15752, 16158, 16563, 16968, 17374, 17779, 18185, 18590, 18995, 19401, 19806, 20212, 20617, 21022, 21428, 21833, 22239, 22644, 23049, 23455, 23860, 24266, 24671, 25076, 25482, 25887, 26293, 26698, 27103, 27509, 27914, 28320, 28725, 29130, 29536, 29941, 30347, 30752, 31157, 31563, 31968]]
    hit0 = 1
    data1 = [int(i*1.085*1.211) for i in [0, 1712, 1886, 2060, 2233, 2407, 2581, 2755, 2928, 3102, 3276, 3450, 3623, 3797, 3971, 4145, 4318, 4492, 4666, 4839, 5013, 5187, 5361, 5534, 5708, 5882, 6056, 6229, 6403, 6577, 6751, 6924, 7098, 7272, 7446, 7619, 7793, 7967, 8141, 8314, 8488, 8662, 8836, 9009, 9183, 9357, 9531, 9704, 9878, 10052, 10225, 10399, 10573, 10747, 10920, 11094, 11268, 11442, 11615, 11789, 11963, 12137, 12310, 12484, 12658, 12832, 13005, 13179, 13353, 13527, 13700]]
    hit1 = 1
    CD = 15.0
    TP成长 = 0.1
    TP上限 = 7


class 技能9(被动技能):
    名称 = '神术强化'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.05 + 0.015 * self.等级, 5)
        else:
            return round(1.00 + 0.02 * self.等级, 5)


class 技能10(主动技能):
    名称 = '聚魂吸星符'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.085*1.21) for i in [0, 349, 385, 420, 456, 491, 527, 563, 598, 634, 669, 705, 740, 776, 811, 847, 882, 918, 953, 989, 1024, 1060, 1095, 1131, 1166, 1202, 1237, 1273, 1308, 1344, 1379, 1415, 1450, 1486, 1521, 1557, 1592, 1628, 1663, 1699, 1734, 1770, 1805, 1841, 1876, 1912, 1947, 1983, 2018, 2054, 2089, 2125, 2160, 2196, 2231, 2267, 2302, 2338, 2373, 2409, 2444, 2480, 2515, 2551, 2586, 2622, 2657, 2693, 2728, 2764, 2799]]
    hit0 = 19
    CD = 15.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    MP = [200, 850]
    无色消耗 = 1

    def 装备护石(self):
        self.hit0 = 22
        self.倍率 *= 1.19
        self.CDR *= 0.95


class 技能11(主动技能):
    名称 = '龙魂之怒'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.051*1.085*1.211) for i in [0, 8953, 9862, 10770, 11679, 12587, 13495, 14404, 15312, 16220, 17129, 18037, 18946, 19854, 20762, 21671, 22579, 23487, 24396, 25304, 26212, 27121, 28029, 28938, 29846, 30754, 31663, 32571, 33479, 34388, 35296, 36205, 37113, 38021, 38930, 39838, 40746, 41655, 42563, 43472, 44380, 45288, 46197, 47105, 48013, 48922, 49830, 50738, 51647, 52555, 53464, 54372, 55280, 56189, 57097, 58005, 58914, 59822, 60731, 61639, 62547, 63456, 64364, 65272, 66181, 67089, 67998, 68906, 69814, 70723, 71631]]
    hit0 = 1
    CD = 20.0
    TP成长 = 0.1
    TP上限 = 5

    MP = [250, 1260]
    无色消耗 = 1


class 技能12(主动技能):
    名称 = '百八念珠'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    #单体和范围双形态
    data0 = [int(i*1.05*1.085*1.211) for i in [0, 653, 720, 786, 852, 919, 984, 1051, 1117, 1184, 1250, 1316, 1383, 1449, 1516, 1582, 1648, 1713, 1780, 1846, 1913, 1979, 2046, 2111, 2179, 2244, 2311, 2377, 2443, 2510, 2576, 2643, 2709, 2775,
                                  2842, 2908, 2974, 3040, 3107, 3173, 3239, 3306, 3372, 3439, 3505, 3571, 3636, 3703, 3769, 3836, 3902, 3969, 4034, 4102, 4167, 4234, 4299, 4366, 4432, 4499, 4565, 4632, 4698, 4765, 4830, 4898, 4963, 5030, 5096, 5162, 5229]]
    hit0 = 20
    power0 = 1
    data1 = [int(i*1.05) for i in [0, 1069, 1178, 1288, 1395, 1505, 1611, 1721, 1830, 1938, 2047, 2154, 2264, 2373, 2482, 2590, 2698, 2807, 2915, 3025, 3132, 3242, 3349, 3458, 3567, 3676, 3784, 3892, 4000, 4110, 4220, 4327, 4434, 4544, 4652, 4762, 4871, 4978, 5086, 5195, 5305, 5413, 5522, 5629, 5737, 5847, 5956, 6064, 6173, 6281, 6390, 6499, 6607, 6715, 6825, 6932, 7042, 7149, 7259, 7367, 7475, 7584, 7692, 7801, 7910, 8019, 8127, 8234, 8344, 8454, 8562]]
    hit1 = 0
    power1 = 1
    CD = 25.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    MP = [250, 1260]
    无色消耗 = 1

    形态 = ["单体", "范围"]

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "单体":
            self.hit0 = 20
            self.hit1 = 0
        if 形态 == "范围":
            self.hit0 = 0
            self.hit1 = 10

    # cp下的提升率为1.14；这里还没改
    def 装备护石(self):
        # self.倍率 *= 1.27
        self.power0 *= 1.27
        self.power1 *= 1.14
        self.CDR *= 0.83


class 技能13(主动技能):
    名称 = '不动珠箔阵'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    data0 = [int(i*1.053*1.085*1.21) for i in [0, 446, 491, 537, 582, 627, 673, 718, 763, 808, 854, 899, 944, 990, 1035, 1080, 1126, 1171, 1216, 1262, 1307, 1352, 1397, 1443, 1488, 1533, 1579, 1624, 1669, 1715, 1760, 1805, 1850, 1896, 1941, 1986, 2032, 2077, 2122, 2168, 2213, 2258, 2303, 2349, 2394, 2439, 2485, 2530, 2575, 2621, 2666, 2711, 2756, 2802, 2847, 2892, 2938, 2983, 3028, 3074, 3119, 3164, 3210, 3255, 3300, 3345, 3391, 3436, 3481, 3527, 3572]]
    hit0 = 24
    data1 = [int(i*1.053*1.085*1.21) for i in [0, 7144, 7869, 8594, 9319, 10044, 10769, 11493, 12218, 12943, 13668, 14393, 15118, 15842, 16567, 17292, 18017, 18742, 19467, 20192, 20916, 21641, 22366, 23091, 23816, 24541, 25265, 25990, 26715, 27440, 28165, 28890, 29614, 30339, 31064, 31789, 32514, 33239, 33964, 34688, 35413, 36138, 36863, 37588, 38313, 39037, 39762, 40487, 41212, 41937, 42662, 43386, 44111, 44836, 45561, 46286, 47011, 47736, 48460, 49185, 49910, 50635, 51360, 52085, 52809, 53534, 54259, 54984, 55709, 56434, 57158]]
    hit1 = 1
    CD = 45.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    MP = [250, 2500]
    无色消耗 = 2


    def 装备护石(self):
        self.倍率 *= 1.17
        self.CDR *= 0.90


class 技能14(主动技能):
    名称 = '神龙如意珠'
    备注 = '(1次)'
    是否主动 = 0
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    data0 = [int(i*1.0) for i in [0, 526, 611, 694, 779, 862, 946, 1030, 1113, 1198, 1282, 1366, 1450, 1534, 1618, 1702, 1786, 1870, 1954,
                                  2038, 2121, 2207, 2290, 2374, 2458, 2542, 2626, 2710, 2794, 2878, 2962, 3046, 3130, 3213, 3298, 3382, 3466, 3550, 3634, 3718, 3802]]
    CD = 0.5
    关联技能 = ['所有']

    def 等效CD(self, **argv):
        return 0.5

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.115 + 0.015 * self.等级, 5)


class 技能15(主动技能):
    名称 = '神谕：神龙雷雨祭'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.085*1.21) for i in [0, 2167, 2670, 3173, 3676, 4178, 4681, 5184, 5686, 6189, 6692, 7194, 7697, 8200, 8703, 9205, 9708, 10211, 10713, 11216, 11719, 12222, 12724, 13227, 13730, 14232, 14735, 15238, 15740, 16243, 16746, 17249, 17751, 18254, 18757, 19259, 19762, 20265, 20768, 21270, 21773]]
    hit0 = 16
    data1 = [int(i*1.085*1.21) for i in [0, 14865, 18312, 21760, 25207, 28654, 32101, 35548, 38995, 42442, 45889, 49337, 52784, 56231, 59678, 63125, 66572, 70019, 73466, 76914, 80361, 83808, 87255, 90702, 94149, 97596, 101044, 104491, 107938, 111385, 114832, 118279, 121726, 125173, 128621, 132068, 135515, 138962, 142409, 145856, 149303]]
    hit1 = 1
    CD = 140.0

    MP = [900, 7560]
    无色消耗 = 5


class 技能16(主动技能):
    名称 = '因果业火符'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.051*1.085*1.211) for i in [0, 1426, 1571, 1716, 1861, 2005, 2150, 2295, 2440, 2584, 2729, 2874, 3019, 3163, 3308, 3453, 3598, 3742, 3887, 4032, 4177, 4321, 4466, 4611, 4756, 4900, 5045, 5190, 5335, 5479, 5624, 5769, 5914, 6058, 6203, 6348, 6493, 6637, 6782, 6927, 7072, 7216, 7361, 7506, 7651, 7795, 7940, 8085, 8230, 8374, 8519, 8664, 8809, 8953, 9098, 9243, 9388, 9532, 9677, 9822, 9967, 10111, 10256, 10401, 10546, 10690, 10835, 10980, 11125, 11269, 11414]]
    hit0 = 7
    data1 = [int(i*1.051*1.085*1.211) for i in [0, 5378, 5923, 6469, 7014, 7560, 8106, 8651, 9197, 9742, 10288, 10834, 11379, 11925, 12470, 13016, 13562, 14107, 14653, 15198, 15744, 16290, 16835, 17381, 17926, 18472, 19018, 19563, 20109, 20654, 21200, 21746, 22291, 22837, 23382, 23928, 24474, 25019, 25565, 26110, 26656, 27202, 27747, 28293, 28839, 29384, 29930, 30475, 31021, 31567, 32112, 32658, 33203, 33749, 34295, 34840, 35386, 35931, 36477, 37023, 37568, 38114, 38659, 39205, 39751, 40296, 40842, 41387, 41933, 42479, 43024]]
    hit1 = 1
    CD = 30.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    MP = [400, 1620]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.33


class 技能17(主动技能):
    名称 = '夺命大念阵'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.051*1.085*1.211) for i in [0, 1826, 2011, 2196, 2381, 2566, 2752, 2937, 3122, 3307, 3493, 3678, 3863, 4048, 4234, 4419, 4604, 4789, 4975, 5160, 5345, 5530, 5716, 5901, 6086, 6271, 6457, 6642, 6827, 7012, 7198, 7383, 7568, 7753, 7939, 8124, 8309, 8494, 8680, 8865, 9050, 9235, 9421, 9606, 9791, 9976, 10162, 10347, 10532, 10717, 10903, 11088, 11273, 11458, 11644, 11829, 12014, 12199, 12385, 12570, 12755, 12940, 13126, 13311, 13496, 13681, 13867, 14052, 14237, 14422, 14608]]
    hit0 = 6
    data1 = [int(i*1.051*1.085*1.211) for i in [0, 16434, 18101, 19768, 21435, 23102, 24770, 26437, 28104, 29771, 31439, 33106, 34773, 36440, 38107, 39775, 41442, 43109, 44776, 46444, 48111, 49778, 51445, 53112, 54780, 56447, 58114, 59781, 61449, 63116, 64783, 66450, 68117, 69785, 71452, 73119, 74786, 76453, 78121, 79788, 81455, 83122, 84790, 86457, 88124, 89791, 91458, 93126, 94793, 96460, 98127, 99795, 101462, 103129, 104796, 106463, 108131, 109798, 111465, 113132, 114800, 116467, 118134, 119801, 121468, 123136, 124803, 126470, 128137, 129805, 131472]]
    hit1 = 1
    CD = 50.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    MP = [800, 1680]
    无色消耗 = 2

    def 装备护石(self):
        self.倍率 *= 1.32


class 技能18(被动技能):
    名称 = '龙神之力'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40
    # 二觉被动双加成
    关联技能2 = ['念珠连射']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02* self.等级, 5)


class 技能19(主动技能):
    名称 = '退魔阴阳符'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.05*1.085*1.211) for i in [0, 471, 518, 566, 614, 662, 710, 757, 805, 853, 901, 949, 996, 1044, 1092, 1140, 1188, 1235, 1283, 1331, 1379, 1427, 1474, 1522, 1570, 1618, 1666, 1713, 1761, 1809, 1857, 1905, 1952, 2000, 2048, 2096, 2144, 2191, 2239, 2287, 2335, 2383, 2430, 2478, 2526, 2574, 2622, 2669, 2717, 2765, 2813, 2860, 2908, 2956, 3004, 3052, 3099, 3147, 3195, 3243, 3291, 3338, 3386, 3434, 3482, 3530, 3577, 3625, 3673, 3721, 3769]]
    hit0 = 1
    data1 = [int(i*1.05*1.085*1.211) for i in [0, 3886, 4281, 4675, 5069, 5464, 5858, 6252, 6647, 7041, 7435, 7830, 8224, 8618, 9013, 9407, 9801, 10196, 10590, 10984, 11379, 11773, 12167, 12562, 12956, 13350, 13745, 14139, 14533, 14928, 15322, 15716, 16110, 16505, 16899, 17293, 17688, 18082, 18476, 18871, 19265, 19659, 20054, 20448, 20842, 21237, 21631, 22025, 22420, 22814, 23208, 23603, 23997, 24391, 24786, 25180, 25574, 25969, 26363, 26757, 27152, 27546, 27940, 28335, 28729, 29123, 29518, 29912, 30306, 30700, 31095]]
    hit1 = 12
    CD = 40.0
    是否有护石 = 1

    MP = [580, 4500]
    无色消耗 = 3

    def 装备护石(self,):
        self.倍率 *= 1.32

class 技能20(主动技能):
    名称 = '天坠阴阳玉'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.052*1.085*1.25) for i in [0, 3007, 3312, 3617, 3922, 4227, 4532, 4837, 5142, 5447, 5753, 6058, 6363, 6668, 6973, 7278, 7583, 7888, 8193, 8498, 8803, 9109, 9414, 9719, 10024, 10329, 10634, 10939, 11244, 11549, 11854, 12159, 12465, 12770, 13075, 13380, 13685, 13990, 14295, 14600, 14905, 15210, 15515, 15820, 16126, 16431, 16736, 17041, 17346, 17651, 17956, 18261, 18566, 18871, 19176, 19482, 19787, 20092, 20397, 20702, 21007, 21312, 21617, 21922, 22227, 22532, 22838, 23143, 23448, 23753, 24058]]
    hit0 = 3
    data1 = [int(i*1.052*1.085*1.25) for i in [0, 35519, 39122, 42726, 46329, 49932, 53536, 57139, 60743, 64346, 67950, 71553, 75156, 78760, 82363, 85967, 89570, 93173, 96777, 100380, 103984, 107587, 111190, 114794, 118397, 122001, 125604, 129208, 132811, 136414, 140018, 143621, 147225, 150828, 154431, 158035, 161638, 165242, 168845, 172448, 176052, 179655, 183259, 186862, 190466, 194069, 197672, 201276, 204879, 208483, 212086, 215689, 219293, 222896, 226500, 230103, 233706, 237310, 240913, 244517, 248120, 251723, 255327, 258930, 262534, 266137, 269741, 273344, 276947, 280551, 284154]]
    hit1 = 1
    CD = 45.0
    是否有护石 = 1

    MP = [580, 4500]
    无色消耗 = 5

    def 装备护石(self):
        self.hit0 = 0
        self.倍率 *= 1.61
        self.CDR *= 0.86

class 技能21(主动技能):
    名称 = '龙威如狱·龙恩如海'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.085*1.211) for i in [0, 3402, 4191, 4980, 5769, 6558, 7347, 8136, 8925, 9714, 10503, 11292, 12081, 12870, 13659, 14448, 15237, 16026, 16815, 17604, 18393, 19182, 19971, 20760, 21549, 22338, 23127, 23917, 24706, 25495, 26284, 27073, 27862, 28651, 29440, 30229, 31018, 31807, 32596, 33385, 34174, 34963, 35752, 36541, 37330, 38119, 38908, 39697, 40486, 41275, 42064, 42853, 43642, 44431, 45220, 46009, 46798, 47587, 48376, 49165, 49954, 50743, 51532, 52321, 53110, 53899, 54688, 55477, 56266, 57055, 57844]]
    hit0 = 9
    data1 = [int(i*1.085*1.211) for i in [0, 5103, 6287, 7470, 8654, 9838, 11021, 12205, 13388, 14572, 15755, 16939, 18122, 19306, 20489, 21673, 22856, 24040, 25223, 26407, 27590, 28774, 29957, 31141, 32324, 33508, 34691, 35875, 37059, 38242, 39426, 40609, 41793, 42976, 44160, 45343, 46527, 47710, 48894, 50077, 51261, 52444, 53628, 54811, 55995, 57178, 58362, 59545, 60729, 61913, 63096, 64280, 65463, 66647, 67830, 69014, 70197, 71381, 72564, 73748, 74931, 76115, 77298, 78482, 79665, 80849, 82032, 83216, 84399, 85583, 86766]]
    hit1 = 6
    data2 = [int(i*1.085*1.211) for i in [0, 40831, 50299, 59767, 69236, 78704, 88172, 97640, 107108, 116576, 126045, 135513, 144981, 154449, 163917, 173386, 182854, 192322, 201790, 211258, 220726, 230195, 239663, 249131, 258599, 268067, 277535, 287004, 296472, 305940, 315408, 324876, 334345, 343813, 353281, 362749, 372217, 381685, 391154, 400622, 410090, 419558, 429026, 438494, 447963, 457431, 466899, 476367, 485835, 495304, 504772, 514240, 523708, 533176, 542644, 552113, 561581, 571049, 580517, 589985, 599453, 608922, 618390, 627858, 637326, 646794, 656263, 665731, 675199, 684667, 694135]]
    hit2 = 1
    CD = 180.0

    MP = [2500, 5000]
    无色消耗 = 10


class 技能22(被动技能):
    名称 = '乾坤之境'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能23(主动技能):
    名称 = '天泽神龙阵'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    data0 = [int(i*1.05*1.085*1.211) for i in [0, 6033, 6645, 7257, 7869, 8481, 9094, 9706, 10318, 10930, 11542, 12154, 12766, 13378, 13990, 14602, 15215, 15827, 16439, 17051, 17663, 18275, 18887, 19499, 20111, 20723, 21336, 21948, 22560, 23172, 23784, 24396, 25008, 25620, 26232, 26844, 27457, 28069, 28681, 29293, 29905, 30517, 31129, 31741, 32353, 32965, 33578, 34190, 34802, 35414, 36026, 36638, 37250, 37862, 38474, 39086, 39699, 40311, 40923, 41535, 42147, 42759, 43371, 43983, 44595, 45207, 45820, 46432, 47044, 47656, 48268]]
    hit0 = 10
    data1 = [int(i*1.05*1.085*1.211) for i in [0, 34079, 37536, 40994, 44451, 47908, 51366, 54823, 58280, 61738, 65195, 68652, 72110, 75567, 79024, 82482, 85939, 89396, 92854, 96311, 99768, 103226, 106683, 110140, 113598, 117055, 120512, 123970, 127427, 130884, 134342, 137799, 141256, 144714, 148171, 151628, 155086, 158543, 162001, 165458, 168915, 172373, 175830, 179287, 182745, 186202, 189659, 193117, 196574, 200031, 203489, 206946, 210403, 213861, 217318, 220775, 224233, 227690, 231147, 234605, 238062, 241519, 244977, 248434, 251891, 255349, 258806, 262263, 265721, 269178, 272635]]
    hit1 = 1
    CD = 60.0

    MP = [870, 6750]
    无色消耗 = 7


class 技能24(主动技能):
    名称 = '神龙之舞·天一'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    data0 = [int(i*1.05*1.085*1.164) for i in [0, 18619, 22937, 27254, 31572, 35890, 40207, 44525, 48842, 53160, 57478, 61795, 66113, 70430, 74748, 79066, 83383, 87701, 92018, 96336, 100654, 104971, 109289, 113606, 117924, 122242, 126559, 130877, 135194, 139512, 143830, 148147, 152465, 156782, 161100, 165418, 169735, 174053, 178370, 182688, 187006, 191323, 195641, 199958, 204276, 208594, 212911, 217229, 221546, 225864, 230182, 234499, 238817, 243134, 247452, 251770, 256087, 260405, 264722, 269040, 273358, 277675, 281993, 286310, 290628, 294946, 299263, 303581, 307898, 312216, 316534]]
    hit0 = 5
    data1 = [int(i*1.05*1.085*1.164) for i in [0, 62065, 76457, 90849, 105241, 119633, 134025, 148417, 162809, 177201, 191593, 205985, 220377, 234769, 249161, 263553, 277945, 292337, 306729, 321121, 335513, 349905, 364297, 378689, 393081, 407473, 421865, 436257, 450649, 465041, 479433, 493825, 508217, 522609, 537001, 551393, 565785, 580177, 594569, 608961, 623353, 637745, 652137, 666529, 680921, 695313, 709705, 724097, 738489, 752881, 767273, 781665, 796057, 810449, 824841, 839233, 853625, 868017, 882409, 896801, 911193, 925585, 939977, 954369, 968761, 983153, 997545, 1011937, 1026329, 1040721, 1055113]]
    hit1 = 1
    data2 = [int(i*1.05*1.085*1.164) for i in [0, 22166, 27306, 32446, 37586, 42726, 47866, 53006, 58146, 63286, 68426, 73566, 78706, 83846, 88986, 94126, 99266, 104406, 109546, 114686, 119826, 124966, 130106, 135246, 140386, 145526, 150666, 155806, 160946, 166086, 171226, 176366, 181506, 186646, 191786, 196926, 202066, 207206, 212346, 217486, 222626, 227766, 232906, 238046, 243186, 248326, 253466, 258606, 263746, 268886, 274026, 279166, 284306, 289446, 294586, 299726, 304866, 310006, 315146, 320286, 325426, 330566, 335706, 340846, 345986, 351126, 356266, 361406, 366546, 371686, 376826]]
    hit2 = 7
    CD = 290.0

    MP = [4000, 8000]
    无色消耗 = 15


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'sorceress'
        self.名称 = '神启·巫女'
        self.角色 = '圣职者(女)'
        self.角色类型 = '输出'
        self.职业 = '巫女'
        self.武器选项 = ['念珠']
        self.输出类型选项 = ['魔法百分比']
        self.防具精通属性 = ['智力']
        self.类型 = '魔法百分比'
        self.武器类型 = '念珠'
        self.防具类型 = '布甲'
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
        self.buff = 2.08

        super().__init__()