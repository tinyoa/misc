-- demo_bookings.sql


select count(1)cnt from bookings.aircrafts_data;		-- 9
select * from bookings.aircrafts_data;

select count(1)cnt from bookings.airports_data;		-- 104
select * from bookings.airports_data;

select count(1)cnt from bookings.boarding_passes;		-- 7925812
select * from bookings.boarding_passes limit 100;

select count(1)cnt from bookings.bookings;			-- 2111110
select * from bookings.bookings limit 100;

select count(1)cnt from bookings.flights;			-- 214867
select * from bookings.bookings limit 100;

select count(1)cnt from bookings.seats;			-- 1339
select * from bookings.seats limit 100;

select count(1)cnt from bookings.ticket_flights;			-- 8391852
select * from bookings.ticket_flights limit 100;

select count(1)cnt from bookings.tickets;			-- 2949857
select * from bookings.tickets limit 100;



-- Проходы в самолет
select * 
from bookings.boarding_passes as bp 
limit 100;











