#!/usr/bin/env python3
import random
import time
from paho.mqtt import client as mqtt_client

BROKER   = "127.0.0.1"
PORT     = 1883
TOPIC    = "digital-twin/sensor"
CLIENT_ID = f"subscriber-{random.randint(0, 1000)}"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"🔌 Connected to MQTT broker, return code = {rc}")
        client.subscribe(TOPIC)
        print(f"📡 Subscribed to topic: {TOPIC}")
    else:
        print(f"❌ Connection failed with code {rc}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"📨 Received message: {payload}")

# 1) Client oluştur ve callback’leri ata
client = mqtt_client.Client(client_id=CLIENT_ID, protocol=mqtt_client.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message

# 2) Broker’a bağlan
print(f"➡️  Connecting to {BROKER}:{PORT} as {CLIENT_ID} …")
client.connect(BROKER, PORT)

# 3) Döngüye gir
client.loop_forever()
