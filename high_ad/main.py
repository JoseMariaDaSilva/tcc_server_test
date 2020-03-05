#!/usr/bin/python
# -*- coding:utf-8 -*-


import time
import ADS1256
import RPi.GPIO as GPIO
from threading import Thread
import matplotlib.pyplot as plt
from datetime import datetime

import numpy as np


def run(seconds):
    data = []
    try:
        
        ADC = ADS1256.ADS1256()
        ADC.ADS1256_init()
        
        t1 = datetime.now()
        for _ in range(6060*seconds):
            
            
            #print ("0 ADC = {}".format(round(5*ADC.ADS1256_GetSingleChannel(0)/2**23,2)))
            data.append(round(ADC.ADS1256_GetSingleChannel(0)*5.0/0x7fffff,3))
            #ata1.append(round(ADC.ADS1256_GetSingleChannel(1)*5.0/0x7fffff,5))
            
        print(datetime.now()-t1)
        print(max(data))
        print(min(data))
        #print(np.sum(ADC.timer))
        plt.plot(data[500:])
        plt.legend()
        #plt.plot(data1[500:])
        plt.show()
        raise TypeError
            
    except :
    
        GPIO.cleanup()
        print ("\r\nProgram end     ")
        exit()

 
        
if __name__ == '__main__':
    t = Thread(target=run, args=3)
    
    t.start()
    
    
