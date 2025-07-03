import time
from paho.mqtt import client as mqtt_client

BROKER = 'localhost'
PORT   = 1883
TOPIC  = 'digital-twin/sensor'

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT, code =", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(msg.payload.decode())

# Yeni Client, default olarak v3.1.1 kullanır
client = mqtt_client.Client()
client.on_connect = on_connect
client.on_message = on_message

# Arka planda network döngüsünü başlat
client.loop_start()

# Broker’a bağlan
client.connect(BROKER, PORT)

# Ana thread’i yaşıyor tutalım
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Subscriber stopped.")
    client.loop_stop()
