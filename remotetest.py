from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Motor
from gpiozero import LED
from time import sleep
#factory = PiGPIOFactory(host='192.168.1.124')
red = LED(4)

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)



