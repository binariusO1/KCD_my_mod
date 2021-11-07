import xlsxwriter

PATH_VAL = "Data/Libs/Tables/item/"
VAL1 = ["pickable_item.xml","weight"]
VAL2 = ["",""]
VAL3 = ["",""]
VAL4 = ["melee_weapon.xml","attack"]
VAL5 = ["weapon.xml","defense"]
VAL6A = [ "armor.xml","slash_def"]
VAL6W = [ "melee_weapon.xml","slash_att_mod"]
VAL7A = ["armor.xml","smash_def"]
VAL7W = [ "melee_weapon.xml","smash_att_mod"]
VAL8A = ["armor.xml","stab_def"]
VAL8W = ["melee_weapon.xml","stab_att_mod"]
VAL9 = ["",""]
VAL10 = ["",""]
VAL11 = ["",""]
VAL12A = ["armor.xml","str_req"]
VAL12W = ["weapon.xml","str_req"]
VAL13 = ["weapon.xml","agi_req"]
VAL14 = ["equippable_item.xml","charisma"]
VAL15A = ["armor.xml","max_status"]
VAL15W = ["weapon.xml","max_status"]
VAL16 = ["",""]
VAL17 = ["",""]
VAL18 = ["",""]
VAL19 = ["pickable_item.xml","price"]

_ARR_ARMOR = [ VAL1 , VAL2, VAL3, VAL4, VAL5, VAL6A, VAL7A, VAL8A, VAL9, VAL10, VAL11, VAL12A, VAL13, VAL14, VAL15A, VAL16, VAL17, VAL18, VAL19  ]
_ARR_WEAPON = [ VAL1 , VAL2, VAL3, VAL4, VAL5, VAL6W, VAL7W, VAL8W, VAL9, VAL10, VAL11, VAL12W, VAL13, VAL14, VAL15W, VAL16, VAL17, VAL18, VAL19  ]

SCRIPT_HASH = "item_xml_to_excel_input.txt"
SCRIPT_OUTPUT = "item_xml_to_excel_output_"
SCRIPT_OUTPUT_TXT = ".txt"

HASH_LIST = []

LIST_P = []


def create_workbook():
    workbook = xlsxwriter.Workbook("item_xml_to_excel_workbook.xlsx")

    return workbook


def create_headers(worksheet):
    temp_arr = ["weight","weight[kg]","","attack","defence","slash","smash","stab","N_slash","N_smash","N_stab","str","agi","char","stat","wid","eks","hał","price"]
    for i in range (len(temp_arr)):
        worksheet.write(0, i, temp_arr[i])


def read_hash(file_name):
    print("def read_hash()")
    file = open(file_name, "r", encoding="utf8")

    lines = file.readlines()
    for hash in lines:
        hash = hash[0: 36: 1]

        HASH_LIST.append(hash)

    file.close()


def read_type(file_name):
    file = open(file_name, "r", encoding="utf8")
    lines = file.readlines()
    for line in lines:
        if line.find("weapon") > 0:
            file.close()
            return True
        else:
            file.close()
            return False


def read(file_name,value_name,COL,worksheet):
    print("def read()")


    if file_name == "":
        return ""
    file = open(PATH_VAL+file_name, "r", encoding="utf8")
    #file_output = open(SCRIPT_OUTPUT+value_name+SCRIPT_OUTPUT_TXT, "w")

    lines = file.readlines()

    for i_hash, hash in enumerate(HASH_LIST):

        #if hash == "":
            #file_output.write('\n')
            #continue

        find_value_p = 0
        find_value_p2 = 0
        str_to_end = ""

        _value = False
        for line in lines:
            line = line[:-1]

            find_num = line.find(hash)
            if find_num > 0:
                find_hash = line.find(value_name)
                if find_hash > 0:
                    find_value_p = find_hash+len(value_name)+2
                    str_to_end = line[find_value_p: (len(line)-1): 1]
                    _value = True
                    break
        if _value:
            q = str_to_end.find('\"')
            if q > 0:
                find_value_p2 = q

            value_len = find_value_p + find_value_p2
            val = ""
            for i in range(q):
                #if line[find_value_p] == ".":
                    #val += ","
                #else:
                val += line[find_value_p]
                find_value_p = find_value_p + 1

            LIST_P.append(val)
            #print(i_hash+1, COL ,val )
            val = float(val)
            worksheet.write(i_hash+1,COL,(float.__round__(val,2)))
            #file_output.write(val+'\n')

    file.close()

    #file_output.close()
    return ""


workbook = create_workbook()
worksheet = workbook.add_worksheet()
create_headers(worksheet)

#--------
read_hash(SCRIPT_HASH)
for i in range (0,len(_ARR_WEAPON),1):

    #print(_ARR_WEAPON[i][0])
    if read_type(SCRIPT_HASH):
        read(_ARR_WEAPON[i][0],_ARR_WEAPON[i][1],i,worksheet)
    else:
        read(_ARR_ARMOR[i][0],_ARR_ARMOR[i][1],i,worksheet)

workbook.close()

