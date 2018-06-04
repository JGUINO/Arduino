import RPi.GPIO as GPIO		# import GPIO
#import paho.mqtt.client as mqtt
from tkinter import *
import tkinter as tk
fenetre = tk.Tk()
downarrow=PhotoImage(file='arrowdown.gif')
uparrow=PhotoImage(file='arrowup.gif')

c=['IOoutlfu','IOoutlfd','IOoutrfu','IOoutrfd','IOoutlmu','IOoutlmd','IOoutrmu','IOoutrmd','IOoutltu','IOoutltd','IOoutrtu','IOoutrtd']
pieds=['IOoutup1','IOoutdo1','IOoutup2','IOoutdo2','IOoutup3','IOoutdo3','IOoutup4','IOoutdo4']

class pied():
    def __init__(self,pieds):
        self.IOoutup1=IOoutup1
        self.IOoutdo1=IOoutdo1
        self.IOoutup2=IOoutup2
        self.IOoutdo2=IOoutdo2
        self.IOoutup3=IOoutup3
        self.IOoutdo3=IOoutdo3
        self.IOoutup4=IOoutup4
        self.IOoutdo4=IOoutdo4

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.IOoutup1,GPIO.OUT)
        GPIO.output(self.IOoutup1, False)
        GPIO.setup(self.IOoutdo1,GPIO.OUT)
        GPIO.output(self.IOoutdo1, False)
        GPIO.setup(self.IOoutup2,GPIO.OUT)
        GPIO.output(self.IOoutup2, False)
        GPIO.setup(self.IOoutdo2,GPIO.OUT)
        GPIO.output(self.IOoutdo2, False)
        GPIO.setup(self.IOoutup3,GPIO.OUT)
        GPIO.output(self.IOoutup3, False)
        GPIO.setup(self.IOoutdo3,GPIO.OUT)
        GPIO.output(self.IOoutdo3, False)
        GPIO.setup(self.IOoutup4,GPIO.OUT)
        GPIO.output(self.IOoutup4, False)
        GPIO.setup(self.IOoutdo4,GPIO.OUT)
        GPIO.output(self.IOoutdo4, False)

    def up1():
        GPIO.output(self.IOoutup, True)
        print("Activation up1")
    def down1():
        GPIO.output(self.IOoutdo, True)
        print("Activation down1")
    
    def up2():
        GPIO.output(self.IOoutup, True)
        print("Activation up2")
    def down2():
        GPIO.output(self.IOoutdo, True)
        print("Activation down2")

    def up3():
        GPIO.output(self.IOoutup, True)
        print("Activation up3")
    def down3():
        GPIO.output(self.IOoutdo, True)
        print("Activation down3")

    def up4():
        GPIO.output(self.IOoutup, True)
        print("Activation up4")
    def down4():
        GPIO.output(self.IOoutdo, True)
        print("Activation down4")

boutons=[]

class coffrage:
    #def __init__(self,c):
        #for i in c:
            #self.i = i
            #GPIO.setup(self.i,GPIO.OUT)
            #GPIO.output(self.i,False)
    def activer(self,x):
        self.x=x
        global boutons
        #GPIO.output(self.x,True)
        print("Activation de "+str(x))
        for i in boutons:
            if str(i)!=x:
                i.config(state=DISABLED)
    def release(self):
        global boutons
        for i in boutons:
            i.config(state=NORMAL)

d=0

    
    



n=1
l=0
h=0
c3189=coffrage()
framec=Frame(fenetre,height=190,width=720,bg="green")
framec.place(x=0,y=30)
Label(framec,text='Coffrage',font=(25)).place(x=630,y=30)

framep=Frame(fenetre,height=190,width=720,bg="blue")
framep.place(x=0,y=230)
Label(framep,text='Pieds',font=(25)).place(x=630,y=30)

for i in c:
    p=i
    if n%2==1:
        p=tk.Button(fenetre)
        p.config(image=uparrow)
        p.bind('<ButtonPress-1>',lambda event, p=p:c3189.activer(p))
        p.bind('<ButtonRelease-1>',lambda event, p=i:print(p+' desactivé'),c3189.release)
        p.place(x=l,y=50)
        
    elif n%2==0:
        p=tk.Button(fenetre,image=downarrow,command=lambda p=i: print("activation de "+str(p)))
        p.config(image=downarrow)
        p.bind('<ButtonPress-1>',lambda event, p=i:c3189.activer(p))
        p.bind('<ButtonRelease-1>',lambda event, p=i:print(p+' desactivé'),c3189.release)
        p.place(x=l,y=150)
        l=l+100
    n=n+1
    boutons.append(p)

l=0
for i in pieds:
    p=i
    if n%2==1:
        p=tk.Button(fenetre)
        p.config(image=uparrow)
        p.bind('<ButtonPress-1>',lambda event, p=i:c3189.activer(p))
        p.bind('<ButtonRelease-1>',lambda event, p=i:print(p+' desactivé'),c3189.release)
        p.place(x=l,y=250)
        
    elif n%2==0:
        p=tk.Button(fenetre,image=downarrow,command=lambda p=i: print("activation de "+str(p)))
        p.config(image=downarrow)
        p.bind('<ButtonPress-1>',lambda event, p=i:c3189.activer(p))
        p.bind('<ButtonRelease-1>',lambda event, p=i:print(p+' desactivé'),c3189.release)
        p.place(x=l,y=350)
        l=l+100
    n=n+1
    boutons.append(p)



pied1=Label(text="Pied 1")
pied1.place(x=5,y=320)
pied2=Label(text="Pied 2")
pied2.place(x=105,y=320)
pied3=Label(text="Pied 3")
pied3.place(x=205,y=320)
pied4=Label(text="Pied 4")
pied4.place(x=305,y=320)

clf1=Label(text="Avant",bg='green')
clf2=Label(text="gauche",bg='green')
crf1=Label(text="Avant",bg='green')
crf2=Label(text="droit",bg='green')
clm1=Label(text="Milieu",bg='green')
clm2=Label(text="gauche",bg='green')
crm1=Label(text="Milieu",bg='green')
crm2=Label(text="droit",bg='green')
clt1=Label(text="Arrière",bg='green')
clt2=Label(text="gauche",bg='green')
crt1=Label(text="Arrière",bg='green')
crt2=Label(text="droit",bg='green')
clf1.place(x=5,y=110)
clf2.place(x=5,y=130)
crf1.place(x=105,y=110)
crf2.place(x=105,y=130)
clm1.place(x=205,y=110)
clm2.place(x=205,y=130)
crm1.place(x=305,y=110)
crm2.place(x=305,y=130)
clt1.place(x=405,y=110)
clt2.place(x=405,y=130)
crt1.place(x=505,y=110)
crt2.place(x=505,y=130)

quitter=tk.Button(fenetre,text='Quitter',command=fenetre.destroy)
quitter.place(x=730,y=400)

for i in boutons:
    i.config(state=NORMAL)

fenetre.geometry("800x600+10+10")
fenetre.overrideredirect(True)
fenetre.geometry("{0}x{1}+0+0".format(fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()))
fenetre.mainloop()


GPIO.cleanup()

