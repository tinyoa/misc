#trying_parse


import requests
from bs4 import BeautifulSoup


# Отправляем GET-запрос на веб-страницу
url = 'http://parsinger.ru/2.1/DOM/index2.html'
# view-source:https://parsinger.ru/2.1/DOM/index2.html

response = requests.get(url)
response.encoding = 'utf-8'

# Проверяем статус-код ответа
if response.status_code == 200:
    
    # Инициализируем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ищем элемент с ID "text777"
    target_element = soup.find(id="text777")

    # Извлекаем текст из найденного элемента
    if target_element:
        extracted_text = target_element.text
        print(f"Извлеченный текст: {extracted_text}")  # Вывод на экран
    else:
        print("Элемент с ID 'text777' не найден.")
else:
    print(f"Не удалось получить доступ к странице, статус-код: {response.status_code}")




