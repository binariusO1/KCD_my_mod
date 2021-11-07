import xlsxwriter

PATH_VAL = "Data/Libs/Tables/item/"

HASH_LIST_INPUT = "find_hash_and_return_lines_with_hash_input.txt"
FILE_INPUT = "equippable_item.xml"
SCRIPT_OUTPUT = "find_hash_and_return_lines_with_hash_output"
SCRIPT_OUTPUT_TXT = ".txt"

HASH_LIST = []
OUTPUT_LINES = []

def read_hash(file_name):
    print("def read_hash()")
    file = open(file_name, "r", encoding="utf8")

    lines = file.readlines()
    for hash in lines:
        hash = hash[0: 36: 1]

        HASH_LIST.append(hash)

    file.close()


def read(file_name):
    print("def read()")
    file = open(file_name, "r", encoding="utf8")
    file_output = open(SCRIPT_OUTPUT+SCRIPT_OUTPUT_TXT, "w")

    lines = file.readlines()

    for hash in HASH_LIST:

        if hash == "":
            file_output.write('\n')
            continue

        for line in lines:
            line = line[:-1]

            find_num = line.find(hash)
            if find_num > 0:
                print(line)
                OUTPUT_LINES.append(line)
                file_output.write(line+'\n')
                break

    file.close()
    file_output.close()
    return ""


def delete_rows(FILE_INPUT):
    with open(FILE_INPUT, "r", encoding="utf8") as f:
        lines = f.readlines()
    with open(FILE_INPUT, "w", encoding="utf8") as f:
        flag = False
        for line in lines:
            for outputLine in OUTPUT_LINES:
                if line[:-1] == outputLine:
                    flag = True
                    break

            if not flag:
                f.write(line)
            flag = False

# --------------------------
print("wybierz plik docelowy w Data/Libs/Tables/item/ :")
print("1) equippable_item.xml")
print("2) armor.xml")
print("3) pickable_item.xml")
print("4) nazwa pliku bezpośrednio w folderze")
YN = input()
if YN == "1":
    FILE_INPUT = "equippable_item.xml"
    read_hash(HASH_LIST_INPUT)
    read(PATH_VAL+FILE_INPUT)
    delete_rows(PATH_VAL+FILE_INPUT)
    print("z pliku  Data/Libs/Tables/item/ " + FILE_INPUT + "zostały usunięte linie zawierające hashe:")
    print("w folderze ze skryptem jest output, który nalezy wkleić w odpowiednie miejsce w tym pliku")
elif YN == "2":
    FILE_INPUT = "armor.xml"
    read_hash(HASH_LIST_INPUT)
    read(PATH_VAL+FILE_INPUT)
    delete_rows(PATH_VAL+FILE_INPUT)
    print("z pliku  Data/Libs/Tables/item/ " + FILE_INPUT + "zostały usunięte linie zawierające hashe:")
    print("w folderze ze skryptem jest output, który nalezy wkleić w odpowiednie miejsce w tym pliku")
elif YN == "3":
    FILE_INPUT = "pickable_item.xml"
    read_hash(HASH_LIST_INPUT)
    read(PATH_VAL+FILE_INPUT)
    delete_rows(PATH_VAL+FILE_INPUT)
    print("z pliku  Data/Libs/Tables/item/ " + FILE_INPUT + "zostały usunięte linie zawierające hashe:")
    print("w folderze ze skryptem jest output, który nalezy wkleić w odpowiednie miejsce w tym pliku")
elif YN == "4":
    FILE_INPUT = input()
    read_hash(HASH_LIST_INPUT)
    read(FILE_INPUT)
    print("w folderze ze skryptem jest output, który nalezy wkleić w odpowiednie miejsce w tym pliku")
else:
    print("Inny znak, anulowano")

input()