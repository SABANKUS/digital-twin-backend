import random
import time
import json
import paho.mqtt.client as mqtt
import requests

BROKER = "127.0.0.1"
PORT   = 1883
API_URL = "http://127.0.0.1:5000/sensor"

client = mqtt.Client()
client.connect(BROKER, PORT)

try:
    while True:
        data = {
            "temperature": round(random.uniform(18.0, 30.0), 2),
            "vibration":   round(random.uniform(0.1, 5.0), 2),
            "humidity":    round(random.uniform(30.0, 70.0), 2)
        }
        payload = json.dumps(data)

        # 1) MQTT publish
        client.publish("digital-twin/sensor", payload)
        # 2) HTTP POST to REST API
        try:
            resp = requests.post(API_URL, json=data, timeout=1)
            if resp.status_code != 201:
                print("API hata:", resp.status_code, resp.text)
        except Exception as e:
            print("API bağlantı hatası:", e)

        print(f"Published & Posted: {payload}")
        time.sleep(2)

except KeyboardInterrupt:
    print("Simulation stopped.")
    client.disconnect()
