
--[[
Скрипт должен сохранять все сделки в файл
TODO
- объявить константы для префикса файла сделок и расширения
- записывать заголовок в файл сделок
]]

local act_time = 0
local prev_time = 0
local save_time = ""
local prev_save_time = ""
local counter = 0
local is_run = true
local date_time= ""
local datetime_m = ""
local prev_datetime_m = ""
local new_row = ""
local acc_row = ""
local delimiter = ";"

function SaveTextToFile(filename, text)
	-- Пытается открыть файл в режиме "чтения/записи"
	f = io.open(getScriptPath().."\\"..filename, "r+");
	-- Если файл не существует
	--[[if f == nil then 
		log.trace('creating file')
		-- Создает файл в режиме "записи"
		f = io.open(getScriptPath().."\\"..filename, "w"); 
		-- Закрывает файл
		f:close();
	end;
	]]
	
	-- Открывает уже существующий файл в режиме "добавления"
	f = io.open(getScriptPath().."\\"..filename, "a+");
	f:write(text);
end
	
function OnAllTrade(alltrade)
	--act_time = tonumber(alltrade.datetime.sec)
	save_time = alltrade.datetime.year
				.. alltrade.datetime.month
				.. alltrade.datetime.day 
				.. "_" .. alltrade.datetime.hour 
				.. "_" .. alltrade.datetime.min 
	datetime_m = alltrade.datetime.year
				.. alltrade.datetime.month
				.. alltrade.datetime.day 
				--.. "_" .. alltrade.datetime.hour 
				--.. "_" .. alltrade.datetime.min 
	--if  act_time == prev_time then
	if save_time == prev_save_time then
		counter = counter + 1
		
		date_time = tostring(alltrade.datetime.hour) .. ":" .. tostring(alltrade.datetime.min) .. ":" .. tostring(alltrade.datetime.sec)
		--message(date_time .. "   " .. tostring(counter))
		new_row = alltrade.exchange_code  .. delimiter .. 
				alltrade.class_code   .. delimiter .. 
				alltrade.period    .. delimiter .. 
				alltrade.datetime.hour .. ":" .. 
				alltrade.datetime.min .. ":" ..
				alltrade.datetime.sec .. "." ..
				alltrade.datetime.mcs   .. delimiter .. 
				alltrade.trade_num   .. delimiter .. 
				alltrade.sec_code   .. delimiter.. 
				alltrade.price  .. delimiter .. 
				alltrade.qty   .. delimiter .. 
				alltrade.value    .. delimiter .. 
				alltrade.flags     .. delimiter .. 
				alltrade.exec_market 
		message(datetime_m .. "|".. new_row .. " / " .. tostring(counter))
		acc_row = acc_row .. "\n" .. new_row
	else
		SaveTextToFile("deals\\deals_"..datetime_m..".tab", acc_row)
		counter = 0
		acc_row = ""
		prev_time = tonumber(alltrade.datetime.sec)
		prev_save_time = save_time
		prev_datetime_m = datetime_m
	end

end
--[[
function OnAllTrade(alltrade)
date_time = tostring(alltrade.datetime.hour) .. ":" .. tostring(alltrade.datetime.min) .. ":" .. tostring(alltrade.datetime.sec)
message(date_time)
end
--]]

function main()
	while is_run 
	do
		sleep(100)
	end
end


function OnStop()
	is_run = false
	return 1000
end