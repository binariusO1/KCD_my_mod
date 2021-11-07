import os

PATH_VAL = "Data/Libs/Tables/item/"
FILE_INPUT = "item_excel_to_xml_input.txt"
FILE_TEMPLATE = "item_excel_to_xml_template.txt"
FIRST_ROW = []
INPUT_ARRAY = []
#melee_weapon.xml
XML_MELEE_WEAPON = "melee_weapon.xml"
XML_MELEE_WEAPON_TEMP = "melee_weapon_temp.xml"
ARRAY_MELEE_WEAPON = ["attack", "slash_att_mod", "smash_att_mod", "stab_att_mod"]
ARRAY_MELEE_WEAPON_VALUE = [9, 11, 12, 13]
#weapon.xml
XML_WEAPON = "weapon.xml"
XML_WEAPON_TEMP = "weapon_temp.xml"
ARRAY_WEAPON = ["agi_req", "defense", "max_status", "str_req"]
ARRAY_WEAPON_VALUE = [18, 10, 20, 17]
#armor.xml
XML_ARMOR = "armor.xml"
XML_ARMOR_TEMP = "weapon_temp.xml"
ARRAY_ARMOR = ["slash_def", "smash_def", "stab_def", "max_status", "str_req"]
ARRAY_ARMOR_VALUE = [11, 12, 13, 20, 17]
#pickable_item.xml
XML_PICKABLE_ITEM = "pickable_item.xml"
XML_PICKABLE_ITEM_TEMP = "pickable_item_temp.xml"
ARRAY_PICKABLE_ITEM = ["weight", "price"]
ARRAY_PICKABLE_ITEM_VALUE = [6, 24]
#equippable_item.xml
XML_EQUIPPABLE_ITEM = "equippable_item.xml"
XML_EQUIPPABLE_ITEM_TEMP = "equippable_item_temp.xml"
ARRAY_EQUIPPABLE_ITEM = ["charisma"]
ARRAY_EQUIPPABLE_ITEM_VALUE = [19]


def read_first_row(file):
    f = open(file, "r", encoding="utf8")
    lines = f.readlines()
    for x in lines:
        FIRST_ROW.append(x.split())

    f.close()
    return ""


def read_input(file):
    f = open(file, "r", encoding="utf8")
    lines = f.readlines()
    for line in lines:
        INPUT_ARRAY.append(line.split("\t"))
    #modify_melee_weapon()
    f.close()
    return ""


def modify_melee_weapon():
    print("fun modify_melee_weapon()")
    f = open(PATH_VAL + XML_MELEE_WEAPON, "r", encoding="utf8")
    f2 = open(PATH_VAL + XML_MELEE_WEAPON_TEMP, "w", encoding="utf8")
    lines = f.readlines()

    for line in lines:
        #line = line[:-1]
        for i, row in enumerate(INPUT_ARRAY):
            pos_id = line.find(INPUT_ARRAY[i][2])

            if pos_id > 0:
                #print(line, INPUT_ARRAY[i][2])

                find_value_p = 0
                str_to_end = ""

                _value = False
                j = 0

                for value in ARRAY_MELEE_WEAPON:
                    #print(value)
                    find_value = line.find(value)
                    if find_value > 0:
                        find_value_p = find_value + len(value) + 2
                        str_to_end = line[find_value_p: (len(line) - 1): 1]
                        _value = True
                        #break
                    if _value:
                        q = str_to_end.find('\"')
                        str_start_to_value = line[0: find_value_p: 1]
                        str_value_to_end = line[find_value_p+q: (len(line)): 1]
                        #print(str_start_to_value, INPUT_ARRAY[i][mw_value], str_value_to_end)
                        _value = False


                        val = INPUT_ARRAY[i][ARRAY_MELEE_WEAPON_VALUE[j]]
                        val2 = val.replace(",", ".")

                        #print(val2)

                        #print(val)
                        #print(str_start_to_value, val, str_value_to_end)
                        line = str_start_to_value + val2 + str_value_to_end
                        #print(line)
                    j = j + 1
                #INPUT_ARRAY.remove(INPUT_ARRAY[i])

        f2.write(line)
    print("\n end")
    f.close()
    f2.close()
    os.remove(PATH_VAL + XML_MELEE_WEAPON)
    os.rename(PATH_VAL + XML_MELEE_WEAPON_TEMP,PATH_VAL+XML_MELEE_WEAPON)
    return ""


def modify_weapon():
    print("fun modify_weapon()")
    f = open(PATH_VAL + XML_WEAPON, "r", encoding="utf8")
    f2 = open(PATH_VAL + XML_WEAPON_TEMP, "w", encoding="utf8")
    lines = f.readlines()

    for line in lines:
        #line = line[:-1]
        for i, row in enumerate(INPUT_ARRAY):
            pos_id = line.find(INPUT_ARRAY[i][2])

            if pos_id > 0:
                #print(line, INPUT_ARRAY[i][2])

                find_value_p = 0
                str_to_end = ""

                _value = False
                j = 0

                for value in ARRAY_WEAPON:
                    #print(value)
                    find_value = line.find(value)
                    if find_value > 0:
                        find_value_p = find_value + len(value) + 2
                        str_to_end = line[find_value_p: (len(line) - 1): 1]
                        _value = True
                        #break
                    if _value:
                        q = str_to_end.find('\"')
                        str_start_to_value = line[0: find_value_p: 1]
                        str_value_to_end = line[find_value_p+q: (len(line)): 1]
                        #print(str_start_to_value, INPUT_ARRAY[i][mw_value], str_value_to_end)
                        _value = False


                        val = INPUT_ARRAY[i][ARRAY_WEAPON_VALUE[j]]
                        val2 = val.replace(",", ".")

                        #print(val2)

                        #print(val)
                        #print(str_start_to_value, val, str_value_to_end)
                        line = str_start_to_value + val2 + str_value_to_end
                        #print(line)
                    j = j + 1
                #INPUT_ARRAY.remove(INPUT_ARRAY[i])

        f2.write(line)
    print("\n end")
    f.close()
    f2.close()
    os.remove(PATH_VAL + XML_WEAPON)
    os.rename(PATH_VAL + XML_WEAPON_TEMP, PATH_VAL+XML_WEAPON)
    return ""


def modify_armor():
    print("fun modify_armor()")
    f = open(PATH_VAL + XML_ARMOR, "r", encoding="utf8")
    f2 = open(PATH_VAL + XML_ARMOR_TEMP, "w", encoding="utf8")
    lines = f.readlines()

    for line in lines:
        #line = line[:-1]
        for i, row in enumerate(INPUT_ARRAY):
            pos_id = line.find(INPUT_ARRAY[i][2])

            if pos_id > 0:
                #print(line, INPUT_ARRAY[i][2])

                find_value_p = 0
                str_to_end = ""

                _value = False
                j = 0

                for value in ARRAY_ARMOR:
                    #print(value)
                    find_value = line.find(value)
                    if find_value > 0:
                        find_value_p = find_value + len(value) + 2
                        str_to_end = line[find_value_p: (len(line) - 1): 1]
                        _value = True
                        #break
                    if _value:
                        q = str_to_end.find('\"')
                        str_start_to_value = line[0: find_value_p: 1]
                        str_value_to_end = line[find_value_p+q: (len(line)): 1]
                        #print(str_start_to_value, INPUT_ARRAY[i][mw_value], str_value_to_end)
                        _value = False


                        val = INPUT_ARRAY[i][ARRAY_ARMOR_VALUE[j]]
                        val2 = val.replace(",", ".")

                        #print(val2)

                        #print(val)
                        #print(str_start_to_value, val, str_value_to_end)
                        line = str_start_to_value + val2 + str_value_to_end
                        #print(line)
                    j = j + 1
                #INPUT_ARRAY.remove(INPUT_ARRAY[i])

        f2.write(line)
    print("\n end")
    f.close()
    f2.close()
    os.remove(PATH_VAL + XML_ARMOR)
    os.rename(PATH_VAL + XML_ARMOR_TEMP, PATH_VAL+XML_ARMOR)
    return ""


def modify_pickable_item():
    print("fun modify_pickable_item()")
    f = open(PATH_VAL + XML_PICKABLE_ITEM, "r", encoding="utf8")
    f2 = open(PATH_VAL + XML_PICKABLE_ITEM_TEMP, "w", encoding="utf8")
    lines = f.readlines()

    for line in lines:
        #line = line[:-1]
        for i, row in enumerate(INPUT_ARRAY):
            pos_id = line.find(INPUT_ARRAY[i][2])

            if pos_id > 0:
                #print(line, INPUT_ARRAY[i][2])

                find_value_p = 0
                str_to_end = ""

                _value = False
                j = 0

                for value in ARRAY_PICKABLE_ITEM:
                    #print(value)
                    find_value = line.find(value)
                    if find_value > 0:
                        find_value_p = find_value + len(value) + 2
                        str_to_end = line[find_value_p: (len(line) - 1): 1]
                        _value = True
                        #break
                    if _value:
                        q = str_to_end.find('\"')
                        str_start_to_value = line[0: find_value_p: 1]
                        str_value_to_end = line[find_value_p+q: (len(line)): 1]
                        #print(str_start_to_value, INPUT_ARRAY[i][mw_value], str_value_to_end)
                        _value = False


                        val = INPUT_ARRAY[i][ARRAY_PICKABLE_ITEM_VALUE[j]]
                        val2 = val.replace(",", ".")

                        #print(val2)

                        #print(val)
                        #print(str_start_to_value, val, str_value_to_end)
                        line = str_start_to_value + val2 + str_value_to_end
                        #print(line)
                    j = j + 1
                #INPUT_ARRAY.remove(INPUT_ARRAY[i])

        f2.write(line)
    print("\n end")
    f.close()
    f2.close()
    os.remove(PATH_VAL + XML_PICKABLE_ITEM)
    os.rename(PATH_VAL + XML_PICKABLE_ITEM_TEMP, PATH_VAL+XML_PICKABLE_ITEM)
    return ""


def modify_equicappable_item():
    print("fun modify_equicappable_item()")
    f = open(PATH_VAL + XML_EQUIPPABLE_ITEM, "r", encoding="utf8")
    f2 = open(PATH_VAL + XML_EQUIPPABLE_ITEM_TEMP, "w", encoding="utf8")
    lines = f.readlines()

    for line in lines:
        #line = line[:-1]
        for i, row in enumerate(INPUT_ARRAY):
            pos_id = line.find(INPUT_ARRAY[i][2])

            if pos_id > 0:
                #print(line, INPUT_ARRAY[i][2])

                find_value_p = 0
                str_to_end = ""

                _value = False
                j = 0

                for value in ARRAY_EQUIPPABLE_ITEM:
                    #print(value)
                    find_value = line.find(value)
                    if find_value > 0:
                        find_value_p = find_value + len(value) + 2
                        str_to_end = line[find_value_p: (len(line) - 1): 1]
                        _value = True
                        #break
                    if _value:
                        q = str_to_end.find('\"')
                        str_start_to_value = line[0: find_value_p: 1]
                        str_value_to_end = line[find_value_p+q: (len(line)): 1]
                        #print(str_start_to_value, INPUT_ARRAY[i][mw_value], str_value_to_end)
                        _value = False


                        val = INPUT_ARRAY[i][ARRAY_EQUIPPABLE_ITEM_VALUE[j]]
                        val2 = val.replace(",", ".")

                        #print(val2)

                        #print(val)
                        #print(str_start_to_value, val, str_value_to_end)
                        line = str_start_to_value + val2 + str_value_to_end
                        #print(line)
                    j = j + 1
                #INPUT_ARRAY.remove(INPUT_ARRAY[i])

        f2.write(line)
    print("\n end2")
    f.close()
    f2.close()
    os.remove(PATH_VAL + XML_EQUIPPABLE_ITEM)
    os.rename(PATH_VAL + XML_EQUIPPABLE_ITEM_TEMP, PATH_VAL+XML_EQUIPPABLE_ITEM)
    return ""


read_first_row(FILE_TEMPLATE)
read_input(FILE_INPUT)
print("select: Armour - a / Weapon - w ")
while True:
    choice = input()
    if choice == 'a':
        modify_pickable_item()
        modify_equicappable_item()
        modify_armor()
        break
    elif choice == 'w':
        modify_melee_weapon()
        modify_weapon()
        modify_pickable_item()
        modify_equicappable_item()
        break
    else:
        print("zly wybór")

input()
