#!/usr/bin/python 
#

"""
Title: ADC test program:

Description:
    adc_test program requests the analog voltage using the ADC located on the omap processor
    The ADC voltage is read every 1 second and is printed out (both digital and analog)
    
Developer: TJ Houck
Date: 6.5.2012

"""

import sys, time, datetime, array
import socket
import re

MAX_ADC = 4095      #max digital value for 12bit ADC
MAX_INPUT = 1.8V    #max input voltage

def analog(pinIndex):
     reading = open("/sys/devices/platform/omap/tsc/ain" + str(pinIndex + 1), "r").read()
     print "Analog voltage: %s" % reading

     #convert digital value to analog voltage
     
def main():
    count = 0
    
    print "Start time of analog read: %s" % time.ctime()
    
    while(count < 10):   #read analog voltage every 10 seconds
        analog(0)        #read value of ain1
        count++          #increment counter
        time.sleep(1)
        #For reading multiple ADC values
        #analog(1)  #read value of ain2
        #analog(2)  #read value of ain3
        #analog(3)  #read value of ain4
          
    print "Finish time: %s" % time.ctime()

if __name__ == '__main__':
    main()
