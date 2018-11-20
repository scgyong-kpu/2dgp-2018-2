import paho.mqtt.client as mqttClient
import time

MQTT_TOPIC = '/kr/ac/kpu/2dgp/2018/scgyong'

Connected = False
broker_addr = 'broker.hivemq.com'
# broker_addr = 'test.mosquitto.org'
# broker_addr = 'iot.eclipse.org'

_callback = None
_context = None
def on_connect(client, userdata, flags, rc):
    print(client, userdata, flags, rc)
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")

def on_disconnect(client):
    print("Disconnected")

def on_message(client, userdata, msg):
    text = msg.payload.decode('utf-8')
    print("message", msg.topic, '/', msg.payload, _callback)
    if _callback != None:
        _callback(text, _context)

def publish(msg):
    client.publish(MQTT_TOPIC, msg)
    
def connect(callback = None, context = None):
    global client, _callback, _context
    client = mqttClient.Client('Python')
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect

    client.connect(broker_addr)
    print("After calling connect()")
    client.loop_start()

    client.subscribe(MQTT_TOPIC)
    print("Subscribing", MQTT_TOPIC)

    _callback = callback
    _context = context

def disconnect():
    print("exiting")
    client.disconnect()
    client.loop_stop()
