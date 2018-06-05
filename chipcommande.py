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
boutonscoffrage=[]
boutonspieds=[]

framec=Frame(fenetre,height=190,width=720,bg="green")
framec.place(x=0,y=30)
Label(framec,text='Coffrage',font=(25)).place(x=630,y=30)

framep=Frame(fenetre,height=190,width=720,bg="blue")
framep.place(x=0,y=230)
Label(framep,text='Pieds',font=(25)).place(x=630,y=30)

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
clab=[clf1,clf2,crf1,crf2,clm1,clm2,crm1,crm2,clt1,clt2,crt1,crt2]

pied1=Label(text="Pied 1")
pied2=Label(text="Pied 2")
pied3=Label(text="Pied 3")
pied4=Label(text="Pied 4")
plab=[pied1,pied2,pied3,pied4]

class coffrage:
    #def __init__(self,c):
        #for i in c:
            #self.i = i
            #GPIO.setup(self.i,GPIO.OUT)
            #GPIO.output(self.i,False)
    def activer(self,nom,bout):
        self.bout=bout
        self.nom=nom
        global boutons
        global pieds
        global plab
        #GPIO.output(self.x,True)
        print("Activation de "+str(nom))
        if nom in c:
            framec.config(bg='red')
            for j in clab:
                j.config(bg='red')
        if nom in pieds:
            framep.config(bg='red')
            for k in plab:
                k.config(bg='red')

        for i in boutons:
            if i!=bout:
                i.config(state=DISABLED)

    def release(self,nom):
        global boutons
        global clab
        global plab
        self.nom=nom
        framec.config(bg='green')
        framep.config(bg='blue')
        for j in clab:
            j.config(bg='green')
        for k in plab:
            k.config(bg='blue')
        print(str(nom)+' désactivé')
        for i in boutons:
            i.config(state=NORMAL)

d=0


def affichercoffrage():
    a=10
    o=40
    n=1
    global boutonscoffrage
    global boutons
    global plab
    global clab
    for i in boutons:
        i.place_forget()
    for j in plab:
        j.place_forget()
    for k in boutonscoffrage:
        p=k
        if n%2==1:
            p.place(x=a,y=o)
        elif n%2==0:
            p.place(x=a,y=o+100)
            a=a+100
        n=n+1
        if n==13:
            o=o+100
            a=10
    u=0
    for cl in clab:
        
        if u%2==0:
            cl.place(x=5+u*100,y=110)
        elif u%2==1:
            cl.place(x=5+u*100,y=130)
            u=u+1

    fenetre.mainloop()

def afficherpieds():
    a=10
    o=40
    n=1
    global boutonspieds
    for i in boutons:
        i.place_forget()
    for j in clab:
        j.place_forget()
    for k in boutonspieds:
        p=k
        if n%2==1:
            p.place(x=a,y=o)
        elif n%2==0:
            p.place(x=a,y=o+100)
            a=a+100
        n=n+1
        if n==9:
            o=o+200
            a=10
    u=0
    for pied in plab:
        pied.place(x=5+u*100,y=120)
        u=u+100
    
    fenetre.mainloop()


n=1
l=0
h=0
c3189=coffrage()


for i in c:
    p=i
    if n%2==1:
        p=tk.Button(fenetre)
        p.config(image=uparrow)
        p.bind('<ButtonPress-1>',lambda event, p=p,nom=i:c3189.activer(nom,p))
        p.bind('<ButtonRelease-1>',lambda event, nom=i:c3189.release(nom))
        
        
    elif n%2==0:
        p=tk.Button(fenetre)
        p.config(image=downarrow)
        p.bind('<ButtonPress-1>',lambda event, p=p,nom=i:c3189.activer(nom,p))
        p.bind('<ButtonRelease-1>',lambda event, nom=i:c3189.release(nom))
        
    n=n+1
    boutonscoffrage.append(p)
    boutons.append(p)

l=0
for i in pieds:
    p=i
    if n%2==1:
        p=tk.Button(fenetre)
        p.config(image=uparrow)
        p.bind('<ButtonPress-1>',lambda event, p=p,nom=i:c3189.activer(nom,p))
        p.bind('<ButtonRelease-1>',lambda event, nom=i:c3189.release(nom))
        
        
    elif n%2==0:
        p=tk.Button(fenetre)
        p.config(image=downarrow)
        p.bind('<ButtonPress-1>',lambda event, p=p,nom=i:c3189.activer(nom,p))
        p.bind('<ButtonRelease-1>',lambda event, nom=i:c3189.release(nom))
        
    n=n+1
    boutonspieds.append(p)
    boutons.append(p)



quitter=tk.Button(fenetre,text='Quitter',command=fenetre.destroy)
quitter.place(x=725,y=440)

for i in boutons:
    i.config(state=NORMAL)

bcoffr=tk.Button(fenetre,text='Coffrage',font=(70),height=3,width=10,command=affichercoffrage)
bcoffr.place(x=400,y=425)
bpie=tk.Button(fenetre,text='Pieds',font=70,height=3,width=10,command=afficherpieds)
bpie.place(x=550,y=425)

fenetre.geometry("800x600+10+10")
fenetre.overrideredirect(True)
fenetre.geometry("{0}x{1}+0+0".format(fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()))
fenetre.mainloop()


GPIO.cleanup()



    


