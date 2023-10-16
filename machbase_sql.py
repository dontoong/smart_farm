from machbaseAPI import machbase
ip='175.126.123.217'
machbase_port=5656
# 온도 센서
def read_ground_temp():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'ground_temp\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return result[10:-2]

# 습도 센서
def read_ground_humi():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'ground_humi\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return result[10:-2]

# ph 센서
def read_ground_ph():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'ground_ph\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return result[10:-2]

# co2 센서
def read_co2():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'Co2\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return result[10:-2]

# 내부 온도 센서
def read_inner_temp():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'inner_temp\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return result[10:-2]

# 내부 습도 센서
def read_inner_humi():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'inner_humi\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return result[10:-2]

# 외부 온도 센서
def read_outer_temp():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'outer_temp\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return result[10:-2]

# 외부 습도 센서
def read_outer_humi():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'outer_humi\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return result[10:-2]

# 풍속 센서
def read_wind():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'wind\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return result[10:-2]

# 물 pH 센서
def read_water_ph():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'water_ph\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return result[10:-2]

# 일조량 센서
def read_sun():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'sun\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return result[10:-2]

# 강수량 센서
def read_rain():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'rain\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return result[10:-2]


# Sensor
# 온도 센서
def read_ground_temp_float():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'ground_temp\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return float(result[10:-2])

# 습도 센서
def read_ground_humi_float():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'ground_humi\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return float(result[10:-2])

# ph 센서
def read_ground_ph_float():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'ground_ph\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return float(result[10:-2])

# co2 센서
def read_co2_float():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'Co2\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return float(result[10:-2])

# 내부 온도 센서
def read_inner_temp_float():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'inner_temp\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return float(result[10:-2])

# 내부 습도 센서
def read_inner_humi_float():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'inner_humi\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return float(result[10:-2])

# 외부 온도 센서
def read_outer_temp_float():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'outer_temp\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return float(result[10:-2])

# 외부 습도 센서
def read_outer_humi_float():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'outer_humi\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return float(result[10:-2])

# 풍속 센서
def read_wind_float():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'wind\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return float(result[10:-2])

# 물 pH 센서
def read_water_ph_float():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'water_ph\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return float(result[10:-2])

# 일조량 센서
def read_sun_float():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'sun\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return float(result[10:-2])

# 강수량 센서
def read_rain_float():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'rain\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return float(result[10:-2])

# Control
# DB에 window_1 열림 신호 보내기
def window_1_open():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('insert into controll (name, time, value) values (\'window_1\', sysdate, 1)') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()

# DB에 window_1 닫힘 신호 보내기
def window_1_close():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('insert into controll (name, time, value) values (\'window_1\', sysdate, 0)') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    
# DB에 window_2 열림 신호 보내기
def window_2_open():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('insert into controll (name, time, value) values (\'window_2\', sysdate, 1)') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()

# DB에 window_2 닫힘 신호 보내기
def window_2_close():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('insert into controll (name, time, value) values (\'window_2\', sysdate, 0)') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()

# DB에 w_pump 열림 신호 보내기
def w_pump_open():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('insert into controll (name, time, value) values (\'w_pump\', sysdate, 1)') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()

# DB에 w_pump 닫힘 신호 보내기
def w_pump_close():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('insert into controll (name, time, value) values (\'w_pump\', sysdate, 0)') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    
# DB에 Ventil 열림 신호 보내기
def Ventil_open():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('insert into controll (name, time, value) values (\'Ventil\', sysdate, 1)') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()

# DB에 Ventil 닫힘 신호 보내기
def Ventil_close():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('insert into controll (name, time, value) values (\'Ventil\', sysdate, 0)') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()

# DB에서 최신 window_1 조회
def find_window_1():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from controll where name =\'window_1\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return result[10:-2]
    
# DB에서 최신 window_2 조회
def find_window_2():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from controll where name =\'window_2\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return result[10:-2]

# DB에서 최신 w_pump 조회
def find_w_pump():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from controll where name =\'w_pump\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return result[10:-2]

# DB에서 최신 Ventil 조회
def find_Ventil():
    db = machbase()
    if db.open(ip,'SYS','MANAGER',machbase_port) == 0 :
        return db.result()
    if db.execute('select value from controll where name =\'Ventil\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return result[10:-2]
 
print(read_ground_temp())   
#print(find_window_1())
# print(find_window_2())
# print(find_w_pump())
# print(find_Ventil())