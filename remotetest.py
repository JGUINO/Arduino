from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Motor
from gpiozero import LED
from time import sleep
factory = PiGPIOFactory(host='192.168.1.124')
p=[]
for i in range(1,35):
    p.append(LED(i,pin_factory=factory))

red=LED(4,pin_factory=factory)

while True:
    for i in p:
        i.on()
    sleep(1)
    for in in p:
        i.off()
    sleep(1)



