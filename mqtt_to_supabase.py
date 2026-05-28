import paho.mqtt.client as mqtt
import psycopg2
import json

BROKER = "broker.hivemq.com"
TOPIC = "dillip/home/sensor"

# Supabase connection
conn = psycopg2.connect(
    host="db.udsqqzlijvkypxbbepxf.supabase.co",
    port="5432",
    database="postgres",
    user="postgres",
    password="Dillip@2004@"
)

cursor = conn.cursor()

print("Connected to Supabase")

# MQTT connect callback
def on_connect(client, userdata, flags, rc):
    print("MQTT Connected:", rc)
    client.subscribe(TOPIC)
    print("Subscribed:", TOPIC)

# MQTT message callback
def on_message(client, userdata, msg):

    payload = msg.payload.decode()

    print("\nRaw MQTT:")
    print(payload)

    try:
        data = json.loads(payload)

        temperature = data["temperature"]
        humidity = data["humidity"]

        cursor.execute(
            """
            INSERT INTO sensor_data
            (temperature, humidity)
            VALUES (%s, %s)
            """,
            (temperature, humidity)
        )

        conn.commit()

        print(
            f"Saved to Supabase -> "
            f"Temp:{temperature} "
            f"Humidity:{humidity}"
        )

    except Exception as e:
        print("Error:", e)

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

print("Connecting MQTT...")

client.connect(BROKER, 1883, 60)

client.loop_forever()