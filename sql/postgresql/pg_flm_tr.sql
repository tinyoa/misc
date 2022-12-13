
DROP TABLE IF EXISTS public.price_list_imp;
CREATE TABLE public.price_list_imp(
	id serial,
	grp varchar(50),
	item_name varchar(150),
	price varchar(20)
);

COPY public.price_list_imp (grp, item_name, price) 
FROM 'D:\trash\imp\price_utf8.csv' 
WITH DELIMITER ';'
CSV HEADER;


SELECT * FROM public.price_list_imp;

UPDATE public.price_list_imp
SET price = '22,10'
WHERE id = 1;

SELECT id, grp, item_name, REPLACE(REPLACE(price, ',', '.'), ' ', '')::float pr
FROM public.price_list_imp;

DROP TABLE IF EXISTS public.price_list;
CREATE TABLE public.price_list(
	id serial,
	grp varchar(50),
	item_name varchar(150),
	price float
);

INSERT INTO public.price_list
SELECT id, grp, item_name, REPLACE(REPLACE(price, ',', '.'), ' ', '')::float pr
FROM public.price_list_imp;

SELECT * FROM public.price_list;
