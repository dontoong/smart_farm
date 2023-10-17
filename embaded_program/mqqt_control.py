import paho.mqtt.client as mqtt
import machbase_sql
mqqt_port=5050
mqttc = mqtt.Client()
mqttc.connect(machbase_sql.ip, mqqt_port)

def window_1_send_1():
        mqttc.publish("window_1", '1')
        
def window_1_send_0():
        mqttc.publish("window_1", '0')
        
def window_2_send_1():
        mqttc.publish("window_2", '1')
        
def window_2_send_0():
        mqttc.publish("window_2", '0')
        
def w_pump_send_1():
        mqttc.publish("w_pump", '1')
        
def w_pump_send_0():
        mqttc.publish("w_pump", '0')
        
def ventil_send_1():
        mqttc.publish("ventil", '1')
        
def ventil_send_0():
        mqttc.publish("ventil", '0')