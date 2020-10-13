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
    sourceDir = inf.readline()
    targetDir = inf.readline()
    for line in inf:
        files_to_copy.append(line.strip())

print(files_to_copy)

