import paho.mqtt.client as mqtt
import json
import time
import datetime 
import random

def on_connect(client, userdata, flags, reason_code, properties):
    curr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("============================================================")
    print("   GRAND MARINA WATER MONITORING DASHBOARD")
    print(f"  Connected at: {curr}")
    print("============================================================")
    client.subscribe("hydroficient/grandmarina/#")

def display_reading(data):
    print(f"\n{'─' * 40}")
    print(f"  Location:  {data.get('location')}")
    print(f"  Device ID: {data.get('device_id')}")
    print(f"  Time:      {data.get('timestamp')}")
    print(f"  Count:     #{data.get('counter')}")
    print(f"{'─' * 40}")
    up = data.get('pressure_upstream', 0)
    down = data.get('pressure_downstream', 0)
    flow = data.get('flow_rate', 0)
    print(f"  Pressure (upstream):   {up:.1f} PSI")
    print(f"  Pressure (downstream): {down:.1f} PSI")
    print(f"  Flow rate:             {flow:.1f} gal/min")
    print(f"  Pressure differential: {up - down:.1f} PSI")

def on_message(client, userdata, message):
    try:
        user_data = json.loads(message.payload.decode())
        display_reading(user_data)
    except json.JSONDecodeError:
        print(f"[RAW] {message.topic}: {message.payload.decode()}")


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883)
client.loop_forever()