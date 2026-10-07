# -*- coding: utf-8 -*-
"""
Created on Fri May 29 12:10:28 2026

@author: mater
"""

import requests
import json
import time

#%% Request status

response = requests.get('http://192.168.2.159/rr_status?type=1')
data = response.json()
status = data['status']
coords = data['coords']['xyz']

#%% Absolute positioning

response = requests.get('http://192.168.2.159/rr_gcode?gcode=G90')
print(response.status_code) # 200 means success
print(response.json())   

#%% Relative positioning

response = requests.get('http://192.168.2.159/rr_gcode?gcode=G91')
print(response.status_code) # 200 means success
print(response.json())  

#%% Home, reply when idle

response = requests.get('http://192.168.2.159/rr_gcode?gcode=G28')
print(response.status_code) # 200 means success
print(response.json())  

while(1):
    response = requests.get('http://192.168.2.159/rr_status?type=1')
    time.sleep(0.1)
    data = response.json()
    status = data['status']
    if status == 'I':
        break

#%% Move to position

Z = -10

response = requests.get('http://192.168.2.159/rr_gcode?gcode=G0Z' + str(Z))
print(response.status_code) # 200 means success
print(response.json())  

while(1):
    response = requests.get('http://192.168.2.159/rr_status?type=1')
    data = response.json()
    status = data['status']
    if status == 'I':
        break

X = 50
Y = -70

response = requests.get('http://192.168.2.159/rr_gcode?gcode=G0X' + str(X) + 'Y' + str(Y))
print(response.status_code) # 200 means success
print(response.json())  

while(1):
    response = requests.get('http://192.168.2.159/rr_status?type=1')
    data = response.json()
    status = data['status']
    if status == 'I':
        break



