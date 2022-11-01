# -*- coding: utf-8 -*-
"""
Created on Tue May 24 21:27:12 2022

@author: Sam

не может получить retailPlace
"""


import json

file = "extract_20220524.json"
DATA_PATH = 'D:/doc/финансы/чеки/'
outfile = 'json2csv.csv'


# считываю файл
with open(DATA_PATH + '/' + file, encoding = 'utf8') as read_file:
        lines = read_file.read()


decoded_hand = json.loads(lines)

header = 'cashTotalSum;dateTime;ecashTotalSum;fiscalDocumentNumber;fiscalDriveNumber;fiscalSign;items_name;items_nds18;items_price;items_quantity;items_sum;kktRegId;nds18;operationType;operator;receiptCode;requestNumber;shiftNumber;taxationType;totalSum;userInn;createdAt;timeLastAccess;retailPlace\n'

#print(decoded_hand)
#print(decoded_hand[0])
#print(decoded_hand[0]['ticket']['document']['receipt']['items'])

#dic_element = decoded_hand[0]
#items_element = dic_element['ticket']['document']['receipt']['items'][0]
#print(items_element['name'])

#iter_string = str(dic_element['ticket']['document']['receipt']['cashTotalSum']) + ';'
#iter_string = iter_string + dic_element['ticket']['document']['receipt']['dateTime'] + ';'
#iter_string = iter_string + str(dic_element['ticket']['document']['receipt']['ecashTotalSum']) + ';'
#iter_string = iter_string + str(dic_element['ticket']['document']['receipt']['fiscalDocumentNumber']) + ';'
#iter_string = iter_string + dic_element['ticket']['document']['receipt']['fiscalDriveNumber'] + ';'
#iter_string = iter_string + str(dic_element['ticket']['document']['receipt']['fiscalSign']) + ';'
#iter_string = iter_string + items_element['name'] + ';' 
            
            
try:
    lines = ''
    iter_cnt = 0
    # Перебор элементов словаря 
    for dic_element in decoded_hand:
        if 'receipt' in dic_element['ticket']['document']:
            for items_element in dic_element['ticket']['document']['receipt']['items']:
                iter_string = str(dic_element['ticket']['document']['receipt']['cashTotalSum']) + ';' \
                    + dic_element['ticket']['document']['receipt']['dateTime'] + ';' \
                    + str(dic_element['ticket']['document']['receipt']['ecashTotalSum']) + ';' \
                    + str(dic_element['ticket']['document']['receipt']['fiscalDocumentNumber']) + ';' \
                    + dic_element['ticket']['document']['receipt']['fiscalDriveNumber'] + ';' \
                    + str(dic_element['ticket']['document']['receipt']['fiscalSign']) + ';' \
                    + items_element['name'] + ';' 
                if 'nds18' in items_element:
                    iter_string = iter_string + str(items_element['nds18'])
                iter_string = iter_string + ';'
                iter_string = iter_string + str(items_element['price']) + ';' \
                    + str(items_element['quantity']) + ';' \
                    + str(items_element['sum']) + ';' \
                    + dic_element['ticket']['document']['receipt']['kktRegId'] + ';' 
                if 'nds18' in dic_element['ticket']['document']['receipt']:
                    iter_string = iter_string + str(dic_element['ticket']['document']['receipt']['nds18'])
                iter_string = iter_string + ';'
                iter_string = iter_string \
                    + str(dic_element['ticket']['document']['receipt']['operationType']) + ';' 
                if 'operator' in dic_element['ticket']['document']['receipt']:
                    iter_string = iter_string + dic_element['ticket']['document']['receipt']['operator']
                iter_string = iter_string + ';'
                if 'receiptCode' in dic_element['ticket']['document']['receipt']:
                    iter_string = iter_string + str(dic_element['ticket']['document']['receipt']['receiptCode'])
                iter_string = iter_string + ';'
                if 'requestNumber' in dic_element['ticket']['document']['receipt']:
                    iter_string = iter_string + str(dic_element['ticket']['document']['receipt']['requestNumber'])
                iter_string = iter_string + ';'
                if 'shiftNumber' in dic_element['ticket']['document']['receipt']:
                    iter_string = iter_string + str(dic_element['ticket']['document']['receipt']['shiftNumber'])
                iter_string = iter_string + ';'
                if 'taxationType' in dic_element['ticket']['document']['receipt']:
                    iter_string = iter_string + str(dic_element['ticket']['document']['receipt']['taxationType'])
                iter_string = iter_string + ';'
                if 'totalSum' in dic_element['ticket']['document']['receipt']:
                    iter_string = iter_string + str(dic_element['ticket']['document']['receipt']['totalSum'])
                iter_string = iter_string + ';'
                if 'userInn' in dic_element['ticket']['document']['receipt']:
                    iter_string = iter_string + dic_element['ticket']['document']['receipt']['userInn']
                iter_string = iter_string + ';'
                if 'createdAt' in items_element:
                    iter_string = iter_string + dic_element['createdAt']
                iter_string = iter_string + ';'
                if 'timeLastAccess' in items_element:
                    iter_string = iter_string + dic_element['timeLastAccess'] 
                iter_string = iter_string + ';'
                if 'retailPlace' in items_element:
                    iter_string = iter_string + dic_element['retailPlace'] 
                lines = lines + iter_string + '\n'
        if 'bso' in dic_element['ticket']['document']:
            for items_element in dic_element['ticket']['document']['bso']['items']:
                iter_string = str(dic_element['ticket']['document']['bso']['cashTotalSum']) + ';' \
                    + dic_element['ticket']['document']['bso']['dateTime'] + ';' \
                    + str(dic_element['ticket']['document']['bso']['ecashTotalSum']) + ';' \
                    + str(dic_element['ticket']['document']['bso']['fiscalDocumentNumber']) + ';' \
                    + dic_element['ticket']['document']['bso']['fiscalDriveNumber'] + ';' \
                    + str(dic_element['ticket']['document']['bso']['fiscalSign']) + ';' \
                    + items_element['name'] + ';' 
                if 'nds18' in items_element:
                    iter_string = iter_string + str(items_element['nds18'])
                iter_string = iter_string + ';'
                iter_string = iter_string + str(items_element['price']) + ';' \
                    + str(items_element['quantity']) + ';' \
                    + str(items_element['sum']) + ';' \
                    + dic_element['ticket']['document']['bso']['kktRegId'] + ';' 
                if 'nds18' in dic_element['ticket']['document']['bso']:
                    iter_string = iter_string + str(dic_element['ticket']['document']['bso']['nds18'])
                iter_string = iter_string + ';'
                iter_string = iter_string \
                    + str(dic_element['ticket']['document']['bso']['operationType']) + ';' 
                if 'operator' in dic_element['ticket']['document']['bso']:
                    iter_string = iter_string + dic_element['ticket']['document']['bso']['operator']
                iter_string = iter_string + ';'
                if 'receiptCode' in dic_element['ticket']['document']['bso']:
                    iter_string = iter_string + str(dic_element['ticket']['document']['bso']['receiptCode'])
                iter_string = iter_string + ';'
                if 'requestNumber' in dic_element['ticket']['document']['bso']:
                    iter_string = iter_string + str(dic_element['ticket']['document']['bso']['requestNumber'])
                iter_string = iter_string + ';'
                if 'shiftNumber' in dic_element['ticket']['document']['bso']:
                    iter_string = iter_string + str(dic_element['ticket']['document']['bso']['shiftNumber'])
                iter_string = iter_string + ';'
                if 'taxationType' in dic_element['ticket']['document']['bso']:
                    iter_string = iter_string + str(dic_element['ticket']['document']['bso']['taxationType'])
                iter_string = iter_string + ';'
                if 'totalSum' in dic_element['ticket']['document']['bso']:
                    iter_string = iter_string + str(dic_element['ticket']['document']['bso']['totalSum'])
                iter_string = iter_string + ';'
                if 'userInn' in dic_element['ticket']['document']['bso']:
                    iter_string = iter_string + dic_element['ticket']['document']['bso']['userInn']
                iter_string = iter_string + ';'
                if 'createdAt' in items_element:
                    iter_string = iter_string + dic_element['createdAt']
                iter_string = iter_string + ';'
                if 'timeLastAccess' in items_element:
                    iter_string = iter_string + dic_element['timeLastAccess'] 
                iter_string = iter_string + ';'
                if 'retailPlace' in items_element:
                    iter_string = iter_string + dic_element['retailPlace'] 
                lines = lines + iter_string + '\n'
    lines = header + lines[:-1]
    
    
    outfile = 'json2csv.csv'
    with open(DATA_PATH + '/' + outfile, "w",encoding = 'utf8') as write_file:
            write_file.write(lines)
            

except Exception as e:
    #print ("I am unable to connect to the database")
    print(e.__class__)
    print(e)
    #print(step)
    print(lines)
    print(dic_element)
finally:
    pass






