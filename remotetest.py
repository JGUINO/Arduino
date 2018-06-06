from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Motor
from gpiozero import LED
from time import sleep
factory = PiGPIOFactory(host='192.168.1.124')
p=[]
p.append(p0=LED(0,pin_factory=factory))
p.append(p1=LED(1,pin_factory=factory))
p.append(p2=LED(2,pin_factory=factory))
p.append(p3=LED(3,pin_factory=factory))
p.append(p4=LED(4,pin_factory=factory))
p.append(p5=LED(5,pin_factory=factory))
p.append(p6=LED(6,pin_factory=factory))
p.append(p7=LED(7,pin_factory=factory))
p.append(p8=LED(8,pin_factory=factory))
p.append(p9=LED(9,pin_factory=factory))
p.append(p10=LED(10,pin_factory=factory))
p.append(p11=LED(11,pin_factory=factory))
p.append(p12=LED(12,pin_factory=factory))
p.append(p13=LED(13,pin_factory=factory))
p.append(p14=LED(14,pin_factory=factory))
p.append(p15=LED(15,pin_factory=factory))
p.append(p16=LED(16,pin_factory=factory))
p.append(p17=LED(17,pin_factory=factory))
p.append(p18=LED(18,pin_factory=factory))
p.append(p19=LED(19,pin_factory=factory))
p.append(p20=LED(20,pin_factory=factory))
p.append(p21=LED(21,pin_factory=factory))
p.append(p22=LED(22,pin_factory=factory))
p.append(p23=LED(23,pin_factory=factory))
p.append(p24=LED(24,pin_factory=factory))
p.append(p25=LED(25,pin_factory=factory))
p.append(p26=LED(26,pin_factory=factory))
p.append(p27=LED(27,pin_factory=factory))
p.append(p28=LED(28,pin_factory=factory))
p.append(p29=LED(29,pin_factory=factory))
p.append(p30=LED(30,pin_factory=factory))
p.append(p31=LED(31,pin_factory=factory))
p.append(p32=LED(32,pin_factory=factory))
p.append(p33=LED(33,pin_factory=factory))
p.append(p34=LED(34,pin_factory=factory))
p.append(p35=LED(35,pin_factory=factory))
p.append(p36=LED(36,pin_factory=factory))


while True:
    for i in p:
        i.on()
    sleep(1)
    for i in p:
        i.off()
    sleep(1)



