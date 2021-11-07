import xlsxwriter

PATH_VAL = "Data/Libs/Tables/rpg/"
PATH_DESC = "Localization/"
FILE_SOUL = PATH_VAL + "soul.xml"
FILE_V_SOUL = PATH_VAL + "v_soul_character_data.xml"
FILE_DESC = PATH_DESC + "text_ui_soul.xml"
#   excel columns
FILE_TEMPLATE = "soul_xml_to_excel_template.txt"
FIRST_ROW_ARRAY = []
DESC_ARRAY = []


def create_workbook():
    workbook = xlsxwriter.Workbook("soul_xml_to_excel.xlsx")
    return workbook


def create_headers(worksheet):
    for i in range(len(FIRST_ROW_ARRAY)):
        for j in range(len(FIRST_ROW_ARRAY[i])):
            worksheet.write(0, j, FIRST_ROW_ARRAY[i][j])


def create_first_row(file):
    f = open(file, "r", encoding="utf8")
    lines = f.readlines()
    result = []
    for x in lines:
        #print(x.split())
        result.append(x.split())

    f.close()
    return result

#find phrase and return value for single line (for instance: str="1"), where phrase is 'str' and value is 1
def find_phrase(phrase):


    return val


def find_and_write_soul(file_, worksheet):
    print( "fun find_and_write_soul()" )
    file = open(file_, "r", encoding="utf8")
    lines = file.readlines()
    BUFFOR = 79
    COL_OFFSET = 4
    pos_val_start = 0
    str_to_end = ""
    _value = False

    for ROW, line in enumerate(lines):
        line = line[:-1]
        if ROW > BUFFOR:
            for COL in range(COL_OFFSET, len(FIRST_ROW_ARRAY[0]), 1):
                pos_var = line.find(FIRST_ROW_ARRAY[0][COL])

                if pos_var > 0:
                    #print(ROW , FIRST_ROW_ARRAY[0][COL])
                    #print(ROW,COL)
                    pos_val_start = pos_var+len(FIRST_ROW_ARRAY[0][COL])+2
                    if (FIRST_ROW_ARRAY[0][COL])[:-1] == '=':
                        pos_val_start = pos_var + len(FIRST_ROW_ARRAY[0][COL]) + 1
                    str_to_end = line[pos_val_start: (len(line)-1): 1]
                    _value = True

                if _value:
                    q = str_to_end.find('\"')
                    val = ""
                    if q > 0:
                        #print(str_to_end,q)
                        for i in range(q):
                            if(pos_val_start < len(line)):
                                val += line[pos_val_start]
                                #if line[pos_val_start] == '.':
                                    #val += ','
                            else:
                                val += "X"
                            pos_val_start = pos_val_start + 1
                        #print(val)
                        coma = val.find('.')
                        if val == '-1':
                            val = float(-1)
                        elif coma > 0:
                            val = float(val)
                            #print(val)
                        elif val.isdigit():
                            #print(val)
                            val = float(val)
                        #print(ROW + 1-BUFFOR, COL, val)
                        worksheet.write(ROW + 1-BUFFOR, COL, val)

    file.close()
    print( "end find_and_write_soul()" )


def find_and_write_v_soul(file_, worksheet):
    print( "fun find_and_write_v_soul()" )
    file = open(file_, "r", encoding="utf8")
    lines = file.readlines()
    BUFFOR = 79
    COL_OFFSET = 4
    pos_val_start = 0
    str_to_end = ""
    _value = False

    for ROW, line in enumerate(lines):
        line = line[:-1]
        if ROW > BUFFOR:
            for COL in range(1, COL_OFFSET, 1):
                pos_var = line.find(FIRST_ROW_ARRAY[0][COL])

                if pos_var > 0:
                    #print(ROW , FIRST_ROW_ARRAY[0][COL])
                    #print(ROW,COL)
                    pos_val_start = pos_var+len(FIRST_ROW_ARRAY[0][COL])+2
                    if (FIRST_ROW_ARRAY[0][COL])[:-1] == '=':
                        pos_val_start = pos_var + len(FIRST_ROW_ARRAY[0][COL]) + 1
                    str_to_end = line[pos_val_start: (len(line)-1): 1]
                    _value = True

                if _value:
                    q = str_to_end.find('\"')
                    val = ""
                    if q > 0:
                        #print(str_to_end,q)
                        for i in range(q):
                            if(pos_val_start < len(line)):
                                val += line[pos_val_start]
                                #if line[pos_val_start] == '.':
                                    #val += ','
                            else:
                                val += "X"
                            pos_val_start = pos_val_start + 1
                        #print(val)
                        coma = val.find('.')
                        if val == '-1':
                            val = float(-1)
                        elif coma > 0:
                            val = float(val)
                            #print(val)
                        elif val.isdigit():
                            #print(val)
                            val = float(val)
                        #print(ROW + 1-BUFFOR, COL, val)
                        worksheet.write(ROW + 1-BUFFOR, COL, val)
                        if COL == 1:
                            DESC_ARRAY.append(val)
    file.close()
    print( "end find_and_write_v_soul()" )


def find_and_write_desc(file_, worksheet):
    print( "fun find_and_write_desc()" )
    file = open(file_, "r", encoding="utf8")
    lines = file.readlines()
    BUFFOR = 79
    COL = 0
    pos_val_start = 0
    str_to_end = ""
    _value = False

    for ROW, name in enumerate(DESC_ARRAY):
        #print(name)
        for line in lines:
            line = line[:-1]
            pos_name = line.find(name)
            if pos_name > 0:
                cellCell = "</Cell><Cell>"
                pos_cell_end = line.find('</Cell></Row>')
                pos_cell_pre_start = line.find(cellCell)
                str = line[pos_cell_pre_start+len(cellCell): pos_cell_end: 1]
                #print("str: ", str)
                pos_cell_start = str.find(cellCell)
                cell = str[pos_cell_start+len(cellCell): len(str): 1]
                #print(cell)
                worksheet.write(ROW + 2, COL, cell)

    file.close()
    print( "end find_and_write_desc()" )


#######################################
print("start program")
workbook = create_workbook()

worksheet_soul = workbook.add_worksheet("soul")

FIRST_ROW_ARRAY = create_first_row(FILE_TEMPLATE)
create_headers(worksheet_soul)
find_and_write_soul(FILE_SOUL, worksheet_soul)
find_and_write_v_soul(FILE_V_SOUL, worksheet_soul)
find_and_write_desc(FILE_DESC, worksheet_soul)

workbook.close()
print("end program")