# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 23:15:02 2022

@author: Sam
"""

import os
import sys
import codecs

SRC_FOLDER = 'D:\\doc\\reps\\git_tinyoa\\misc\\python\\to_conv'
#SRC_FOLDER = 'D:\doc\reps\git_tinyoa\misc\python\to_conv'

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
    print(item)
    pass


# Перекодировать файл file, сохранить как <filename><_utf8>
def convert_ansi_utf8bommmm(filepath):
    sep='\\'
    filename = filepath.split(sep)[-1:][0]
    parpath = sep.join(filepath.split(sep)[:-2])+ sep
    outfile = parpath + filename
    
    block_size = 1045876
    with codecs.open(filepath,'r', encoding='mbcs') as source_file:
        with codecs.open(outfile, 'w', encoding='utf-8-sig') as target_file:
            while True:
                contents = source_file.read(block_size)
                if not contents:
                    break
                target_file.write(contents)
                
    print(filename)
    print(parpath)
    print(outfile)
    
    return

# Не рабочая Перекодировать файл file, сохранить как <filename><_utf8>
def win2utf(filename, postfix = '_utf8'):
    
    #Как-то придумать название для нового файла
    f_out_extension = filename.split('.')[-1:][0]
    print('f_out_extension: ', f_out_extension)
    f_out_name = '.'.join(filename.split('.')[:-1]) \
            + postfix \
            + '.' \
            + f_out_extension
    print('f_out_name: ', f_out_name)
    #Открыть два файла 
    
    with codecs.open(filename, 'r', encoding = 'cp1252') as f_out \
            , codecs.open(f_out_name, 'wb') as f_in: 
        for line in f_out:
            print(';', line)
            #print(';', line.encode('cp1250').decode('utf-8'))
            #print(';', line.decode('cp1250').encode('utf-8') )
            #print(';', line.decode('utf-8'))
            print(';', line.encode('utf-8'))
            print('- -'*20)
            f_in.write(line.encode('utf-8'))



# Проверить, что кодировка UTF-8 и если 1251, то изменить на UTF-8
#for script_file_path in files_in_catalog(SRC_FOLDER):
#    with open(script_file_path, 'r', encoding ='utf-8') as script_file:

cp_1251_file_path = SRC_FOLDER  #'D:\\doc\\reps\\git_tinyoa\\misc\\python\\src\\'

files = files_in_catalog(SRC_FOLDER)

try:
    for fil in files:
        with open(fil, 'r', encoding='utf-8') as script_file:
            for line in script_file:
                print(line)
except UnicodeDecodeError as e:
    # Если не вышло, то кодируется
    win2utf(fil)
    print ('bad file')
    print(e.__class__)
    pass




