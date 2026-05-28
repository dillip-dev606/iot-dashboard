import paho.mqtt.client as mqtt
import json

BROKER = "broker.hivemq.com"
TOPIC = "dillip/home/sensor"

# Connection callback
def on_connect(client, userdata, flags, rc):
    print("Connected with result code:", rc)
    client.subscribe(TOPIC)
    print("Subscribed to:", TOPIC)

# Message callback
def on_message(client, userdata, msg):

    payload = msg.payload.decode()

    print("\nRaw MQTT:")
    print(payload)

    try:
        data = json.loads(payload)

        temperature = data["temperature"]
        humidity = data["humidity"]

        print("Temperature:", temperature)
        print("Humidity:", humidity)

    except Exception as e:
        print("JSON Parse Error:", e)

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

print("Connecting to broker...")

client.connect(BROKER, 1883, 60)

print("Waiting for MQTT data...")

client.loop_forever()