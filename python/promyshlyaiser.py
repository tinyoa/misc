# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 23:15:02 2022

@author: Sam
"""

import os
import sys


SRC_FOLDER = 'D:\\doc\\reps\\git_tinyoa\\misc\\python\\src\\'

def find_files(catalog, f):
    find_files = []
    for root, dirs, files in os.walk(catalog):
        find_files += [os.path.join(root, name) for name in files if name == f]
    return find_files

def files_in_catalog(catalog):
    find_files = []
    for root, dirs, files in os.walk(catalog):
        find_files += [os.path.join(root, name) for name in files]
    return find_files

# Проверю, что файлы выбираются
for item in files_in_catalog(SRC_FOLDER):
    #print(item)
    pass

# Проверить, что кодировка UTF-8 и если 1251, то изменить на UTF-8
#for script_file_path in files_in_catalog(SRC_FOLDER):
#    with open(script_file_path, 'r', encoding ='utf-8') as script_file:
# 

cp_1251_file_path = 'D:\\doc\\reps\\git_tinyoa\\misc\\python\\src\\'
try:
    with open(cp_1251_file_path, 'r', encoding='utf-8') as script_file:
        for line in script_file:
            print(line)
except UnicodeDecodeError as e:
    # Если не вышло, то кодируется
