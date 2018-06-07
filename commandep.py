import RPi.GPIO as GPIO		# import GPIO
#import paho.mqtt.client as mqtt
from tkinter import *
import tkinter as tk
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import LED

fenetre = tk.Tk()
downarrow=PhotoImage(file='arrowdown.gif')
uparrow=PhotoImage(file='arrowup.gif')

factory = PiGPIOFactory(host='192.168.1.117')

boutons=[]

frame1=Frame(fenetre,height=400,width=400,bg=('yellow'))
frame1.place(x=200,y=50)

class bouton():
    def __init__(self,nom,sortie,ip):
        self.sortie=sortie
        self.ip=ip
        self.nom=nom
        GPIO.setmode(GPIO.BCM)
        self.button=tk.Button(frame1,text=str(self.nom))
        self.button.bind('<ButtonPress-1>',lambda event,self=self:self.press())
        self.button.bind('<ButtonRelease-1>',lambda event:bouton.release())

        if type(self.sortie)==list:
            for i in self.sortie:
                GPIO.setup(i,GPIO.OUT)
                GPIO.output(i, False)
        elif type(self.sortie)==int:
            GPIO.setup(self.sortie,GPIO.OUT)
            GPIO.output(self.sortie, False)

    def press(self):
        if self.sortie==21:
            LED(self.sortie,pin_factory=factory).on()

        if type(self.sortie)==list:
            for i in self.sortie:
                GPIO.output(i,True)
        else:
            GPIO.output(self.sortie, True)
        print('Activation de {}'.format(self.sortie))
        frame.config(bg='red')

        for i in boutons:
            if i.nom!=self.nom:
                i.button.config(state=DISABLED)
        
    def release():
        framec.config(bg='green')
        framep.config(bg='blue')
        f1.config(bg='blue')
        b1.config(bg='blue')
        tt.config(bg='blue')
        for l in boutons:
            GPIO.output(l.sortie,False)
            l.button.config(state=NORMAL)
        LED(21,pin_factory=factory).off()

    def placer():
        lf.button.place(x=10,y=10)
        rf.button.place(x=300,y=10)
        lb.button.place(x=10,y=360)
        rb.button.place(x=300,y=360)
        fw.button.place(x=160,y=50)
        bw.button.place(x=160,y=310)
        fl.button.place(x=50,y=180)
        fr.button.place(x=280,y=180)

lf=bouton('Left Front',1,'192.168.1.117')
rf=bouton('Right Front',2,'192.168.1.117')
lb=bouton('Left Back',3,'192.168.1.117')
rb=bouton('Right Back',4,'192.168.1.117')
fw=bouton('Forward',5,'192.168.1.117')
bw=bouton('Backward',6,'192.168.1.117')
fl=bouton('Full Left',7,'192.168.1.117')
fr=bouton('Full Right',8,'192.168.1.117')
boutons.append(lf)
boutons.append(rf)
boutons.append(lb)
boutons.append(rb)
boutons.append(fw)
boutons.append(bw)
boutons.append(fl)
boutons.append(fr)



bouton.placer()

quitter=tk.Button(fenetre,text='Quitter',command=fenetre.destroy)
quitter.place(x=725,y=440)

fenetre.geometry("800x600+10+10")
fenetre.overrideredirect(True)
fenetre.geometry("{0}x{1}+0+0".format(fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()))

fenetre.mainloop()
