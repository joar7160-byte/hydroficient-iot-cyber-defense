import paho.mqtt.client as mqtt
import json
import time
import datetime 
import random

def main():
    deviceid = "GM-HYDROLOGIC-01"
    location = "main-building"
    topic = 'hydroficient/grandmarina/sensors/main-building/readings'
    interval = 2
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect("localhost", port=1883)
    counter = 0

    print(f"Starting device: {deviceid}")
    print(f"Location: {location}")
    print(f"Publishing to: {topic}")
    print(f"Interval: {interval} seconds")
    print("----------------------------------------")

    while True:
        counter += 1
        timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        pressure_upstream = random.uniform(80,85)
        pressure_downstream = random.uniform(75,80)
        flow_rate = random.uniform(38,42)
        print(f"[{counter}] Pressure:{pressure_upstream:.1f}/{pressure_downstream:.1f} PSI, Flow: {flow_rate:.1f} gal/min")
        payload = {
            "device_id": deviceid,
            "location": location,
            "pressure_upstream": pressure_upstream,
            "pressure_downstream": pressure_downstream,
            "flow_rate": flow_rate,
            "timestamp": timestamp,
            "counter": counter
        }
        client.publish(topic,json.dumps(payload) )
        time.sleep(2)


if __name__ == "__main__":
    main()
      
