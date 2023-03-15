# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 06:21:57 2022

@author: K___O
"""
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker =  "###################"#"mqtt.eclipseprojects.io"
client = mqtt.Client('Temperatur_Outside')
client.connect(mqttBroker)

while True:
    #randNumber = randrange(10)
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE/Outside", randNumber)
    print("just published "+str(randNumber)+" to topic TEMPERATUR Outside")
    time.sleep(1)