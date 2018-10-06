import RPi.GPIO as x
import time

x.setmode(x.BOARD)
x.setwarnings(False)
x.setup(40, x.OUT)# enable1
x.setup(38, x.OUT)# in 1
x.setup(36, x.OUT)# in 2

x.setup(33, x.OUT)#
x.setup(35, x.OUT)#
x.setup(37, x.OUT)#


x.setup(5, x.IN)#
x.setup(3, x.IN)#
#################################################################
x.output(40, x.HIGH)
x.output(33, x.HIGH)
while 1:
    val = x.input(5)
    if val:
        
        x.output(35, x.LOW)
        x.output(37, x.HIGH) 
        
    else: 
        x.output(37, x.LOW)
        x.output(35, x.LOW)

    val = x.input(3)
    if val:
        
        x.output(36, x.LOW)
        x.output(38, x.HIGH) 
        
    else: 
        x.output(36, x.LOW)
        x.output(38, x.LOW)
        

x.cleanup()
