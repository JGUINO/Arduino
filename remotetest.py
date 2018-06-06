from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Motor
from gpiozero import LED
from time import sleep
factory = PiGPIOFactory(host='192.168.1.124')
red=LED(7,25,pin_factory=factory)

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)



