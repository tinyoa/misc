# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 20:20:14 2020

@author: Sam

Копировать указанные файлы в указанную директорию
Изменить кодировку с одной на другую


_Файл с настройками:_
путь источника
путь приемника
направление конвертирования
список файлов для обработки
"""


#Файл с настройками
# Прочесть файл
# 


files_to_copy = []

with open('copier.cop') as inf:
    sourceDir = inf.readline().strip()
    targetDir = inf.readline().strip()
    for line in inf:
        files_to_copy.append(line.strip())

print('sourceDir', sourceDir)
print('targetDir', targetDir)
print(files_to_copy)

# По очереди открывать файлы из списка и сохранять их в другом месте

filename = files_to_copy[0]
with open(sourceDir + '/' + filename, 'r', encoding="cp1251") as src_f:
    with open(targetDir + '/' + filename, 'w', encoding="utf-8-sig") as trg_f:
         for line in src_f:
             print(line)
             #trg_f.write(line.decode('cp1251').encode('utf8'))
             trg_f.write(line)

#f = file("utf8.html", "wb")
#for line in file("cp1251.html", "rb"):
#    f.write(line.decode('cp1251').encode('utf8'))



