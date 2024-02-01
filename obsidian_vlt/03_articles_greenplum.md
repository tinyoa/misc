

## Полезный код Greenplum

Получить размеры таблиц
```
select
    n.nspname
    , n.nspname || '.' c.relname  as relation
    , c relowner
    , c.relhasoids
    , r.rolname
    , pg_size_pretty(pg_total_relation_size(c.oid))  as size_pretty
    , pg_total_relation_size(c.oid) / (1024*1024)  as sizeMb
from pg_class as c
join pg_namespace  as n
    on (n.oid = c.relnamespace)
    and n.nspname = 'schema_name'
left join pg_roles  as r
    on c.relowner = r.oid
where nspname not in ('pg_catalog', 'information_schema')
    and c.relkind <> 'i'
    and nspname !~ '^pg_toast'
order by sizeMb desc;
```

Получить код создания view

Получить код создания процедуры

Выбрать внешние таблицы

Пример анонимного блока

Создание автоинкрементного поля

##### Администрирование, мониторинг

Получение ключа дистрибуции по таблице

Вычислить коэффциент перекоса таблицы

Проверка доступных таблиц

Просмотреть свои активные процессы

Получить размеры таблиц

Выбрать таблицы схемы

Просмотреть заблокированные запросы

Запрос показывает какой именно запрос заблокирован

Найти владельца таблицы

Найти таблицы созданные под персональной учеткой

## Примеры кода 

Партиционирование

Пример включения оптимизатора GPORCA












