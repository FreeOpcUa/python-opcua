# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 06:27:17 2022

@author: K___O
"""

import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker =  "broker.emqx.io"#"mqtt.eclipseprojects.io"
client = mqtt.Client('Temperatur_Inside')
client.connect(mqttBroker)

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE/Inside", randNumber)
    print("just published "+str(randNumber)+" to topic: TEMPERATUR Inside")
    time.sleep(1)