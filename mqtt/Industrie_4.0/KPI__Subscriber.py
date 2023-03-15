# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 07:06:47 2022

@author: K___O
"""

import paho.mqtt.client as mqtt
import time


Broker = "127.0.0.1"
client = mqtt.Client("KPI Subscriber")
client.connect(Broker)

def on_message(client, userdata, message):
    
    print("Message Topic = ",message.topic)
    print("Received message: ", str(message.payload.decode("utf-8")))
    print("\n")

client.loop_start()
client.subscribe("KPI/Availability")
client.subscribe("KPI/Performance")
client.subscribe("KPI/Quality")
client.subscribe("KPI/OEE")
client.on_message = on_message
time.sleep(30)
client.loop_stop()
