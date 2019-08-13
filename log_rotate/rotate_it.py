import os
import glob
import datetime

files=["tst.log","HRS_RT_current.log"]
logSize=1000000

#функция переименовывает файл и конкатинирует дату с именем
def rename_all(name):
    for file in files:
        if os.path.getsize(file) > logSize:
            t=datetime.datetime.today().strftime("%d%m%Y_%H%M%S")
            end_index = file.find(".") # нужно найти индекс символа "."в имени файла. Это нужно чтобы использовать для переименования без расширения файла.
            newFileName = file[0:end_index] # берётся диапазот индексов от 0 до символа "." и дальше эта переменная используется в переименовании.
            if os.path.isfile(file):
                ren=os.rename(file, newFileName+"_"+t+"tst"+".arch")
                createFile(file)
                delOldFile(file)
            else:
                createFile(file)
                delOldFile(file)
        else:
            continue

def createFile(trueFileName):
    f=open(trueFileName, "w+")
    f.close

def delOldFile(name):
    end_index = name.find(".")
    newFileName = name[0:end_index]
    list=[]
    for itfile in glob.glob(newFileName+"_*"):
        list.append(itfile)
    sorted(list)
    while len(list) > 5:
        os.remove(list[0])
        print("Удаляется файл "+list[0])
        del list[0]

rename_all(files)
