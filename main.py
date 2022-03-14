import os
import shutil as s


def scan(source, target, sep):
    client_code = []
    source_scan = os.scandir(source)

    for files in source_scan:
        temp = files.name
        temp = temp.split(sep, 1)
        temp = temp[1].rsplit('.', 1)
        client_code.append(temp[0])

    iterator = 0
    for itens in client_code:
        if os.path.exists(target+client_code[iterator]):
            iterator += 1
        else:
            os.mkdir(target + client_code[iterator])
            iterator += 1

    control = 0
    source_scan = os.scandir(source)
    for tries in source_scan:
        s.copy(source + tries.name, target + client_code[control])
        control += 1


def delete(target):
    target_scan = os.scandir(target)
    for folder in target_scan:
        folder2 = os.scandir(target+folder.name)
        for file in folder2:
            try:
                os.remove(os.path.join(target, folder.name,file))
            except Exception as e:
                print(file)
                print(f"O diretório'{target+folder.name}'possui uma pasta, ela não pode ser excluída por este script")


path = ''
path2 = ''
separator = ''

if len(path) == 0:
    while not os.path.exists(path):
        path = input("Por favor insira um Caminho de pasta raíz válida: \n")

if len(path2) == 0:
    while not os.path.exists(path):
        path2 = input("Por favor insira um Caminho de pasta alvo válida: \n")

if len(separator) == 0:
    separator = input("Por favor insira o sepadaor: \n")

select = input("1 - Para copiar arquivos\n2 - Para limpar as pastas\n")

if select == '1':
    scan(path, path2, separator)
elif select == '2':
    delete(path2)

