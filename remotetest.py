from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Motor
from gpiozero import LED
from time import sleep
factory = PiGPIOFactory(host='192.168.1.117')
#p=[]

red=LED(21,pin_factory=factory)

while True:
    red.on()
#    for i in p:
#        i.on()
    sleep(1)
    red.off()
#    for i in p:
#        i.off()
    sleep(1)



