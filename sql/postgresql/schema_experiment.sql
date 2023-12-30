-- schema_experiment.sql


create type experiment.tp_log_entry as (
message_txt text,
event_type_cd varchar(64),
event_ts timestamp
);


create type experiment.tp_log_instance as (
log_entries_arr _tp_log_entry,
procedure_nm text,
run_id int8
);


create type experiment.tp_parent_static as (
info_type_cd varchar(64),
info_dt date,
payment_amt numeric(20,4),
child_num int2
);



create sequence experiment.tst_seq 
increment by 1
minvalue 1
maxvalue 9223372036854775807
start 1;

alter sequence experiment.tst_seq owner to smbd;
grant all on sequence eperiment.tst_seq to smbd;

create sequence experiment.sq_error_table
increment by 1
minvalue 1
maxvalue 9223372036854775807 
start 1;

create sequence experiment.sq_procedure_log
increment by 1
minvalue 1
maxvalue 9223372036854775807 
start 1;

create sequence experiment.sq_procedure_run_id
increment by 1
minvalue 1
maxvalue 9223372036854775807 
start 1;


-- -- -- -- 
create or replace function experiment.drv_add_log_entry(
	p_log_item experiment.tp_log_instance
	, p_message_txt text 
	, p_event_type_cd varchar(64))
	returns tp_log_instance
	language plpgsql
	immutable 
as $$
begin 
	p_log_item.log_entries_arr[coalesce(array_upper(p_log_item.log_entries_arr, 1), 0) + 1] := (
		p_message_txt
		, p_event_type_cd
		, clock_timestamp() at time zone 'msk')::experiment.tp_log_entry
		;
end;
$$
execute on any;

create or replace function experiment.srv_create_log(p_procedure_nm text)
	returns tp_log_instance
	language plpgsql
	immutable 
as $$ 
declare
	l_log_item experiment.tp_log_instance;
begin
	l_log_item.run_id := nextval('experiment.sq_procedure_run_id');
	l_log_item.procedure_nm := p_procedure_nm;
	l_log_item.log_entries_arr := array[]::experiment.tp_log_entry[];

	return l_log_item;
end;
$$
execute on any;

create or replace function experiment.srv_demo_error()
	returns void
	language plpgsql
	security definer 
	volatile 
	set search_path = 'experiment'
as $$
declare 
	l_log tp_log_instance;
begin
	l_log := srv_add_log_entry(l_log, 'Test1', 'test');
	select  1/0;

	-- return void;
	exception
		when others then
			declare
				l_sqlstate text;
				l_message text;
				l_context text;
			begin
				get stacked diagnostics
					l_sqlstate  = returned_sqlstate,
					l_message = message_text,
					l_context = pg_exception_context;
				
				l_log := srv_add_log_entry(l_log, 'ErrorState = '||l_sqlstate||
					'; ErrorText = '||l_message||'; ErrorContext = '||l_context, 'ERROR');
				
			end;
		
	begin
		l_log := srv_add_log_entry(l_log, 'Test2', 'TEST');
		select 1/0;
	exception
		when others then
			l_log := srv_add_log_error (l_log, sqlstate, SQLERROR);
			l_log := srv_save_log(l_log);
			return;
	end;

	l_log := srv_add_log_entry(l_log, 'Test3', 'TEST');
	l_log := srv_save_log(l_log);
	return;
end;
$$


create table experiment.srv_etl_params (
	process_cd varchar(64) not null,
	parameter_cd varchar(64) not null,
	parameter_value_txt text null
);
with(appendonly = false)
distributed randomly;

create or replace function experiment.srv_get_parameter_value(
		p_process_cd varchar(64)
		, p_parameter_cd varchar(64))
	returns text 
	language sql 
	volatile 
	set search_path = 'experiment'
as $$
	select parameter_value_txt 
	from srv_etl_params 
	where parameter_cd = p_parameter_cd
		and process_cd = p_process_cd;
$$

create or replace function experiment.srv_if_tmp_table_exists(p_tablename text)
	returns bool
	language plpgsql
	volatile
as $$
	/* Функция для определения существует ли временная таблица p_tablename */

declare 
	step int default 0;
	proc varchar(64) := 'srv_if_tmp_table_exists';
	number_affected bigint;
	l_log experiment.tp_log_instance;

begin
	l_log := experiment.srv_add_log_entry(proc);

	step := 0;
	l_log := experiment.srv_add_log_entry(l_log
		, 'step ' || step || '{p_tablename = ' || p_tablename || '}'
		, 'START');
	
	select count(1)cnt
	from pg_catalog.pg_class as c
	left join pg_catalog.pg_namespace as n 
		on n.oid = c.relnamespace
	where n.nspname like '%pg_temp_%'
		--and pg_catalog.pg_table_id_visible(c.oid)
		and upper(relname) = upper(p_tablename)
		and relowner = (select oid from pg_roles where rolname = user)
	into number_affected;

	l_log := experiment.srv_add_log_entry(l_log
		, 'step ' || step || '{p_tablename = ' || p_tablename || '}'
		, 'SUCCESS');
	
	if number_affected > 0 then
		return true;
	else
		return false;
	end if;
end;
$$





-- Таблица дат
select 
	gs::date								as dat
	, extract(dow from gs::date) 			as dow
	, extract(isodow from gs::date) 		as isodow
	, extract(year from gs::date) 			as year
	, extract(month from gs::date) 			as month
	, extract(day from gs::date) 			as day
	, extract(doy from gs::date) 			as doy
	, extract(week from gs::date) 			as week
	, extract(quarter from gs::date) 		as quarter
	, extract(julian from gs::date) 		as julian
from generate_series('2022-12-01', '2022-12-31', interval '1 day') as gs;


CREATE OR REPLACE FUNCTION experiment.tsp_ft_days(p_start_dt date, p_end_dt date)
returns table (date_dt date ,
	dow integer,
	isodow integer,
	year integer,
	month integer,
	day integer,
	doy integer,
	week integer,
	quarter integer,
	julian integer
	) as 
$$
declare
    results record;
begin
    return query
	    select 
			gs::date										as dat
			, extract(dow from gs::date)::integer 			as dow
			, extract(isodow from gs::date)::integer 		as isodow
			, extract(year from gs::date)::integer 			as year
			, extract(month from gs::date)::integer 		as month
			, extract(day from gs::date)::integer 			as day
			, extract(doy from gs::date)::integer 			as doy
			, extract(week from gs::date)::integer 			as week
			, extract(quarter from gs::date)::integer 		as quarter
			, extract(julian from gs::date)::integer 		as julian
		from generate_series(p_start_dt, p_end_dt, interval '1 day') as gs;
end;
$$ language 'plpgsql';


select * from experiment.tsp_ft_days(date'2021-01-01', current_date);



