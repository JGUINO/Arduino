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

frame=Frame(fenetre,height=400,width=400,bg=('yellow'))
frame.place(x=100,y=200)

class bouton():
    def __init__(self,nom,sortie,ip,x,y):
        self.sortie=sortie
        self.ip=ip
        self.nom=nom
        self.x=x
        self.y=y
        GPIO.setmode(GPIO.BCM)
        self.button=tk.Button(text=str(self.nom))
        self.button.bind('<ButtonPress-1>',lambda event,self=self:self.press())
        self.button.bind('<ButtonRelease-1>',lambda event:bouton.release())
        self.button.pack(frame,padx=self.x,pady=self.y)

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

    #def placer():
        #lf.button.place(fenetre,x=10,y=10)
        #rf.button.place(frame,padx=350,pady=10)
        #lb.button.place(frame,padx=10,pady=350)
        #rb.button.place(frame,padx=350,pady=350)
        #fw.button.place(frame,padx=180,pady=50)
        #bw.button.place(frame,padx=180,pady=310)
        #fl.button.place(frame,padx=50,pady=180)
        #fr.button.place(frame,padx=310,pady=180)

lf=bouton('Left Front',1,'192.168.1.117',10,10)
rf=bouton('Right Front',2,'192.168.1.117',350,10)
lb=bouton('Left Back',3,'192.168.1.117',10,350)
rb=bouton('Right Back',4,'192.168.1.117',350,350)
fw=bouton('Forward',5,'192.168.1.117',180,50)
bw=bouton('Backward',6,'192.168.1.117',180,310)
fl=bouton('Full Left',7,'192.168.1.117',50,180)
fr=bouton('Full Right',8,'192.168.1.117',310,180)
boutons.append(lf)
boutons.append(rf)
boutons.append(lb)
boutons.append(rb)
boutons.append(fw)
boutons.append(bw)
boutons.append(fl)
boutons.append(fr)



#bouton.placer()

quitter=tk.Button(fenetre,text='Quitter',command=fenetre.destroy)
quitter.place(x=725,y=440)

fenetre.geometry("800x600+10+10")
fenetre.overrideredirect(True)
fenetre.geometry("{0}x{1}+0+0".format(fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()))

fenetre.mainloop()
