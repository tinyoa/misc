-- schema__stg.sql

create table _stg.stg_person_dirty(
id bigint GENERATED ALWAYS AS IDENTITY (
  		START WITH 20221020 INCREMENT BY 1 
		MINVALUE 1 MAXVALUE 2147483647 NO CYCLE) not null,
src_id		bigint,
person_md5 	text,
name 		text,
surname		text,
middle_name text,
birth_date	date,
phone		text,
city		text,
email		text,
cite		text,
car_registry_name	text,
car_vin_number		text,
social_network_name text,
social_network_nick text,
password	text,
comment		text,
source_txt	text,				-- Полный путь к файлу
upload_ts	timestamp
);

comment on table _stg.stg_person_dirty is 'Таблица для грязного импорта данных по людям';


select * from _stg.stg_person_dirty;