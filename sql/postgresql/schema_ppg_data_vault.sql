-- schema_ppg_data_vault.sql

select user


/*

create role r_ppg_data_vault_r;
--grant select on schema ppg_data_vault to r_ppg_data_vault_r;
--grant usage on schema r_ppg_data_vault to r_ppg_data_vault;
ALTER DEFAULT PRIVILEGES IN SCHEMA ppg_data_vault 
GRANT SELECT ON TABLES TO r_ppg_data_vault_r;

create role r_ppg_data_vault_rw;
ALTER DEFAULT PRIVILEGES IN SCHEMA ppg_data_vault 
GRANT SELECT ON TABLES TO r_ppg_data_vault_rw;
ALTER DEFAULT PRIVILEGES IN SCHEMA ppg_data_vault 
GRANT  insert, delete, truncate, references, trigger, update ON TABLES TO r_ppg_data_vault_rw;
ALTER DEFAULT PRIVILEGES IN SCHEMA ppg_data_vault 



*/



ppg_data_vault.sources
ppg_data_vault.h_name
ppg_data_vault.h_surname
ppg_data_vault.h_middlename
ppg_data_vault.h_phonenumber
ppg_data_vault.h_address
ppg_data_vault.h_domain
ppg_data_vault.h_l1domain
ppg_data_vault.h_nickname
ppg_data_vault.h_email
ppg_data_vault.h_city
ppg_data_vault.h_person
ppg_data_vault.l_person_email




-- truncate table ppg_data_vault.sources;
-- drop table if exists ppg_data_vault.sources;
create table ppg_data_vault.sources(
id bigint GENERATED ALWAYS AS IDENTITY (
  		START WITH 20220202 INCREMENT BY 1 
		MINVALUE 1 MAXVALUE 2147483647 NO CYCLE) not null,
source_cd varchar(64),
source_desc text
);
-- select * from ppg_data_vault.sources;
-- хэш
-- дата добавления
-- откуда пришел источник (телеграм канал, прочее)
-- кол-во колонок
-- разделитель
-- хэш файла 


-- drop table if exists ppg_data_vault.h_name;
create table ppg_data_vault.h_name (
id bigint GENERATED ALWAYS AS IDENTITY (
  		START WITH 20210227 INCREMENT BY 1 
		MINVALUE 1 MAXVALUE 2147483647 NO CYCLE) not null,
name varchar(64)
);
-- select * from ppg_data_vault.h_name order by id desc limit 100;
-- update ppg_data_vault.h_name set name = lower(name);



-- drop table if exists ppg_data_vault.h_surname;
create table ppg_data_vault.h_surname(
id bigint GENERATED ALWAYS AS IDENTITY (
  		START WITH 20210227 INCREMENT BY 1 
		MINVALUE 1 MAXVALUE 2147483647 NO CYCLE) not null,
name varchar(64)
);
-- select * from ppg_data_vault.h_surname;



-- drop table if exists ppg_data_vault.h_middlename;
create table ppg_data_vault.h_middlename(
id bigint GENERATED ALWAYS AS IDENTITY (
  		START WITH 20210227 INCREMENT BY 1 
		MINVALUE 1 MAXVALUE 2147483647 NO CYCLE) not null,
name varchar(64)
);
-- select * from ppg_data_vault.h_middlename;



-- drop table if exists ppg_data_vault.h_phonenumber;
create table ppg_data_vault.h_phonenumber(
id bigint GENERATED ALWAYS AS IDENTITY (
  		START WITH 20220406 INCREMENT BY 1 
		MINVALUE 1 MAXVALUE 2147483647 NO CYCLE) not null,
source_id bigint,
phonenumber bigint
);
-- select * from ppg_data_vault.h_phonenumber;



-- drop table if exists ppg_data_vault.h_address;
create table ppg_data_vault.h_address(
id bigint GENERATED ALWAYS AS IDENTITY (
  		START WITH 20220406 INCREMENT BY 1 
		MINVALUE 1 MAXVALUE 2147483647 NO CYCLE) not null,
hash text,
source_id bigint,
address text
);
-- select * from ppg_data_vault.h_address;




-- drop table if exists ppg_data_vault.h_domain;
create table ppg_data_vault.h_domain(
id bigint GENERATED ALWAYS AS IDENTITY (
  		START WITH 20220430 INCREMENT BY 1 
		MINVALUE 1 MAXVALUE 2147483647 NO CYCLE) not null,
hash text,
domain text
);
-- select * from ppg_data_vault.h_domain;



-- drop table if exists ppg_data_vault.h_l1domain;
create table ppg_data_vault.h_l1domain(
id bigint GENERATED ALWAYS AS IDENTITY (
  		START WITH 20220502 INCREMENT BY 1 
		MINVALUE 1 MAXVALUE 2147483647 NO CYCLE) not null,
hash text,
l1domain text
);
-- select * from ppg_data_vault.h_l1domain;





-- drop table if exists ppg_data_vault.h_nickname;
create table ppg_data_vault.h_nickname(
id bigint GENERATED ALWAYS AS IDENTITY (
  		START WITH 20220430 INCREMENT BY 1 
		MINVALUE 1 MAXVALUE 2147483647 NO CYCLE) not null,
hash text,
nickname text
);
-- select * from ppg_data_vault.h_nickname;



-- drop table if exists ppg_data_vault.h_email;
create table ppg_data_vault.h_email(
id bigint GENERATED ALWAYS AS IDENTITY (
  		START WITH 20220430 INCREMENT BY 1 
		MINVALUE 1 MAXVALUE 2147483647 NO CYCLE) not null,
hash text,
source_id bigint,
nickname_id bigint,
domain_id bigint,
l1domain_id bigint
);
-- select * from ppg_data_vault.h_email;


-- drop table if exists ppg_data_vault.h_city;
create table ppg_data_vault.h_city(
id bigint GENERATED ALWAYS AS IDENTITY (
  		START WITH 20220430 INCREMENT BY 1 
		MINVALUE 1 MAXVALUE 2147483647 NO CYCLE) not null,
hash text,
city text
);
-- select * from ppg_data_vault.h_city;



-- drop table if exists ppg_data_vault.h_person;
create table ppg_data_vault.h_person(
id bigint GENERATED ALWAYS AS IDENTITY (
  		START WITH 20220430 INCREMENT BY 1 
		MINVALUE 1 MAXVALUE 2147483647 NO CYCLE) not null,
hash text,
source_id bigint,
surname_id bigint,
name_id bigint,
middlename_id bigint,
birthdate date,
phonenumber_id bigint,
city_id bigint
);
-- select * from ppg_data_vault.h_person;
-- select count(1)cnt from ppg_data_vault.h_person;		-- 261931
-- select * from h_person order by id desc;
-- select * from h_person where hash = '96cc81b33193851ea77636f758e46126';
-- delete from ppg_data_vault.h_person where surname_id is null and name_id is null and birthdate is null and phonenumber_id is null and city_id is null;
insert into ppg_data_vault.h_person(source_id, hash) 
                values(20211227 , '96cc81b33193851ea77636f758e46126');
select id from ppg_data_vault.h_person where hash = '96cc81b33193851ea77636f758e46126';
               

-- drop table if exists ppg_data_vault.l_person_email;
create table ppg_data_vault.l_person_email(
id bigint GENERATED ALWAYS AS IDENTITY (
  		START WITH 20220502 INCREMENT BY 1 
		MINVALUE 1 MAXVALUE 2147483647 NO CYCLE) not null,
hash text,
source_id bigint,
person_id bigint,
email_id bigint
);
-- select * from ppg_data_vault.l_person_email;





ppg_data_vault.sources
ppg_data_vault.h_name
ppg_data_vault.h_surname
ppg_data_vault.h_middlename
ppg_data_vault.h_phonenumber
ppg_data_vault.h_address
ppg_data_vault.h_domain
ppg_data_vault.h_l1domain
ppg_data_vault.h_nickname
ppg_data_vault.h_email
ppg_data_vault.h_city
ppg_data_vault.h_person
ppg_data_vault.l_person_email


select
	hpers.hash 
	, hpers.birthdate 
	, surn."name" 	as surname
	, nam."name" 	as name
	, mnam."name"	as middlename
	, phon.phonenumber 
	, city.city 
from ppg_data_vault.h_person as hpers
left join ppg_data_vault.h_surname as surn
	on hpers.surname_id = surn.id
left join ppg_data_vault.h_name as nam
	on hpers.name_id = nam.id
left join ppg_data_vault.h_middlename as mnam 
	on hpers.middlename_id = mnam.id
left join ppg_data_vault.h_phonenumber as phon
	on hpers.phonenumber_id = phon.id
left join ppg_data_vault.h_city as city
	on hpers.city_id = city.id

	
	l_person_email





-- drop table if exists ppg_data_vault.h_socnetwork;
create table ppg_data_vault.h_socnetwork(
id bigint GENERATED ALWAYS AS IDENTITY (
  		START WITH 20220514 INCREMENT BY 1 
		MINVALUE 1 MAXVALUE 2147483647 NO CYCLE) not null,
hash text,
source_id bigint,
socnetwork text
);
-- select * from ppg_data_vault.h_socnetwork;


-- drop table if exists ppg_data_vault.h_pass;
create table ppg_data_vault.h_pass(
id bigint GENERATED ALWAYS AS IDENTITY (
  		START WITH 20220514 INCREMENT BY 1 
		MINVALUE 1 MAXVALUE 2147483647 NO CYCLE) not null,
hash text,
source_id bigint,
pass text
);
-- select * from ppg_data_vault.h_pass;





-- drop table if exists ppg_data_vault.l_person_socnetwork;
create table ppg_data_vault.l_person_socnetwork(
id bigint GENERATED ALWAYS AS IDENTITY (
  		START WITH 20220514 INCREMENT BY 1 
		MINVALUE 1 MAXVALUE 2147483647 NO CYCLE) not null,
hash text,
source_id bigint,
person_id bigint,
socnetwork_id bigint
);
-- select * from ppg_data_vault.l_person_socnetwork;



-- drop table if exists ppg_data_vault.l_person_socnetwork_pass;
create table ppg_data_vault.l_person_socnetwork_pass(
id bigint GENERATED ALWAYS AS IDENTITY (
  		START WITH 20220514 INCREMENT BY 1 
		MINVALUE 1 MAXVALUE 2147483647 NO CYCLE) not null,
hash text,
source_id bigint,
person_socnetwork_id bigint,
pass_id bigint
);
-- select * from ppg_data_vault.l_person_socnetwork_pass;





