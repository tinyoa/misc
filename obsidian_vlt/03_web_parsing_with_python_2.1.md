

Пример
```
<!DOCTYPE html> <html> <head> <meta charset="UTF-8"> <title>Интернет-магазин</title> <style> /* CSS для оформления карточки товара */ .product-card { border: 1px solid #ccc; padding: 15px; width: 300px; } .product-title { font-size: 1.2em; } .product-price { color: #e44d26; } </style> </head> <body> <h1>Каталог товаров</h1> <!-- Карточка товара --> <div class="product-card" id="product-1"> <h2 class="product-title">Название товара</h2> <img src="product-image.jpg" alt="Изображение товара" width="100"> <p class="product-description">Описание товара, которое подробно расскажет о его характеристиках.</p> <p class="product-price">Цена: 1000 руб.</p> <button type="button" onclick="addToCart('product-1')">Добавить в корзину</button> </div> </body> 
</html>
```

В данном примере:

- `<title>` задаёт название веб-страницы, отображаемое в вкладке браузера.
- В разделе `<style>` прописаны CSS-правила для оформления карточки товара, но чаще всего они стили располагаются в отдельном файле.
- Карточка товара оформлена в теге `<div>` с классом `product-card` и уникальным идентификатором `id="product-1"`.
- `<h2>` используется для указания названия товара, и этому тегу присвоен класс `product-title`.
- Тег `<img>` отображает изображение товара. Атрибуты `src` и `alt` задают путь к изображению и альтернативный текст соответственно.
- `<p>` с классом `product-description` и `product-price` используются для отображения описания и цены товара.
- Кнопка "Добавить в корзину" реализована с помощью тега `<button>`, атрибут `onclick` которого запускает JavaScript-функцию `addToCart`.
