import os
import pprint as pp
import pandas as pd
import datetime
import time
import openpyxl
# Files_Dir - сканирование файлов из заданной папки включая вложенные папки.
# Получение пути, имени файла, расширения и размера, а также даты изменения.
# Запись результата в EXCEL файл

def listdirs(rootdir, ListFiles):
    # global ListFiles

    for it in os.scandir(rootdir):
        if it.is_dir() == False:
            # print(it.path)

            split_ = os.path.split(it.path)
            splitext_ = os.path.splitext(it.path)
            mtime = os.path.getmtime(it.path)
            mtime_readable = datetime.date.fromtimestamp(mtime)
            ListFiles.append(it.path.__str__() + ';' + split_[0] + ';' + split_[1] + ';' + splitext_[1] +
                             ';' + str(os.path.getsize(it.path)) + ';' + str(mtime_readable))
        if it.is_dir():
            print(it.path)
            listdirs(it, ListFiles)
    # return myList


rootdir = 'c:\\Work'
ListFiles = list()
listdirs(rootdir, ListFiles)

# pp.pprint(ListFiles)
df = pd.DataFrame(ListFiles, columns=["First"])
excel_file_path = "output5.xlsx"
df.to_excel(excel_file_path, index=False)
