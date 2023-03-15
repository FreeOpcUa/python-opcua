# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 07:06:02 2022

@author: K___O
"""

import paho.mqtt.client as mqtt
from random import uniform
import time


Broker = "127.0.0.1"
client = mqtt.Client("KPI Publisher")
client.connect(Broker)

while True:
    KPI_Availability = uniform(75, 98)
    KPI_Performance = uniform(85, 95)
    KPI_Quality = uniform(90, 99)
    KPI_OEE = (KPI_Availability/100) * (KPI_Performance/100) * (KPI_Quality/100)
    
    client.publish("KPI/Availability", KPI_Availability)
    print("Just published " + str(KPI_Availability) + " to Topic: KPI/Availability")
    
    client.publish("KPI/Performance", KPI_Performance)
    print("Just published " + str(KPI_Performance) + " to Topic: KPI/Performanc")
    
    client.publish("KPI/Quality", KPI_Quality)
    print("Just published " + str(KPI_Quality) + " to Topic: KPI/Quality")
    
    client.publish("KPI/OEE", KPI_OEE)
    print("Just published " + str(KPI_OEE) + " to Topic: KPI/OEE")
    
    time.sleep(1)