# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 06:23:34 2022

@author: K___O
"""


import paho.mqtt.client as mqtt
import time

mqttBroker = "broker.emqx.io"
client = mqtt.Client("Temperature_Man_1")
client.connect(mqttBroker)

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))
    print("\n Message topic = ",message.topic)



client.loop_start()
client.subscribe("TEMPERATURE/Inside")
client.on_message = on_message
time.sleep(4)
client.loop_stop()
