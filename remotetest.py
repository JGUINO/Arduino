from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Motor

#factory = PiGPIOFactory(host='192.168.1.124')
red = LED(17)

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)



