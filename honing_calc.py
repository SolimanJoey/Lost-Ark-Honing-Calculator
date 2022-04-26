def honing_calc(values):
    armor_silver_1302 = [28164, 28444, 28724, 31056, 31336, 31636, 45183, 51555, 62836, 60850, 61751, 92259, 98166, 99912, 129634]
    armor_gold_1302 = [0, 0, 0, 0, 0, 0, 111, 142, 198, 198, 198, 340, 340, 340, 465]
    armor_shards_1302 = [496, 496, 496, 714, 714, 714, 955, 974, 1007, 1237, 1237, 1339, 1596, 1596, 1703]
    armor_fusion_1302 = [0, 0, 0, 2, 2, 2, 4, 5, 6, 12, 12, 20, 20, 20, 27]
    armor_crystals_1302 = [82, 82, 82, 120, 120, 120, 247, 317, 440, 541, 541, 932, 1107, 1107, 1514]
    armor_leapstones_1302 = [2, 2, 4, 4, 4, 4, 7, 9, 12, 17, 30, 30, 39, 54]

    weapon_silver_1302 = [40268, 40648, 41048, 44312, 44732, 45172, 64607, 73705, 89813, 86909, 88261, 131775, 140121, 142643, 185043]
    weapon_gold_1302 = [0, 0, 0, 0, 0, 0, 190, 244, 339, 339, 339, 583, 583, 583, 797]
    weapon_shards_1302 = [710, 710, 710, 1020, 1020, 1020, 1367, 1394, 1442, 1777, 1777, 1927, 2291, 2291, 2449]
    weapon_fusion_1302 = [0, 0, 0, 2, 2, 2, 7, 9, 12, 12, 12, 20, 30, 30, 40]
    weapon_crystals_1302 = [138, 138, 138, 198, 198, 198, 409, 524, 727, 902, 902, 1553, 1844, 1844, 2523]
    weapon_leapstones_1302 = [4, 4, 6, 6, 6, 6, 13, 17, 23, 29, 29, 49, 49, 59, 80]
    
    armor_silver_1340 = [58744, 59224, 59724, 77504, 78004, 78524, 109368, 120438, 140092, 113318, 115008, 168039, 179670, 182775, 234513, 331518, 387149, 601481, 710047, 1033216]
    armor_gold_1340 = [160, 160, 170, 170, 170, 170, 270, 345, 479, 479, 479, 825, 825, 825, 1195, 1394, 1660, 3204, 3662, 6116]
    armor_shards_1340 = [2522, 2522, 2522, 3626, 3626, 3626, 4793, 4842, 4927, 6072, 6072, 6341, 7545, 7545, 7827, 10612, 14345, 21356, 29300, 44185]
    armor_fusion_1340 = [4, 4, 4, 4, 4, 4, 10, 13, 17, 23, 23, 39 ,39, 39, 54, 67, 67, 138, 161, 245]
    armor_crystals_1340 = [216, 216, 216, 310, 310, 310, 640, 820, 1139, 1403, 1403, 2416, 2872, 2872, 3930, 4554, 4554, 7850, 8926, 13630]
    armor_leapstones_1340 = [4, 6, 6, 6, 6, 8, 13, 21, 29, 29, 29, 59, 59, 59, 80, 93, 107, 184, 206, 350]

    weapon_silver_1340 = [84016, 84696, 85396, 110768, 111508, 112248, 156273, 172081, 200182, 161948, 164314, 240045, 256763, 261129, 334858, 471887, 552795, 858607, 1009098, 1468121]
    weapon_gold_1340 = [300, 300, 300, 300, 300, 320, 507, 650, 902, 902, 930, 1601, 1601, 1601, 2191, 2722, 3187, 6180, 7324, 12756]
    weapon_shards_1340 = [3610, 3610, 3610, 5188, 5188, 5188, 6857, 6927, 7050, 8693, 8693, 9084, 10803, 10803, 11210, 15072, 20516, 30558, 41654, 62931]
    weapon_fusion_1340 = [4, 4, 4, 6, 6, 6, 10, 13, 23, 23, 23 ,39, 49, 49, 67, 80, 93, 184, 206, 350]
    weapon_crystals_1340 = [358, 358, 358, 516, 516, 516, 1064, 1363, 1893, 2338, 2338, 4027, 4784, 4784, 6546, 7594, 7594, 13091, 14876, 22716]
    weapon_leapstones_1340 = [6, 8, 8, 10, 10, 12, 19, 29, 40, 46, 46, 88, 88, 98, 133, 147, 160, 321, 344, 560]

    item = values[0]
    slvl = values[1]
    elvl = values[2]
    num = values[3]
    
    if item == 1:
        silver = sum(armor_silver_1302[slvl:elvl]) * num
        gold = sum(armor_gold_1302[slvl:elvl]) * num
        shards = sum(armor_shards_1302[slvl:elvl]) * num
        sfusion = sum(armor_fusion_1302[slvl:elvl]) * num
        bfusion = 0
        gcrystals = sum(armor_crystals_1302[slvl:elvl]) * num
        dcrystals = 0
        hleapstones = sum(armor_leapstones_1302[slvl:elvl]) * num
        ghleapstones = 0

    elif item == 2:
        silver = sum(armor_silver_1340[slvl:elvl]) * num
        gold = sum(armor_gold_1340[slvl:elvl]) * num
        shards = sum(armor_shards_1340[slvl:elvl]) * num
        sfusion = 0
        bfusion = sum(armor_fusion_1340[slvl:elvl]) * num
        gcrystals = sum(armor_crystals_1340[slvl:elvl]) * num
        dcrystals = 0
        hleapstones = 0
        ghleapstones = sum(armor_leapstones_1340[slvl:elvl]) * num

    elif item == 3:
        silver = sum(weapon_silver_1302[slvl:elvl]) * num
        gold = sum(weapon_gold_1302[slvl:elvl]) * num
        shards = sum(weapon_shards_1302[slvl:elvl]) * num
        sfusion = sum(weapon_fusion_1302[slvl:elvl]) * num
        bfusion = 0
        gcrystals = 0
        dcrystals = sum(weapon_crystals_1302[slvl:elvl]) * num
        hleapstones = sum(weapon_leapstones_1302[slvl:elvl]) * num
        ghleapstones = 0

    else:
        silver = sum(weapon_silver_1340[slvl:elvl]) * num
        gold = sum(weapon_gold_1340[slvl:elvl]) * num
        shards = sum(weapon_shards_1340[slvl:elvl]) * num
        sfusion = 0
        bfusion = sum(weapon_fusion_1340[slvl:elvl]) * num
        gcrystals = 0
        dcrystals = sum(weapon_crystals_1340[slvl:elvl]) * num
        hleapstones = 0
        ghleapstones = sum(weapon_leapstones_1340[slvl:elvl]) * num

    return [silver, gold, shards, sfusion, bfusion, gcrystals, dcrystals, hleapstones, ghleapstones]


def user_input():
    item = input("Please choose item type: armor1302, armor1340, weapon1302, weapon1340\n")
    if item == "armor1302":
        item = 1
        slvl = int(input("Please enter starting level (0-14)\n"))
        while slvl < 0 or slvl > 14:
            slvl = int(input("Please enter a level between 0 and 14\n"))
        elvl = int(input("Please enter end level (1-15)\n"))
        while elvl < slvl or slvl > 15:
            elvl = int(input("Please enter a level higher than starting level and less than or equal 15\n"))
        num = int(input("Please enter how many armor pieces you would like (1-5)\n"))
        while num < 1 or num > 5:
            num = int(input("Please enter a number between 1 and 5 inclusive\n"))
    
    elif item == "armor1340":
        item = 2
        slvl = int(input("Please enter starting level (0-19)\n"))
        while slvl < 0 or slvl > 19:
            slvl = int(input("Please enter a level between 0 and 19\n"))
        elvl = int(input("Please enter end level (1-20)\n"))
        while elvl < slvl or slvl > 20:
            elvl = int(input("Please enter a level higher than starting level and less than or equal to 20\n"))
        num = int(input("Please enter how many armor pieces you would like (1-5)\n"))
        while num < 1 or num > 5:
            num = int(input("Please enter a number between 1 and 5 inclusive\n"))

    elif item == "weapon1302":
        item = 3
        slvl = int(input("Please enter starting level (0-14)\n"))
        while slvl < 0 or slvl > 14:
            slvl = int(input("Please enter a level between 0 and 14\n"))
        elvl = int(input("Please enter end level (1-15)\n"))
        while elvl < slvl or slvl > 15:
            elvl = int(input("Please enter a level higher than starting level and less than or equal 15\n"))
        num = 1

    else:
        item = 4
        slvl = int(input("Please enter starting level (0-19)\n"))
        while slvl < 0 or slvl > 19:
            slvl = int(input("Please enter a level between 0 and 19\n"))
        elvl = int(input("Please enter end level (1-20)\n"))
        while elvl < slvl or slvl > 20:
            elvl = int(input("Please enter a level higher than starting level and less than or equal to 20\n"))
        num = 1

    return [item, slvl, elvl, num]


if __name__ == '__main__':
    silver = 0
    gold = 0
    shards = 0
    sfusion = 0
    bfusion = 0
    gcrystals = 0
    dcrystals = 0
    hleapstones = 0
    ghleapstones = 0
    
    item = user_input()
    mats = honing_calc(item)
    silver += mats[0]
    gold += mats[1]
    shards += mats[2]
    sfusion += mats[3]
    bfusion += mats[4]
    gcrystals += mats[5]
    dcrystals += mats[6]
    hleapstones += mats[7]
    ghleapstones = mats[8]

    while input("Would you like to add more? Press \"y\" for yes and \"n\" for no\n") == "y":
        item = user_input()
        mats = honing_calc(item)
        silver += mats[0]
        gold += mats[1]
        shards += mats[2]
        sfusion += mats[3]
        bfusion += mats[4]
        gcrystals += mats[5]
        dcrystals += mats[6]
        hleapstones += mats[7]
        ghleapstones += mats[8]
    
    print("Total materials needed:")
    print("Silver: ", silver)
    print("Gold: ", gold)
    print("Honor Shards: ", shards)
    print("Simple Oreha Fusion Materials: ", sfusion)
    print("Basic Oreha Fusion Materials: ", bfusion)
    print("Guardian Stone Crystals: ", gcrystals)
    print("Destruction Stone Crystals: ", dcrystals)
    print("Honor Leapstones: ", hleapstones)
    print("Great Honor Leapstones: ", ghleapstones)
