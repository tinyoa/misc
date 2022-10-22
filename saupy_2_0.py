# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 13:15:03 2021

@author: Sam


2.0 Убираю ненужные части
"""


import pandas as pd
import pyodbc
import time
import teradata
import datetime
from datetime import datetime
import inspect


APP_NAME = 'sau_etl'
APP_VER = '2.0'
DATA_CATALOG = ''
TERADATA_DSN = 'td'


class conn_td():
    def __enter__(self):
        self.conn = pd.connect(method = 'ODBC', DSN = TERADATA_DSN)
        return self.conn
    def __exit__(self, type, value, traceback):
        self.conn.close()
        print("Connection " + TERADATA_DSN + " is closed")

class conn_teradata():
    def __enter__(self):
	    self.conn = pyodbc.connect('DRIVER=' + TERADATA_DSN + ';DATABASE=DBO')


def info():
    print('APP_NAME: ', APP_NAME)
    print('APP_VER: ', APP_VER)
    print('DATA_CATALOG: ', DATA_CATALOG)
    print('TERADATA_DSN: ', TERADATA_DSN)

def print_log(log_message, file_name = APP_NAME + '.log'):
    with open(file_name, 'a') as flog:
	    flog.write(str(time.strftime("%Y:%m:%d %H:%M:%S")) + ' ' + '; ' + log_message + '\n')
    print(log_message);
    return

             
# строковая функция. Берет amount символов слева строки s
def left(s, amount):
    return s[:amount]
	
# строковая функция. Берет amount символов справа строки s
def right(s, amount):
    return s[-amount:]

# строковая функция. Берет amount символов справа строки s, начиная с позиции offset
def mid(s, offset, amount):
    return s[offset:offset+amount]                   

# Возвращает датафрейм с результатом запроса query. Выполняется на боевом сервере
def tera_query(query, DSN = ''):
    # Если DSN не указан, то использовать боевой сервере
	if DSN == '':
	    DSN = TERADATA_DSN
	sql = query
	
	udaExec = teradata.UdaExec(appName = APP_NAME, version=APP_VER
	    , logConsole = False, logLevel="ERROR")
	session = udaExec.connect(method='odbc', DSN = DSN)
	
	df = pd.DataFrame()
	df = pd.read_sql_query(sql, session)
	session.close()
	return df



# уснуть на hours минут
def delay_h(hours):
    time.sleep(hours * 60 * 60)

# уснуть на hours минут	
def delay_h(minutes):
    time.sleep(minutes * 60)






                                
