import RPi.GPIO as GPIO		# import GPIO
#import paho.mqtt.client as mqtt
from tkinter import *
import tkinter as tk
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import LED
from gpiozero import Servo
from time import sleep

fenetre = tk.Tk()
downarrow=PhotoImage(file='arrowdown.gif')
uparrow=PhotoImage(file='arrowup.gif')

factory = PiGPIOFactory(host='192.168.1.127')
coffrage=[]
pieds=[]
numpadb=[7,8,9,4,5,6,1,2,3,0]
boutons=[]
global clab
global plab
global servo
global led
global led1
global led2
global led3
global led4
led=[]
led2=[]
led1=[]
led3=[]
led4=[]


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
            self.button.config(image=uparrow)
        elif self.dire=='down':
            self.button.config(image=downarrow)
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
        global servo
        global led
        global led1
        global led2
        global led3
        global led4
        try:
            if type(self.sortie)==list:
                if len(self.sortie)==2:
                    led1=LED(self.sortie[0],self.sortie[1],pin_factory=factory)
                    led2=LED(self.sortie[1],pin_factory=factory)
                    led1.on()
                    led2.on()
                if len(self.sortie)==4:
                    led1=LED(self.sortie[0],pin_factory=factory)
                    led2=LED(self.sortie[1],pin_factory=factory)
                    led3=LED(self.sortie[2],pin_factory=factory)
                    led4=LED(self.sortie[3],pin_factory=factory)
                    led1.on()
                    led2.on()
                    led3.on()
                    led4.on()

            else:
                servo=Servo(21,pin_factory=factory)
                servo.value(1)
                #led=LED(self.sortie,pin_factory=factory)
                #led.on()
                GPIO.output(self.sortie, True)
            print('Activation de {}'.format(self.sortie))
            framec.config(bg='red')
            framep.config(bg='red')
            f1.config(bg='red')
            b1.config(bg='red')
            tt.config(bg='red')
            for p in plab:
                p.config(bg='red')
            for q in clab:
                p.config(bg='red')
            for i in boutons:
                if i.nom!=self.nom:
                    i.button.config(state=DISABLED)
        except:
            fenetre.destroy()
            fenetre.mainloop()


    def release():
        global servo
        global led
        global led1
        global led2
        global led3
        global led4
        framec.config(bg='green')
        framep.config(bg='blue')
        f1.config(bg='blue')
        b1.config(bg='blue')
        tt.config(bg='blue')
        try:
            if type(servo)!=list:
                servo.value(-1)
            if type(led)!=list:
                led.off()
            if type(led1)!=list:
                led1.off()
            if type(led2)!=list:
                led2.off()
            if type(led3)!=list:
                led3.off()
            if type(led4)!=list:
                led4.off()
        except:
            fenetre.destroy()
            fenetre.mainloop()

        servo=[]
        led=[]
        led1=[]
        led2=[]
        led3=[]
        led4=[]

        for l in boutons:
            GPIO.output(l.sortie,False)
        for k in plab:
            k.config(bg='green')
        for i in boutons:
            i.button.config(state=NORMAL)
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
pied2=Label(text="Pied 2",bg="green")
pied3=Label(text="Pied 3",bg="green")
pied4=Label(text="Pied 4",bg="green")
plab=[pied1,pied2,pied3,pied4]

class numpad(tk.Frame):
    def __init__(self,fenetre,outil):
        self.outil=outil
        self.nump=[]
        framec.place_forget()
        framep.place_forget()
        tk.Frame.__init__(self,fenetre)
        self.grid()
        self.numpad_create()
        self.pw=[]
    
    def numpad_create(self):
        r=1
        c=0
        for t in self.numpadb:
            t
            t=tk.Button(fenetre,text=str(b),width=10,height=5)
            t.bind('<ButtonPress-1>',lambda event, p=b:self.onPress(p))
            t.grid(row=r,column=c)
            self.nump.append(t)
            c += 1
            if c>2:
                c=0
                r += 1
        self.valid=tk.Button(fenetre,text='Valider',width=10,height=5)
        self.valid.bind('<ButtonPress-1>',lambda event:self.valider())
        self.valid.grid(row=5,column=1)
        self.corriger=tk.Button(fenetre,text='Corriger',width=10,height=5)
        self.corriger.bind('<ButtonPress-1>',lambda event:self.corrige())
        self.corriger.grid(row=5,column=2)

    def corrige(self):
        self.pw=[]

    def onPress(self,b):
        self.pw.append(b)
        
    def valider(self):
        if self.pw==[1,2,3,4]:
            self.afficheroutil()
            return 'OK'
        elif self.pw!=[] and [1,2,3,4]:
            return 'incorrect'
        self.pw=[]

    def oublie(self):
        for t in self.nump:
            self.t.grid_forget()


    def afficheroutil(self):
        self.oublie()
        self.valid.grid_forget()
        self.corriger.grid_forget()
        if self.outil=='coffrage':
            
            a=10
            o=40
            n=1
            global boutons
            global plab
            global clab
            bcoffr.config(bg='yellow')
            bpie.config(bg='grey')
            tt.place_forget()
            for i in boutons:
                i.button.place_forget()
            for j in plab:
                j.place_forget()
            for k in coffrage:
                if n%2==1:
                    k.button.place(x=a,y=o)
                elif n%2==0:
                    k.button.place(x=a,y=o+100)
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
        if self.outil=='pieds':
            a=10
            o=40
            n=1
            global plab
            bpie.config(bg='yellow')
            bcoffr.config(bg='grey')
            f1.place_forget()
            b1.place_forget()
            tt.place_forget()
            for i in boutons:
                i.button.place_forget()
            for j in clab:
                j.place_forget()
            for k in pieds:
                if n%2==1:
                    k.button.place(x=a,y=o)
                    print('Bouton {} setup'.format(k.nom))
                elif n%2==0:
                    k.button.place(x=a,y=o+100)
                    print('Bouton {} setup'.format(k.nom))
                    a=a+100
                n=n+1
                if n==9:
                    o=o+200
                    a=10
            u=0
            tt.place(x=10,y=305)
            pied1.place(x=10,y=105)
            pied2.place(x=110,y=105)
            pied3.place(x=210,y=105)
            pied4.place(x=310,y=105)


framec=Frame(fenetre,height=190,width=720,bg="green")
framec.place(x=0,y=30)
Label(framec,text='Simple',font=(25)).place(x=630,y=30)

framep=Frame(fenetre,height=190,width=720,bg="blue")
framep.place(x=0,y=230)
Label(framep,text='Multi',font=(25)).place(x=630,y=30)

pfw1=bouton('fw1',21,'192.168.1.117','pied','up')
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

pfw=bouton('pw',[21,16,5,7],'192.168.1.117','pied','up')
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









d=0






    








quitter=tk.Button(fenetre,text='Quitter',command=fenetre.destroy)
quitter.place(x=725,y=440)

for i in boutons:
    i.button.config(state=NORMAL)

bcoffr=tk.Button(fenetre,text='Coffrage',font=(70),height=3,width=10)
bcoffr.bind('<ButtonPress-1>',lambda event:numpad(fenetre,'coffrage',numpadb))
bcoffr.place(x=400,y=425)
bpie=tk.Button(fenetre,text='Pieds',font=70,height=3,width=10)
bpie.bind('<ButtonPress-1>',lambda event:numpad(fenetre,'pieds',numpadb))
bpie.place(x=550,y=425)

fenetre.geometry("800x600+10+10")
fenetre.overrideredirect(True)
fenetre.geometry("{0}x{1}+0+0".format(fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()))
fenetre.mainloop()


GPIO.cleanup()



    


