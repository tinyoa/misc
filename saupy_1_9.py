# saupy_1_9.py

# 1.5   Изменение процедуры update_place_passport. Убраны задвои. Берется первая запись.
# 1.6   добавлена функция сохраняющая месяцы v_months
#   get_cur_monthid
#   get_month_first_dt
#   get_month_last_dt
#   get_week_first_dt
#   get_week_last_dt
# 1.7   функция tera_exec_file(file_path)    выполняющая файл sql на терадате
# 1.8   добавлена функция tera_query_file(file_path, out_path = '', output_name = 'output') выполняющая файл sql, находящийся по пути file_path на терадате. Если запрос начинается с SELECT, то результат сохраняется в папку out_path (если out_path не зада, то в папку с запросом) под именем 'output_name_<номер запроса в файле>.csv' (значение по-умолчанию: 'output').
# 1.81  В tera_query_file split(' ') заменен на split() для повышения универсальности.
#      datetime.datetime.today() заменено на datetime.today()
# 1.9   Перейти к сессиям-объектам, чтобы избежать повисания сессий

import pandas as pd
import pyodbc
import time
import teradata
import datetime
from datetime import datetime
import inspect

APP_NAME = 'merch_etl'
APP_VER = '1.9'
DATA_CATALOG = 'R:/Департамент аналитики/Отдел анализа эффективности торгового пространства/Самоквитов АЮ/справочники/'
TERADATA_DSN = 'teradata'
TVA_DSN = 'tdtva'
TDDEV_DSN = 'tddev'
DEFAULT_WHS = 24409   #; Актинолит


def info():
    print('APP_NAME: ', APP_NAME)
    print('APP_VER: ', APP_VER)
    print('DATA_CATALOG: ', DATA_CATALOG)
    print('TERADATA_DSN: ', TERADATA_DSN)
    print('TVA_DSN: ', TVA_DSN)
    print('TDDEV_DSN: ', TDDEV_DSN)
    print('DEFAULT_WHS: ', DEFAULT_WHS)
	
def print_log(log_message, file_name = APP_NAME + '.log'):
    with open(file_name, 'a') as flog:
	    flog.write(str(time.strftime("%Y:%m:%d %H:%M:%S")) + ' ' + '; ' + log_message + '\n')
    print(log_message);
    return

	
# hp2_print_log(project_name = 'DUMMY PROJECT', comment = 'DUMMY COMMENT') Записывает в таблицу лога [dbo].[T_SERV_LOG] hyper-prod2 комментарий comment к проекту project_name
def hp2_print_log(project_name = 'DUMMY PROJECT, comment = 'DUMMY COMMENT', printlog = False):
    if printlog:
        print_log(project_name + '|' + comment)
    try:
        with pyodbc.connect('DRIVER={SQL SERVER}; SERVER=HYPER-PROD2;DATABASE=DPSP_ANALYTICS') as cnxn:
            cursor = cnxn.cursor()
            cursor.execute("exec DPSP_ANALYTICS.[dbo].[P_PRINT_LOG] '{}', '{}'".format(project_name, comment))
            cursor.commit()
    except Exception as e:
        print_log(str(e.__class__) + str(e))
        print_log(project_name + '|' + comment)		

def hp2_query(query = ''):
    with pyodbc.connect('DRIVER={SQL SERVER}; SERVER=HYPER-PROD2;DATABASE=DPSP_ANALYTICS') as cnxn:
        cursor = cnxn.cursor()
        cursor.execute("exec DPSP_ANALYTICS.[dbo].[P_PRINT_LOG] '{}', '{}'".format(project_name, comment))
        cursor.commit()

# Классы подключений от Андрея
class conn_hp2():
    def __enter__(self):
	    self.conn = p.connect('DRIVER = {SQL Server}; SERVER=hyper-prod2;DATABASE=dpsp_analytics')
		return self.conn
	def __exit__(self, type, value, traceback):
	    self.conn.close()
		print("Connection hyper-prod2 is closed")

class conn_hyper():
    def __enter__(self):
	    self.conn = p.connect('DRIVER = {SQL Server}; SERVER=hyper;DATABASE=TSO')
		return self.conn
	def __exit__(self, type, value, traceback):
	    self.conn.close()
		print("Connection hyper is closed")
		
class conn_tva():
    def __enter__(self):
	    self.conn = p.connect(method = 'ODBC', DSN = TVA_DSN)
		return self.conn
	def __exit__(self, type, value, traceback):
	    self.conn.close()
		print("Connection " + TVA_DSN + " is closed")

class conn_teradata():
    def __enter__(self):
	    self.conn = pyodbc.connect('DRIVER=' + TERADATA_DSN + ';DATABASE'
		
		
# строковая функция. Берет amount символов слева строки s
def left(s, amount):
    return s[:amount]
	
# строковая функция. Берет amount символов справа строки s
def right(s, amount):
    return s[-amount:]

# строковая функция. Берет amount символов справа строки s, начиная с позиции offset
def mid(s, offset, amount):
    return s[offset:offset+amount]
		
# Функция возвращает week_id_2 текущей недели
def get_cur_weekid2():
    date = str(datetime.today().year) + '-' right('0' + str(datetime.today().month(), 2) + '-' right('0' + str(datetime.today().day(), 2)
	df_vdays = pd.read_csv(DATA_CATALOG + 'v_days.csv', engine = 'python', sep=';', encoding = 'cp1251')
	weekid2 = df_vdays.loc[df_vdays['DAY_ID'] == date].WEEK_ID_2.astype('int32').values[0]
	return weekid2
	
# Возвращает первую дату указанной недели
def get_week_first_dt(week_id2):
    df_vweeks = pd.read_csv(DATA_CATALOG + 'v_weeks.csv', engine = 'python', sep = ';', encoding = 'cp1251')
	day_id = df_vweeks.loc[df_vweeks['WEEK_ID_2']==week_id2].WEEK_FIRST_DT.values[0]
	return day_id
	
# Возвращает первую дату указанной недели
def get_week_last_dt(week_id2):
    df_vweeks = pd.read_csv(DATA_CATALOG + 'v_weeks.csv', engine = 'python', sep = ';', encoding = 'cp1251')
	day_id = df_vweeks.loc[df_vweeks['WEEK_ID_2']==week_id2].WEEK_LAST_DT.values[0]
	return day_id
	
	
	
	
	
# Возвращает датафрейм с результатом запроса query. Выполняется на боевом сервере
def tera_query(query, DSN = ''):
    # Если DSN не указан, то использовать боевой сервере
	if DSN = '':
	    DSN = TERADATA_DSN
	sql = query
	
	udaExec = teradata.UdaExec(appName = APP_NAME, version=APP_VER
	    , logConsole = False, logLevel="ERROR")
	session = udaExec.connect(method='odbc', DSN = DSN)
	
	df = pd.DataFrame()
	df = pd.read_sql_query(sql, session)
	session.close()
	return df
	
# Возвращает датафрейм с результатом запроса query. Выполняется на сервере аналитики
def tva_query(query):
    return tera_query(query, DSN = TVA_DSN)
	
# Выполняет запрос находящийся в файле file_path (полный путь к файлу). Выполняется через DSN 'teradata'
def tera_exec_file(file_path, DSN = ''):
    if DSN == '':
        DSN = TERADATA_DSN
    
    udaExec = teradata.UdaExec(appName = APP_NAME, version = APP_VER
        , logConsole = False, logLevel = "ERROR")
    sessoin = udaExec.connect(method = 'odbc', DSN = DSN)
    session.execute(file = file_path)
    session.close()

# Выполняет запрос находящийся по пути file_path на терадате. Если запрос начинается с SELECT, то результат сохраняется в папку out_path (если out_path не зада, то в папку с запросом) под именем 'output_name_<номер запроса в файле>.csv' (значение по-умолчанию: 'output').
def tera_query_file(file_path, out_path = '', output_name = 'output', DSN = ''):
    if DSN == '':
	    DSN = TERADATA_DSN
	udaExec = teradata.UdaExec(appName = APP_NAME, version = APP_VER
	    , logConsole = False, logLevel = "ERROR")
	session = udaExec.connect(method='odbc', DSN = DSN)
	
	if out_path == '':
	    out_path = '/'.join(query_path3.split('/')[:-1])
		
	# чтение файла file_path
	with open(query_path3, encoding = 'utf8') as fquery:
	    s = fquery.read()
	
	# разбивка строки на список запросов разделителем ";"
	query_list = s.split(';')
	query_num = 0
	for query in query_list:
	    # очищаю запрос от управляющих символов (strip), разбиваю на слова пробелами (split), 
		#  беру первое слово, перевожу его в верхний регистр (upper) и сравниваю его со словом 'SELECT'
	    if query.strip().split()[0].upper() == 'SELECT':
		    df = pd.DataFrame()
			df = pd.read_sql_query(query + ';', session)
			df.to_csv(out_path + '/' + output_name + '_' + str(query_num) + '.csv', sep = ';')
		else:
		    session.execute(query + ';')
		query_num += 1
	session.close()
	
# уснуть на hours минут
def delay_h(hours):
    time.sleep(hours * 60 * 60)

# уснуть на hours минут	
def delay_h(minutes):
    time.sleep(minutes * 60)












	


