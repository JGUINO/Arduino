import RPi.GPIO as GPIO		# import GPIO
#import paho.mqtt.client as mqtt
from tkinter import *
import tkinter as tk
from gpiozero.pins.pigpio import PiGPIOFactory

fenetre = tk.Tk()
downarrow=PhotoImage(file='arrowdown.gif')
uparrow=PhotoImage(file='arrowup.gif')

factory = PiGPIOFactory(host='192.168.1.117')

coffrage=[]
pieds=[]
boutons=[]


class bouton():
    def __init__(self,nom,sortie,ip,typ,dire):
        self.sortie=sortie
        self.ip=ip
        self.typ=typ
        self.nom=nom
        self.dire=dire
        GPIO.setmode(GPIO.BCM)
        self.button=tk.Button(fenetre)
        if self.dire=='up':
            button.config(image=uparrow)
        elif self.dire=='down':
            button.config(image=downarrow)
        button.bind('<ButtonPress-1>',lambda event:nom.activer())
        button.bind('<ButtonRelease-1>',lambda event:nom.release())

        if type(self.sortie)==list:
            for i in sortie:
                GPIO.setup(self.i,GPIO.OUT)
                GPIO.output(self.i, False)

    def press(self):
        if type(self.sortie)==list:
            for i in sortie:
                GPIO.output(self.i,True)
        else:
            GPIO.output(self.sortie, True)
        print('Activation de {}'.format(self.sortie))
        framec.config(bg='red')
        framep.config(bg='red')
        f1.config(bg='red')
        b1.config(bg='red')
        tt.config(bg='red')
        for i in boutons:
            if i.nom!=self.nom:
                i.config(state=DISABLED)
        
        def release(self):
            framec.config(bg='green')
            framep.config(bg='blue')
            f1.config(bg='blue')
            b1.config(bg='blue')
            tt.config(bg='blue')
            for j in clab:
                j.config(bg='green')
            for k in plab:
                k.config(bg='green')
            for i in boutons:
                i.button.config(state=NORMAL)


pfw1=bouton('fw1',1,'192.168.1.117','pied','up')
pieds.append(pfw1)
pbw1=bouton('bw1',2,'192.168.1.117','pied','down')
pieds.append(pbw1)
pfw2=bouton('fw2',3,'192.168.1.117','pied','up')
pieds.append(pfw2)
pbw2=bouton('bw2',4,'192.168.1.117','pied','down')
pieds.append(pbw2)
pfw3=bouton('fw3',5,'192.168.1.117','pied','up')
pieds.append(pfw3)
pbw3=bouton('bw3',6,'192.168.1.117','pied','down')
pieds.append(pbw3)
pfw4=bouton('fw4',7,'192.168.1.117','pied','up')
pieds.append(pfw4)
pbw4=bouton('bw4',8,'192.168.1.117','pied','down')
pieds.append(pbw4)

pfw=bouton('pw',[1,3,5,7],'192.168.1.117','pied','up')
pbw=bouton('bw',[2,4,6,8],'192.168.1.117','pied','down')
pieds.append(pfw)
pieds.append(pbw)

clfu=bouton('lfu',9,'192.168.1.117','coffrage','up')
clfd=bouton('lfd',10,'192.168.1.117','coffrage','down')
crfu=bouton('rfu',11,'192.168.1.117','coffrage','up')
crfd=bouton('rfd',12,'192.168.1.117','coffrage','down')
clmu=bouton('lmu',13,'192.168.1.117','coffrage','up')
clmd=bouton('lmd',14,'192.168.1.117','coffrage','down')
crmu=bouton('rmu',15,'192.168.1.117','coffrage','up')
crmd=bouton('rmd',16,'192.168.1.117','coffrage','down')
clbu=bouton('lbu',17,'192.168.1.117','coffrage','up')
clbd=bouton('lbd',18,'192.168.1.117','coffrage','down')
crbu=bouton('rbu',19,'192.168.1.117','coffrage','up')
crbd=bouton('rbd',20,'192.168.1.117','coffrage','down')
cfu=bouton('fu',[9,11],'192.168.1.117','coffrage','up')
cfd=bouton('fd',[10,12],'192.168.1.117','coffrage','down')
cbu=bouton('bu',[17,19],'192.168.1.117','coffrage','up')
cbd=bouton('bd',[18,20],'192.168.1.117','coffrage','down')
cup=bouton('up',[9,11,17,19],'192.168.1.117','coffrage','up')
cdo=bouton('do',[10,12,18,20],'192.168.1.117','coffrage','down')

coffrage.append(clfu)
coffrage.append(clfd)
coffrage.append(crfu)
coffrage.append(crfd)
coffrage.append(clmu)
coffrage.append(clmd)
coffrage.append(crmu)
coffrage.append(crmd)
coffrage.append(clbu)
coffrage.append(clbd)
coffrage.append(crbu)
coffrage.append(crbd)
coffrage.append(cfu)
coffrage.append(cfd)
coffrage.append(cbu)
coffrage.append(cbd)
coffrage.append(cup)
coffrage.append(cdo)

for i in coffrage:
    boutons.append(i)
for i in pieds:
    boutons.append(i)

framec=Frame(fenetre,height=190,width=720,bg="green")
framec.place(x=0,y=30)
Label(framec,text='Simple',font=(25)).place(x=630,y=30)

framep=Frame(fenetre,height=190,width=720,bg="blue")
framep.place(x=0,y=230)
Label(framep,text='Multi',font=(25)).place(x=630,y=30)

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
f1=Label(text="Avant",bg='blue')
b1=Label(text='Arrière',bg='blue')
tt=Label(text='Tous',bg='blue')


pied1=Label(text="Pied 1",bg="green")
pied2=Label(text="Pied 2",gb="green")
pied3=Label(text="Pied 3",bg="green")
pied4=Label(text="Pied 4",bg="green")
plab=[pied1,pied2,pied3,pied4]





d=0


def affichercoffrage():
    a=10
    o=40
    n=1
    global boutonscoffrage
    global boutons
    global plab
    global clab
    bcoffr.config(bg='yellow')
    bpie.config(bg='grey')
    tt.place_forget()
    for i in boutons:
        i.place_forget()
    for j in plab:
        j.place_forget()
    for k in coffrage:
        p=k.button
        if n%2==1:
            p.place(x=a,y=o)
        elif n%2==0:
            p.place(x=a,y=o+100)
            a=a+100
        n=n+1
        if n==13:
            o=o+200
            a=10
    u=0
    n=0
    f1.place(x=105,y=300)
    b1.place(x=205,y=300)
    tt.place(x=5,y=300)
    for cl in clab:
        
        if n%2==0:
            cl.place(x=5+u*100,y=100)
        elif n%2==1:
            cl.place(x=5+u*100,y=120)
            u=u+1
        n=n+1


    

def afficherpieds():
    a=10
    o=40
    n=1
    global boutonspieds
    global plab
    bpie.config(bg='yellow')
    bcoffr.config(bg='grey')
    f1.place_forget()
    b1.place_forget()
    tt.place_forget()
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
    tt.place(x=5,y=300)
    for p in plab:
        p.place(x=10+u*100,y=110)
        u=u+100






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



    


