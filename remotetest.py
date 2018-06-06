from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Motor
from gpiozero import LED
from time import sleep
#factory = PiGPIOFactory(host='192.168.1.124')
factory3 = PiGPIOFactory(host='192.168.1.3')
red=LED(7,25,pin_factory=factory3)

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)



