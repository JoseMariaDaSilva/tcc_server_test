#!/usr/bin/python
# -*- coding:utf-8 -*-


import ADS1256
import RPi.GPIO as GPIO
import threading
from datetime import datetime



def run():
    data = []
    th1 = threading.currentThread()
    ADC = ADS1256.ADS1256()
    ADC.ADS1256_init()
    
    t1 = datetime.now()
    while getattr(th1, "do_run", True):
        data.append(round(ADC.ADS1256_GetSingleChannel(0)*5.0/0x7fffff,3))
    data = list(map(lambda x: str(x), data))
    print(datetime.now()-t1)
    with open('data.txt','a') as d:
        d.writelines('\n'.join(data))
    GPIO.cleanup()
    print ("\r\nFim do Programa!    ")
    exit()
        



 
    
    
