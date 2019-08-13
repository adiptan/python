import os
import glob
import datetime

files=["tst.log","HRS_RT_current.log"]
logSize=1000000
countOfFiles=5

#функция переименовывает файл и конкатинирует дату с именем
def rename_all(name):
    for file in files:
        if os.path.getsize(file) > logSize:
            t=datetime.datetime.today().strftime("%d%m%Y_%H%M%S")
            if os.path.isfile(file):
                ren=os.rename(file, filePreparing(file)+"_"+t+".arch")
                createFile(file)
                delOldFile(file)
        else:
            continue

def createFile(trueFileName):
    f=open(trueFileName, "w+")
    f.close

def filePreparing(fileForPrep):
    end_index = fileForPrep.find(".") # нужно найти индекс символа "."в имени файла. Это нужно чтобы использовать для переименования без расширения файла.
    newFileName = fileForPrep[0:end_index] # берётся диапазот индексов от 0 до символа "." и дальше эта переменная используется в переименовании.
    return(newFileName)

def delOldFile(name):
    list=[]
    for itfile in glob.glob(filePreparing(name)+"_*"):
        list.append(itfile)
    sorted(list)
    while len(list) > countOfFiles:
        os.remove(list[0])
        print("Удаляется файл "+list[0])
        del list[0]

rename_all(files)
