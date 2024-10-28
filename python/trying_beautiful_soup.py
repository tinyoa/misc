# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 21:28:56 2024

@author: Sam
"""

from bs4 import BeautifulSoup
import requests

site_url_list = ['https://parsinger.ru/2.1/DOM/example.html',
                 'https://parsinger.ru/2.1/DOM/index.html',
                 'https://parsinger.ru/html/hdd/4/4_17.html', 
                 'https://parsinger.ru/html/index5_page_1.html#5_1',
                 'http://parsinger.ru/html/index4_page_1.html']

site_url = 'https://parsinger.ru/2.1/DOM/example.html'
print(f'site_url: {site_url}')
# Получаем содержимое веб-страницы
response = requests.get(site_url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# Комбинированный поиск: ищем все абзацы с классом "my_class" и атрибутом "data-example"
paragraphs = soup.select('p.my_class[data-example]')
print(f'selector: p.my_class[data-example]')
# Выводим найденные элементы
for p in paragraphs:
    print(f'Найденный элемент: {p.text}')

# ищем все абзацы с классом "my_class"   
paragraphs = soup.select('p.my_class')
print(f'selector: p.my_class')
# Выводим найденные элементы
for p in paragraphs:
    print(f'Найденный элемент: {p.text}')

# ищем все абзацы с атрибутом "data-example"
paragraphs = soup.select('p.my_class[data-example]')
print(f'selector: p.[data-example]')
# Выводим найденные элементы
for p in paragraphs:
    print(f'Найденный элемент: {p.text}')
    
# ищем все абзацы с атрибутом "data-example"
paragraphs = soup.select('p')
print(f'selector: p')
# Выводим найденные элементы
for p in paragraphs:
    print(f'Найденный элемент: {p.text}')    



print('\n\n')
site_url = site_url_list[1]         # 'https://parsinger.ru/2.1/DOM/index.html'
print(f'-- -- site_url: {site_url}')
response = requests.get(site_url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# ищем заголовок
soup_selector_string = 'h2.product-title'
paragraphs = soup.select(soup_selector_string)
print(f'-- selector: {soup_selector_string}')
# Выводим найденные элементы
for p in paragraphs:
    print(f'Найденный элемент: {p.text}')

# ищем заголовки
soup_selector_string = 'h2'
paragraphs = soup.select(soup_selector_string)
print(f'-- selector: {soup_selector_string}')
# Выводим найденные элементы
for p in paragraphs:
    print(f'Найденный элемент: {p.text}')

# ищем кнопку
soup_selector_string = 'button'
paragraphs = soup.select(soup_selector_string)
print(f'-- selector: {soup_selector_string}')
# Выводим найденные элементы
for p in paragraphs:
    print(f'Найденный элемент: {p.text}')
    

# ищем по ид
soup_selector_string = '#product-1'
paragraphs = soup.select(soup_selector_string)
print(f'-- selector: {soup_selector_string}')
# Выводим найденные элементы
for p in paragraphs:
    print(f'Найденный элемент: {p.text}')





print('\n\n')
site_url = site_url_list[2]         # 'https://parsinger.ru/2.1/DOM/index.html'
print(f'-- -- site_url: {site_url}')
response = requests.get(site_url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')


# ищем бренд по ID
soup_selector_string = '#brand'
paragraphs = soup.select(soup_selector_string)
print(f'-- selector: {soup_selector_string}')
# Выводим найденные элементы
for p in paragraphs:
    print(f'Найденный элемент: {p.text}')


# ищем бренд по ID
soup_selector_string = "[id='brand']"
paragraphs = soup.select(soup_selector_string)
print(f'-- selector: {soup_selector_string}')
# Выводим найденные элементы
for p in paragraphs:
    print(f'Найденный элемент: {p.text}')


# Пробую завернуть итерацию по элементам
def print_iterate_over_elements_by_selector(soup, soup_selector_string):
    elements = soup.select(soup_selector_string)
    print(f'\n-- selector: {soup_selector_string}')
    # Выводим найденные элементы
    for p in elements:
        print(f'Найденный элемент: {p.text}')



print('\n\n')
site_url = site_url_list[3]         # 'https://parsinger.ru/html/index5_page_1.html#5_1'
print(f'-- -- site_url: {site_url}')
response = requests.get(site_url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

print_iterate_over_elements_by_selector(soup, '.item_card .name_item')



print('\n\n')
site_url = site_url_list[4]         # 'http://parsinger.ru/html/index4_page_1.htmls'
print(f'-- -- site_url: {site_url}')
response = requests.get(site_url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

print_iterate_over_elements_by_selector(soup, '[class="item"] [class="name_item"]')

print_iterate_over_elements_by_selector(soup, 'div p')

# параграфы, являющиеся прямыми наследниками дивов
print_iterate_over_elements_by_selector(soup, 'div > p')

print_iterate_over_elements_by_selector(soup, '[type="text"]')

print_iterate_over_elements_by_selector(soup, '[class="name_item"], div > div > p')



