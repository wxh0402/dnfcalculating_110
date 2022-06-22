
from core.baseClass.skill import 技能
from core.baseClass.character import Character
from core.baseClass.skill import 主动技能, 被动技能


class 技能0(被动技能):
    名称 = '唤魔：蛇腹剑'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)


class 技能1(主动技能):
    名称 = '蛇腹剑：破'
    所在等级 = 20

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 5.0
    TP成长 = 0.10
    TP上限 = 7
    data0 = [0, 743, 818, 894, 969, 1044, 1120, 1195, 1271, 1346, 1422, 1497, 1572, 1648, 1723, 1799, 1874, 1949, 2025, 2100, 2176, 2251, 2326, 2402, 2477, 2553, 2628, 2703, 2779, 2854, 2930, 3005, 3080, 3156, 3230,
             3306, 3381, 3456, 3532, 3607, 3683, 3758, 3833, 3909, 3984, 4060, 4135, 4210, 4286, 4361, 4437, 4512, 4588, 4663, 4738, 4814, 4889, 4965, 5040, 5115, 5191, 5266, 5342, 5417, 5492, 5568, 5643, 5719, 5794, 5869, 5945]
    hit0 = 4
    MP = [8, 170]


class 技能2(主动技能):
    名称 = '蛇腹剑：舞'
    所在等级 = 20

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 6.0
    TP成长 = 0.10
    TP上限 = 7

    data0 = [0, 1131, 1246, 1361, 1475, 1591, 1705, 1821, 1935, 2049, 2165, 2279, 2394, 2509, 2624, 2739, 2854, 2968, 3084, 3198, 3312, 3428, 3542, 3657, 3772, 3887, 4002, 4117, 4231, 4347, 4461, 4575, 4691, 4805, 4920,
             5035, 5150, 5265, 5380, 5494, 5610, 5724, 5838, 5954, 6068, 6184, 6298, 6413, 6528, 6643, 6757, 6873, 6987, 7101, 7217, 7331, 7447, 7561, 7676, 7791, 7906, 8020, 8136, 8250, 8364, 8480, 8594, 8710, 8824, 8939, 9054]
    data1 = [0, 1072, 1181, 1289, 1399, 1507, 1616, 1725, 1834, 1943, 2052, 2160, 2270, 2378, 2487, 2596, 2705, 2813, 2923, 3031, 3140, 3249, 3358, 3466, 3576, 3684, 3793, 3902, 4011, 4119, 4229, 4337, 4445, 4555, 4664,
             4772, 4882, 4990, 5098, 5208, 5316, 5425, 5535, 5643, 5751, 5861, 5969, 6078, 6187, 6296, 6404, 6514, 6622, 6731, 6840, 6949, 7057, 7167, 7275, 7384, 7493, 7602, 7710, 7820, 7928, 8037, 8146, 8255, 8363, 8473, 8581]
    data2 = [0, 1408, 1551, 1694, 1837, 1980, 2123, 2266, 2409, 2552, 2694, 2837, 2980, 3123, 3266, 3409, 3552, 3695, 3838, 3981, 4124, 4267, 4410, 4553, 4696, 4839, 4982, 5125, 5268, 5411, 5554, 5695, 5838, 5981, 6124, 6267,
             6410, 6553, 6696, 6839, 6982, 7125, 7268, 7411, 7554, 7697, 7840, 7983, 8126, 8269, 8412, 8555, 8697, 8840, 8983, 9126, 9269, 9412, 9555, 9698, 9841, 9984, 10127, 10270, 10413, 10555, 10698, 10841, 10984, 11127, 11270]

    hit0 = 1
    hit1 = 1
    hit2 = 1

    MP = [15, 300]


class 技能3(主动技能):
    名称 = '蛇腹剑：刺'
    所在等级 = 25

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7
    data0 = [0, 2552, 2812, 3071, 3330, 3589, 3847, 4107, 4366, 4625, 4884, 5144, 5402, 5661, 5920, 6179, 6439, 6697, 6957, 7215, 7474, 7734, 7992, 8252, 8510, 8770, 9029, 9287, 9547, 9805, 10065, 10324, 10583, 10842, 11101, 11360, 11619,
             11878, 12137, 12397, 12655, 12914, 13173, 13432, 13692, 13950, 14210, 14469, 14727, 14987, 15245, 15505, 15764, 16023, 16282, 16540, 16800, 17059, 17318, 17577, 17837, 18095, 18354, 18613, 18872, 19132, 19390, 19650, 19908, 20167, 20427]
    data1 = [0, 3443, 3793, 4142, 4492, 4841, 5191, 5541, 5889, 6238, 6588, 6938, 7287, 7637, 7986, 8336, 8685, 9034, 9383, 9733, 10082, 10432, 10781, 11131, 11480, 11830, 12178, 12528, 12877, 13227, 13576, 13926, 14276, 14625, 14975, 15323, 15673,
             16022, 16372, 16721, 17071, 17420, 17770, 18119, 18468, 18817, 19167, 19516, 19866, 20215, 20565, 20914, 21264, 21612, 21962, 22311, 22661, 23011, 23360, 23710, 24059, 24409, 24757, 25107, 25456, 25806, 26155, 26505, 26854, 27204, 27553]

    hit0 = 1
    hit1 = 1

    MP = [35, 300]


class 技能4(主动技能):
    名称 = '蛇腹剑：缠'
    所在等级 = 25

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7
    data0 = [0, 2578, 2840, 3101, 3363, 3625, 3886, 4147, 4410, 4671, 4933, 5194, 5455, 5718, 5979, 6240, 6502, 6763, 7026, 7287, 7548, 7810, 8072, 8334, 8595, 8856, 9119, 9380, 9641, 9903, 10164, 10427, 10688, 10949, 11211, 11473, 11735,
             11996, 12257, 12520, 12781, 13042, 13304, 13565, 13828, 14089, 14350, 14612, 14873, 15136, 15397, 15658, 15920, 16182, 16443, 16705, 16966, 17229, 17490, 17751, 18013, 18274, 18537, 18798, 19059, 19321, 19583, 19844, 20106, 20367, 20630]
    data1 = [0, 1266, 1394, 1522, 1651, 1780, 1908, 2036, 2165, 2293, 2422, 2551, 2678, 2807, 2936, 3064, 3193, 3320, 3449, 3578, 3707, 3835, 3963, 4092, 4220, 4349, 4478, 4605, 4734, 4863, 4991, 5120, 5247, 5376, 5505,
             5634, 5762, 5890, 6018, 6147, 6276, 6405, 6532, 6661, 6789, 6918, 7047, 7174, 7303, 7432, 7560, 7689, 7818, 7945, 8074, 8203, 8332, 8460, 8588, 8716, 8845, 8974, 9103, 9230, 9359, 9487, 9616, 9745, 9872, 10001, 10130]
    hit0 = 1
    hit1 = 3

    MP = [25, 325]


class 技能5(主动技能):
    名称 = '蛇腹剑：灭'
    所在等级 = 30

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 12.0
    TP成长 = 0.10
    TP上限 = 7
    data0 = [0, 644, 709, 775, 841, 906, 972, 1037, 1102, 1167, 1233, 1299, 1364, 1430, 1495, 1560, 1625, 1691, 1756, 1822, 1888, 1953, 2018, 2084, 2149, 2214, 2281, 2346, 2411, 2476, 2542, 2607, 2672, 2737, 2804, 2869,
             2934, 3000, 3065, 3130, 3195, 3261, 3327, 3393, 3458, 3523, 3588, 3654, 3719, 3785, 3851, 3916, 3981, 4046, 4112, 4177, 4242, 4309, 4374, 4439, 4504, 4570, 4635, 4700, 4766, 4832, 4897, 4963, 5028, 5093, 5158]
    hit0 = 12

    MP = [40, 300]


class 技能6(被动技能):
    名称 = '魔剑控制'
    所在等级 = 30
    等级上限 = 30
    基础等级 = 20

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 20:
                return round(1.000 + 0.015 * self.等级, 5)
            else:
                return round(1.300 + 0.025 * (self.等级 - 20), 5)


class 技能7(主动技能):
    名称 = '血饮狂舞'
    所在等级 = 35

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 20.0
    TP成长 = 0.10
    TP上限 = 7
    data0 = [0, 781, 860, 940, 1019, 1098, 1178, 1257, 1337, 1416, 1496, 1575, 1653, 1733, 1812, 1892, 1971, 2050, 2130, 2209, 2289, 2368, 2447, 2526, 2605, 2685, 2764, 2843, 2923, 3002, 3082, 3161, 3240, 3320, 3399,
             3478, 3557, 3636, 3716, 3795, 3875, 3954, 4033, 4113, 4192, 4272, 4350, 4429, 4509, 4588, 4668, 4747, 4827, 4906, 4985, 5065, 5144, 5224, 5302, 5381, 5461, 5540, 5620, 5699, 5778, 5858, 5937, 6017, 6096, 6175, 6254]
    data1 = [0, 2012, 2217, 2421, 2626, 2830, 3034, 3238, 3442, 3646, 3851, 4055, 4260, 4464, 4668, 4872, 5076, 5281, 5485, 5689, 5893, 6097, 6301, 6507, 6711, 6915, 7119, 7323, 7527, 7731, 7936, 8140, 8344, 8548, 8752, 8957, 9162, 9366,
             9570, 9774, 9978, 10182, 10387, 10591, 10795, 11000, 11204, 11408, 11612, 11817, 12021, 12225, 12429, 12633, 12837, 13043, 13247, 13451, 13655, 13859, 14063, 14267, 14472, 14676, 14880, 15084, 15288, 15492, 15698, 15902, 16106]
    hit0 = 14
    hit1 = 1

    无色消耗 = 1
    MP = [100, 920]

    是否有护石 = 1

    def 装备护石(self):
        self.hit0 = 14 * 2 * 0.56
        self.hit1 = 1 + 1.25
        self.CDR *= 0.9


class 技能8(主动技能):
    名称 = '碎魔剑'
    所在等级 = 35

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    data0 = [0, 2365, 2605, 2846, 3085, 3325, 3565, 3805, 4045, 4285, 4525, 4765, 5005, 5245, 5486, 5725, 5965, 6206, 6445, 6685, 6926, 7165, 7405, 7645, 7885, 8125, 8365, 8605, 8845, 9085, 9325, 9566, 9805, 10045, 10286, 10525, 10765, 11006,
             11245, 11485, 11726, 11965, 12205, 12445, 12685, 12925, 13165, 13405, 13645, 13885, 14125, 14366, 14605, 14845, 15086, 15325, 15565, 15806, 16045, 16285, 16525, 16765, 17005, 17245, 17485, 17725, 17965, 18205, 18446, 18685, 18925]
    hit0 = 5

    MP = [180, 1512]
    无色消耗 = 1


class 技能9(主动技能):
    名称 = '群魔乱舞'
    所在等级 = 40

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 25.0
    TP成长 = 0.10
    TP上限 = 5
    # [蛇腹剑 : 破]
    data0 = [0, 897, 1040, 1183, 1326, 1469, 1612, 1755, 1899, 2042, 2185, 2328, 2471, 2614, 2757, 2900, 3043, 3186, 3329, 3472, 3615, 3758, 3901, 4044, 4187, 4330, 4473, 4616, 4759, 4902,
             5045, 5188, 5332, 5475, 5618, 5761, 5904, 6047, 6190, 6333, 6476, 6619, 6762, 6905, 7048, 7191, 7334, 7477, 7620, 7763, 7906, 8049, 8192, 8335, 8478, 8622, 8765, 8908, 9051, 9194, 9337]
    # [蛇腹剑 : 舞]
    data1 = [0, 1196, 1387, 1577, 1768, 1959, 2149, 2340, 2531, 2721, 2913, 3103, 3293, 3485, 3675, 3867, 4057, 4247, 4439, 4629, 4820, 5011, 5201, 5392, 5583, 5773, 5964, 6155, 6346, 6536, 6727,
             6918, 7108, 7300, 7490, 7680, 7872, 8062, 8253, 8444, 8634, 8825, 9016, 9207, 9397, 9588, 9779, 9969, 10160, 10351, 10541, 10733, 10923, 11113, 11305, 11495, 11686, 11877, 12067, 12258, 12449]
    # [蛇腹剑 : 刺]
    data2 = [0, 1794, 2080, 2366, 2652, 2938, 3224, 3510, 3797, 4083, 4369, 4655, 4941, 5227, 5513, 5799, 6085, 6371, 6657, 6943, 7230, 7516, 7802, 8088, 8374, 8660, 8946, 9232, 9518, 9804, 10090, 10376,
             10663, 10949, 11235, 11521, 11807, 12093, 12379, 12665, 12951, 13237, 13523, 13811, 14097, 14383, 14669, 14955, 15241, 15527, 15813, 16099, 16385, 16671, 16957, 17244, 17530, 17816, 18102, 18388, 18674]
    # [蛇腹剑 : 灭]
    data3 = [0, 298, 347, 394, 441, 490, 537, 584, 633, 680, 728, 776, 823, 871, 919, 966, 1014, 1062, 1109, 1157, 1205, 1252, 1300, 1348, 1395, 1443, 1491, 1538, 1586, 1634, 1681,
             1729, 1777, 1825, 1872, 1920, 1968, 2015, 2063, 2111, 2158, 2206, 2254, 2301, 2349, 2397, 2444, 2492, 2540, 2587, 2635, 2683, 2730, 2778, 2826, 2873, 2922, 2969, 3016, 3065, 3112]
    # [血饮狂舞]
    data4 = [0, 326, 377, 430, 482, 534, 586, 638, 690, 741, 794, 846, 898, 950, 1002, 1054, 1106, 1158, 1210, 1262, 1315, 1366, 1418, 1470, 1522, 1574, 1626, 1679, 1730, 1782, 1834,
             1887, 1938, 1990, 2043, 2094, 2146, 2198, 2251, 2302, 2354, 2407, 2459, 2510, 2563, 2615, 2666, 2718, 2771, 2823, 2874, 2927, 2979, 3031, 3082, 3135, 3187, 3238, 3291, 3343, 3395]
    hit0 = 4
    hit1 = 3
    hit2 = 2
    hit3 = 12
    hit4 = 11

    MP = [360, 3024]
    无色消耗 = 1

    是否有护石 = 1

    def 装备护石(self):
        self.倍率 = 1.34


class 技能10(主动技能):
    名称 = '唤魔：塔莫斯之袭'
    所在等级 = 45

    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60

    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5
    data0 = [0, 1193, 1314, 1435, 1557, 1677, 1798, 1919, 2041, 2162, 2282, 2403, 2525, 2646, 2767, 2887, 3009, 3130, 3251, 3373, 3493, 3614, 3735, 3857, 3977, 4098, 4220, 4341, 4462, 4582, 4704, 4825, 4946, 5068, 5188,
             5309, 5430, 5552, 5673, 5793, 5914, 6036, 6157, 6278, 6398, 6520, 6641, 6762, 6884, 7004, 7125, 7246, 7368, 7489, 7609, 7731, 7852, 7973, 8094, 8215, 8336, 8457, 8579, 8700, 8820, 8941, 9063, 9184, 9304, 9425, 9547]
    data1 = [0, 9378, 10330, 11282, 12233, 13185, 14136, 15087, 16040, 16991, 17942, 18893, 19846, 20797, 21748, 22700, 23651, 24602, 25555, 26506, 27457, 28408, 29361, 30312, 31263, 32215, 33166, 34118, 35070, 36021, 36972, 37923, 38876, 39827, 40778,
             41730, 42682, 43633, 44585, 45536, 46487, 47439, 48391, 49342, 50293, 51246, 52197, 53148, 54100, 55051, 56003, 56955, 57906, 58857, 59808, 60761, 61712, 62663, 63615, 64567, 65518, 66470, 67421, 68372, 69323, 70276, 71227, 72178, 73130, 74082, 75033]
    data2 = [0, 3600, 3965, 4330, 4695, 5060, 5425, 5791, 6156, 6522, 6887, 7253, 7618, 7983, 8348, 8713, 9078, 9444, 9809, 10174, 10539, 10904, 11269, 11635, 12000, 12365, 12731, 13096, 13462, 13827, 14192, 14557, 14922, 15288, 15653, 16018, 16383,
             16748, 17113, 17479, 17844, 18209, 18574, 18940, 19306, 19671, 20036, 20401, 20766, 21132, 21497, 21862, 22227, 22592, 22957, 23323, 23688, 24053, 24418, 24783, 25150, 25515, 25880, 26245, 26610, 26976, 27341, 27706, 28071, 28436, 28801]

    hit0 = 8
    hit1 = 1
    hit2 = 1

    是否有护石 = 1

    无色消耗 = 2
    MP = [90, 1500]

    def 装备护石(self):
        self.倍率 *= 1.48
        self.hit2 = 0


class 技能11(被动技能):
    名称 = '贪欲之燔祭'
    所在等级 = 48

    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


class 技能12(主动技能):
    名称 = '空绝斩：千刃'
    所在等级 = 50

    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    CD = 145.0
    data0 = [0, 8279, 10199, 12120, 14039, 15959, 17880, 19800, 21719, 23639, 25560, 27479, 29399, 31319, 33240, 35159, 37079, 39000, 40920, 42839, 44759, 46680, 48599, 50519, 52439, 54360, 56279, 58199, 60120, 62039, 63959, 65879, 67800, 69719, 71639, 73560, 75480,
             77399, 79319, 81240, 83159, 85079, 86999, 88920, 90839, 92759, 94680, 96599, 98519, 100439, 102360, 104279, 106199, 108120, 110039, 111959, 113879, 115800, 117719, 119639, 121559, 123480, 125399, 127319, 129240, 131159, 133079, 134999, 136920, 138839, 140759]
    data1 = [0, 12738, 15692, 18645, 21599, 24553, 27507, 30461, 33415, 36369, 39323, 42277, 45230, 48184, 51138, 54091, 57045, 59999, 62953, 65907, 68861, 71814, 74768, 77722, 80676, 83630, 86584, 89538, 92492, 95446, 98399, 101353, 104307, 107261, 110215, 113169, 116123,
             119077, 122031, 124983, 127937, 130891, 133845, 136799, 139753, 142707, 145661, 148614, 151568, 154522, 157476, 160430, 163384, 166338, 169292, 172246, 175199, 178153, 181107, 184060, 187014, 189968, 192922, 195876, 198830, 201783, 204737, 207691, 210645, 213599, 216553]
    data2 = [0, 17833, 21968, 26104, 30239, 34375, 38510, 42645, 46781, 50916, 55052, 59187, 63323, 67458, 71594, 75729, 79863, 83999, 88134, 92270, 96405, 100541, 104676, 108811, 112947, 117082, 121218, 125353, 129489, 133624, 137760, 141895, 146029, 150165, 154300, 158436, 162571,
             166707, 170842, 174978, 179113, 183248, 187384, 191519, 195655, 199790, 203926, 208061, 212197, 216331, 220466, 224602, 228737, 232873, 237008, 241144, 245279, 249415, 253550, 257685, 261821, 265956, 270092, 274226, 278363, 282497, 286632, 290768, 294903, 299039, 303174]
    data3 = [0, 2001, 2465, 2929, 3394, 3858, 4322, 4787, 5250, 5715, 6178, 6643, 7107, 7571, 8035, 8500, 8963, 9428, 9893, 10356, 10821, 11284, 11749, 12213, 12677, 13141, 13606, 14069, 14534, 14997, 15462, 15927, 16390, 16855, 17319, 17783, 18247,
             18712, 19175, 19640, 20103, 20568, 21033, 21496, 21961, 22425, 22889, 23353, 23818, 24281, 24746, 25209, 25674, 26138, 26602, 27067, 27531, 27995, 28459, 28924, 29387, 29852, 30315, 30780, 31244, 31708, 32172, 32637, 33101, 33565, 34030]
    data4 = [0, 0, 0, 0, 0, 0, 3340, 3699, 4057, 4416, 4775, 5133, 5492, 5851, 6209, 6568, 6927, 7285, 7644, 8003, 8361, 8720, 9079, 9437, 9796, 10155, 10513, 10872, 11231, 11590, 11948, 12307, 12666, 13024, 13383, 13742, 14100, 14459,
             14818, 15176, 15535, 15894, 16252, 16611, 16970, 17328, 17687, 18046, 18404, 18763, 19122, 19480, 19839, 20198, 20556, 20915, 21274, 21632, 21991, 22350, 22708, 23067, 23426, 23784, 24143, 24502, 24860, 25219, 25578, 25936, 26295]

    hit0 = 1
    hit1 = 1
    hit2 = 1
    hit3 = 7
    hit4 = 7

    MP = [1500, 12232]
    无色消耗 = 5

    def 等效百分比(self, **argv):
        if self.等级 >= 3:
            self.倍率 *= 1.1
        return super().等效百分比(**argv)


class 技能13(主动技能):
    名称 = '唤魔：逆天之普诺'
    所在等级 = 60

    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5

    data0 = [0, 1552, 1710, 1867, 2025, 2182, 2339, 2497, 2655, 2812, 2970, 3127, 3284, 3442, 3600, 3757, 3915, 4072, 4229, 4387, 4545, 4702, 4860, 5017, 5174, 5332, 5490, 5647, 5805, 5962, 6119, 6277, 6435, 6592, 6750, 6907,
             7064, 7223, 7380, 7538, 7695, 7852, 8009, 8168, 8325, 8483, 8640, 8797, 8954, 9113, 9270, 9428, 9585, 9742, 9899, 10058, 10215, 10373, 10530, 10687, 10844, 11003, 11160, 11318, 11475, 11632, 11789, 11948, 12105, 12263, 12420]
    data1 = [0, 1293, 1424, 1555, 1687, 1819, 1950, 2081, 2212, 2343, 2474, 2606, 2737, 2868, 3000, 3131, 3262, 3393, 3525, 3656, 3787, 3918, 4049, 4180, 4312, 4444, 4575, 4706, 4837, 4968, 5099, 5230, 5363, 5494, 5625,
             5756, 5887, 6018, 6149, 6281, 6413, 6544, 6675, 6806, 6937, 7068, 7200, 7331, 7462, 7594, 7725, 7856, 7987, 8119, 8250, 8381, 8512, 8643, 8774, 8906, 9038, 9169, 9300, 9431, 9562, 9693, 9824, 9957, 10088, 10219, 10350]
    data2 = [0, 7659, 8436, 9213, 9990, 10767, 11544, 12321, 13098, 13875, 14653, 15430, 16207, 16984, 17761, 18538, 19315, 20092, 20869, 21646, 22423, 23200, 23977, 24754, 25531, 26308, 27086, 27863, 28640, 29417, 30194, 30971, 31748, 32525, 33302, 34079,
             34856, 35633, 36410, 37187, 37964, 38741, 39518, 40296, 41073, 41850, 42627, 43404, 44181, 44958, 45735, 46512, 47289, 48066, 48843, 49620, 50397, 51174, 51951, 52729, 53506, 54283, 55060, 55837, 56614, 57391, 58168, 58945, 59722, 60499, 61276]

    hit0 = 5
    hit1 = 8
    hit2 = 1

    无色消耗 = 1
    MP = [120, 1200]

    是否有护石 = 1

    def 装备护石(self):
        self.hit2 = 1 + 0.08 + 0.31


class 技能14(主动技能):
    名称 = '汲血魔剑'
    所在等级 = 70

    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    data0 = [0, 38273, 42155, 46039, 49921, 53804, 57687, 61570, 65452, 69336, 73218, 77101, 80984, 84867, 88749, 92633, 96515, 100398, 104280, 108164, 112046,
             115930, 119812, 123695, 127577, 131460, 135343, 139225, 143109, 146991, 150874, 154757, 158640, 162522, 166406, 170288, 174171, 178054, 181937, 185819, 189703]
    hit0 = 1

    无色消耗 = 2
    MP = [400, 1500]

    是否有护石 = 1

    def 装备护石(self):
        self.hit0 = 1 + 0.07 + 0.15


class 技能15(被动技能):
    名称 = '唤魔：弑神剑'
    所在等级 = 75

    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)

    def 特殊倍率(self):
        return round(1.38 + 0.02 * self.等级, 5)

    data = [0, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11,
            12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19]

    def 次数加成(self):
        return self.data[self.等级]


class 技能16(主动技能):
    名称 = '空绝斩：地裂'
    所在等级 = 75

    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    CD = 40.0
    data0 = [0, 60898, 67076, 73255, 79433, 85611, 91789, 97967, 104146, 110323, 116502, 122680, 128858, 135037, 141214, 147393, 153571, 159749, 165927, 172105, 178284, 184462, 190639, 196818, 202996, 209175, 215352, 221530, 227709, 233887, 240065, 246243, 252421, 258600, 264777, 270956,
             277134, 283312, 289491, 295668, 301847, 308025, 314203, 320381, 326559, 332738, 338916, 345093, 351272, 357450, 363629, 369806, 375984, 382163, 388341, 394519, 400697, 406875, 413054, 419231, 425410, 431588, 437766, 443944, 450122, 456301, 462479, 468657, 474835, 481013, 487192]
    hit0 = 1

    是否有护石 = 1

    MP = [580, 4500]
    无色消耗 = 3

    def 装备护石(self):
        self.倍率 *= 1.34

# 无法抓取


class 技能17(主动技能):
    名称 = '弑神剑：极'
    所在等级 = 80

    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    CD = 45.0
    data0 = [0, 67383, 74221, 81059, 87891, 94728, 101566, 108404, 115237, 122074, 128911, 135749, 142587, 149420, 156257, 163095, 169932, 176765, 183602, 190440, 197278, 204111, 210947, 217785, 224623, 231456, 238294, 245131, 251968, 258806, 265639, 272476, 279314, 286152, 292984, 299822,
             306659, 313497, 320330, 327168, 334004, 340842, 347675, 354513, 361350, 368188, 375020, 381858, 388696, 395533, 402371, 409204, 416041, 422878, 429716, 436549, 443387, 450225, 457061, 463894, 470732, 477570, 484407, 491240, 498077, 504915, 511752, 518585, 525423, 532260, 539098]

    hit0 = 1
    MP = [800, 6000]
    无色消耗 = 5

    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.34
        self.CDR *= 0.9


class 技能18(主动技能):
    名称 = '弑神剑：诸神献祭'
    所在等级 = 85

    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    无色消耗 = 10
    MP = [2500, 5000]

    CD = 180.0

    data0 = [0, 5262, 6482, 7701, 8922, 10142, 11362, 12583, 13802, 15022, 16243, 17463, 18683, 19904, 21123, 22343, 23564, 24784, 26003, 27224, 28444, 29664, 30885, 32105, 33324, 34544, 35765, 36985, 38205, 39425, 40645, 41865, 43086, 44306, 45525, 46746,
             47966, 49186, 50407, 51627, 52846, 54067, 55287, 56507, 57728, 58947, 60167, 61388, 62608, 63828, 65049, 66268, 67488, 68709, 69929, 71148, 72369, 73589, 74809, 76030, 77250, 78469, 79690, 80910, 82130, 83351, 84571, 85790, 87011, 88231, 89451]
    data1 = [0, 19501, 24024, 28546, 33068, 37590, 42113, 46635, 51157, 55680, 60202, 64723, 69245, 73768, 78290, 82812, 87335, 91857, 96379, 100901, 105424, 109946, 114468, 118989, 123513, 128034, 132556, 137079, 141601, 146123, 150645, 155168, 159690, 164212, 168735, 173257,
             177779, 182300, 186824, 191345, 195867, 200390, 204912, 209434, 213956, 218479, 223001, 227523, 232046, 236568, 241090, 245611, 250135, 254656, 259178, 263701, 268223, 272745, 277267, 281790, 286312, 290834, 295357, 299879, 304401, 308922, 313446, 317967, 322489, 327011, 331534]
    data2 = [0, 72857, 89750, 106645, 123540, 140433, 157328, 174221, 191116, 208011, 224904, 241799, 258694, 275587, 292482, 309376, 326270, 343165, 360059, 376953, 393848, 410742, 427636, 444530, 461425, 478319, 495213, 512108, 529002, 545896, 562791, 579684, 596579, 613474, 630367, 647262,
             664157, 681050, 697945, 714840, 731733, 748628, 765523, 782416, 799311, 816206, 833099, 849994, 866888, 883782, 900677, 917570, 934465, 951360, 968253, 985148, 1002042, 1018936, 1035831, 1052725, 1069619, 1086514, 1103408, 1120302, 1137197, 1154091, 1170985, 1187879, 1204774, 1221668, 1238562]
    hit0 = 10
    hit1 = 3
    hit2 = 1


class 技能19(被动技能):
    名称 = '魔源觉醒'
    所在等级 = 95

    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能20(主动技能):
    名称 = '蛇舞血轮剑'
    所在等级 = 95

    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40

    CD = 60.0
    data0 = [0, 13968, 15386, 16803, 18220, 19637, 21055, 22471, 23889, 25306, 26724, 28140, 29558, 30975, 32391, 33809, 35226, 36643, 38060, 39478, 40894, 42312, 43729, 45147, 46563, 47981, 49398, 50815, 52232, 53650, 55066, 56483, 57901, 59318, 60735, 62152,
             63570, 64986, 66404, 67821, 69238, 70655, 72073, 73490, 74907, 76324, 77742, 79158, 80575, 81993, 83409, 84827, 86244, 87662, 89078, 90496, 91913, 93330, 94747, 96165, 97581, 98999, 100416, 101832, 103250, 104667, 106085, 107501, 108919, 110336, 111753]
    data1 = [0, 83815, 92318, 100820, 109323, 117827, 126330, 134833, 143335, 151838, 160342, 168845, 177348, 185851, 194353, 202857, 211360, 219863, 228366, 236868, 245371, 253875, 262378, 270881, 279384, 287886, 296390, 304893, 313396, 321899, 330401, 338904, 347408, 355911, 364414,
             372916, 381419, 389923, 398426, 406929, 415432, 423934, 432438, 440941, 449444, 457947, 466449, 474952, 483456, 491959, 500462, 508965, 517467, 525971, 534474, 542977, 551480, 559982, 568485, 576989, 585492, 593995, 602497, 611000, 619504, 628007, 636510, 645013, 653515, 662019, 670522]

    hit0 = 4
    hit1 = 1

    无色消耗 = 7
    MP = [1065, 8000]


class 技能21(主动技能):
    名称 = '弑神剑：恶魔孤岛'
    所在等级 = 100

    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40

    CD = 290.0
    data0 = [0, 11835, 14578, 17323, 20067, 22812, 25557, 28300, 31045, 33789, 36534, 39278, 42022, 44766, 47511, 50255, 53000, 55743, 58488, 61233, 63977,
             66722, 69465, 72210, 74954, 77699, 80443, 83187, 85931, 88676, 91421, 94165, 96909, 99653, 102398, 105142, 107887, 110630, 113375, 116119, 118864]
    data1 = [0, 266287, 328034, 389782, 451530, 513278, 575025, 636773, 698521, 760268, 822016, 883764, 945512, 1007259, 1069007, 1130755, 1192502, 1254250, 1315998, 1377746, 1439494,
             1501242, 1562990, 1624738, 1686485, 1748233, 1809981, 1871728, 1933476, 1995224, 2056972, 2118719, 2180467, 2242215, 2303962, 2365710, 2427458, 2489205, 2550953, 2612701, 2674449]

    hit0 = 15
    hit1 = 1

    无色消耗 = 15
    MP = [4025, 8055]

    关联技能 = ['无']


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'demon_slayer'
        self.名称 = '极诣·契魔者'
        self.角色 = '鬼剑士(女)'
        self.职业类型 = '输出'
        self.职业 = '契魔者'
        self.武器选项 = ['巨剑', '钝器', '太刀', '短剑']
        self.输出类型选项 = ['物理百分比']
        self.防具精通属性 = ['力量']
        self.类型 = '物理百分比'
        self.武器类型 = '巨剑'
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
        self.buff = 2.00

        super().__init__()

    def 伤害指数计算(self):

        唤魔弑神剑 = self.get_skill_by_name('唤魔：弑神剑')

        x = 唤魔弑神剑.加成倍率(self.武器类型)
        self.get_skill_by_name('血饮狂舞').被动倍率 /= x
        self.get_skill_by_name('唤魔：塔莫斯之袭').被动倍率 /= x

        y = self.get_skill_by_name('魔源觉醒').加成倍率(self.武器类型)
        self.get_skill_by_name('蛇腹剑：缠').被动倍率 *= (x + y - 1) / (x * y)

        self.get_skill_by_name('血饮狂舞').被动倍率 *= 唤魔弑神剑.特殊倍率()
        self.get_skill_by_name('唤魔：塔莫斯之袭').hit0 = 8+唤魔弑神剑.次数加成()
        self.get_skill_by_name('唤魔：塔莫斯之袭').hit1 = 唤魔弑神剑.特殊倍率()

        super().伤害指数计算()
