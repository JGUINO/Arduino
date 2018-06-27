import RPi.GPIO as GPIO		# import GPIO
#import paho.mqtt.client as mqtt
from tkinter import *
import tkinter as tk
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import LED
from gpiozero import Servo
from time import sleep
import matplotlib
matplotlib.use('TKAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as pltlib
import paho.mqtt.client as mqttc

fenetre = tk.Tk()
downarrow=PhotoImage(file='arrowdown.gif')
uparrow=PhotoImage(file='arrowup.gif')

global boutons
factory = PiGPIOFactory(host='192.168.1.127')
coffrage=[]
pieds=[]
numpadb=[7,8,9,4,5,6,1,2,3,0]
boutons=[]
global num
global clab
global c
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

framec=Frame(fenetre,height=190,width=720,bg="green")
#framec.place(x=0,y=30)
Label(framec,text='Simple',font=(25)).place(x=630,y=30)

framep=Frame(fenetre,height=190,width=720,bg="blue")
#framep.place(x=0,y=230)
Label(framep,text='Multi',font=(25)).place(x=630,y=30)

class MQTTb:
    
    
    def on_connect(self,client,userdata,flags,rc):
        #print('connected (%s)' % client._client_id)
        if rc!=0:
            client.connecte = True
            print("Connecte avec le code retour "+str(rc))
        else:
            client.connecte = False
        
    
    def on_message(self,client,userdata,message):
        if message.topic=='ping':
            self.client.publish(topic='ping',payload='check')
            print(message.payload)
        if message.topic=='pressions':
            print(message.payload)
            capt=int(message.payload[0])-49
            print('pos %s' %capt)
            pression=message.payload[1:len(message.payload)]
            c.y[capt]=int(pression)
            c.refreshFigure()

    def on_publish(self,client, obj , mid):
        print("Publication reussie")


    def __init__(self):
        self.client=mqttc.Client(client_id='rpicmd',clean_session=False)
        self.client.username_pw_set(username='commande',password=None)
        self.client.on_connect=self.on_connect
        self.client.on_message=self.on_message
        self.client.connect(host='192.168.1.124',port=1883)
        self.client.subscribe(topic='pressions',qos=2)
        self.client.subscribe(topic='ping',qos=2)
        


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

        else :
            #led=Servo(16,pin_factory=factory)
            #servo.value(1)
            led=LED(self.sortie,pin_factory=factory)
            led.on()
            #GPIO.output(self.sortie, True)
        print('Activation de {}'.format(self.sortie))
        framec.config(bg='red')
        framep.config(bg='red')
        f1.config(bg='red')
        b1.config(bg='red')
        tt.config(bg='red')
        for p in plab:
            p.config(bg='red')
        for q in clab:
            q.config(bg='red')
        for i in boutons:
            if i.nom!=self.nom:
                i.button.config(state=DISABLED)
        


    def release():
        global servo
        global led
        global led1
        global led2
        global led3
        global led4
        global plab
        global boutons
        global clab
        framec.config(bg='green')
        framep.config(bg='blue')
        f1.config(bg='blue')
        b1.config(bg='blue')
        tt.config(bg='blue')

        #if type(servo)!=list:
            #servo.value(-1)
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
        for p in clab:
            p.config(bg='green')
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
        global c
        try:
            c.suppr()
        except NameError:
            print ('c pas def')
        global num
        fenetre.config(bg='light grey')
        num=self
        self.outil=outil
        self.pw1=Label(text="*",font=(50),height=3,width=9,bg='grey')
        self.pw2=Label(text="**",font=(50),height=3,width=9,bg='grey')
        self.pw3=Label(text="***",font=(50),height=3,width=9,bg='grey')
        self.pw4=Label(text="****",font=(50),height=3,width=9,bg='grey')
        self.blanc1=Label(text='',height=3,width=9,font=50,bg='light grey')
        self.blanc2=Label(text='',height=3,width=9,font=50,bg='light grey')
        framec.place_forget()
        framep.place_forget()
        tk.Frame.__init__(self,fenetre)
        self.grid()
        self.pw=[]
        self.numpad_create()
        self.correct=Label(text='Correct',font=50,height=3,width=9,bg='grey',fg='green')
        self.cred=Label(text='Owner:G.Guillon',font=50,height=3,width=15,bg='grey',fg='navy')
        self.incorrect=Label(text='Incorrect',font=50,height=3,width=9,bg='grey',fg='red')
        
    
    def numpad_create(self):
        #r=1
        #c=0
        for i in boutons:
            i.button.place_forget()
        for j in plab:
            j.place_forget()
        for i in boutons:
            i.button.place_forget()
        for j in clab:
            j.place_forget()
        f1.place_forget()
        b1.place_forget()
        tt.place_forget()
        
        self.blanc1.grid(row=1,column=0)
        self.blanc2.grid(row=1,column=1)
        self.pad1=tk.Button(fenetre,text='1',width=10,height=4)
        self.pad1.bind('<ButtonPress-1>',lambda event:self.onPress(1))
        self.pad1.grid(row=4,column=2)
        self.pad2=tk.Button(fenetre,text='2',width=10,height=4)
        self.pad2.bind('<ButtonPress-1>',lambda event:self.onPress(2))
        self.pad2.grid(row=4,column=3)
        self.pad3=tk.Button(fenetre,text='3',width=10,height=4)
        self.pad3.bind('<ButtonPress-1>',lambda event:self.onPress(3))
        self.pad3.grid(row=4,column=4)
        self.pad4=tk.Button(fenetre,text='4',width=10,height=4)
        self.pad4.bind('<ButtonPress-1>',lambda event:self.onPress(4))
        self.pad4.grid(row=3,column=2)
        self.pad5=tk.Button(fenetre,text='5',width=10,height=4)
        self.pad5.bind('<ButtonPress-1>',lambda event:self.onPress(5))
        self.pad5.grid(row=3,column=3)
        self.pad6=tk.Button(fenetre,text='6',width=10,height=4)
        self.pad6.bind('<ButtonPress-1>',lambda event:self.onPress(6))
        self.pad6.grid(row=3,column=4)
        self.pad7=tk.Button(fenetre,text='7',width=10,height=4)
        self.pad7.bind('<ButtonPress-1>',lambda event:self.onPress(7))
        self.pad7.grid(row=2,column=2)
        self.pad8=tk.Button(fenetre,text='8',width=10,height=4)
        self.pad8.bind('<ButtonPress-1>',lambda event:self.onPress(8))
        self.pad8.grid(row=2,column=3)
        self.pad9=tk.Button(fenetre,text='9',width=10,height=4)
        self.pad9.bind('<ButtonPress-1>',lambda event:self.onPress(9))
        self.pad9.grid(row=2,column=4)
        self.pad0=tk.Button(fenetre,text='0',width=10,height=4)
        self.pad0.bind('<ButtonPress-1>',lambda event:self.onPress(0))
        self.pad0.grid(row=5,column=2)
        
        self.nump=[self.pad0,self.pad1,self.pad2,self.pad3,self.pad4,self.pad5,self.pad6,self.pad7,self.pad8,self.pad9]

        self.valid=tk.Button(fenetre,text='Valider',width=10,height=3)
        self.valid.bind('<ButtonPress-1>',lambda event:self.valider())
        self.valid.grid(row=6,column=2)
        self.corriger=tk.Button(fenetre,text='Corriger',width=10,height=3)
        self.corriger.bind('<ButtonPress-1>',lambda event:self.corrige())
        self.corriger.grid(row=6,column=3)
        self.annuler=tk.Button(fenetre,text='Annuler',width=10,height=3)
        self.annuler.bind('<ButtonPress-1>',lambda event:self.annule())
        self.annuler.grid(row=6,column=4)

    def annule(self):
        self.incorrect.grid_forget()
        self.corrige()
        capt()


    def corrige(self):
        self.pw=[]
        self.pw1.grid_forget()
        self.pw2.grid_forget()
        self.pw3.grid_forget()
        self.pw4.grid_forget()
        self.cred.place_forget()

    def onPress(self,b):
        self.incorrect.grid_forget()
        self.cred.place_forget()
        self.pw.append(b)
        if len(self.pw)==1:
            self.pw1.grid(row=1,column=3)
        if len(self.pw)==2:
            self.pw1.grid_forget()
            self.pw2.grid(row=1,column=3)
        if len(self.pw)==3:
            self.pw2.grid_forget()
            self.pw3.grid(row=1,column=3)
        if len(self.pw)==4:
            self.pw3.grid_forget()
            self.pw4.grid(row=1,column=3)
        
    def valider(self):
        if len(self.pw)==1:
            self.pw1.grid_forget()
        if len(self.pw)==2:
            self.pw2.grid_forget()
        if len(self.pw)==3:
            self.pw3.grid_forget()
        if len(self.pw)>=4:
            self.pw4.grid_forget()
        
        if self.pw==[1,2,3,4]:
            self.correct.grid(row=1,column=3)
            self.correct.grid_forget()
            self.blanc1.grid_forget()
            self.blanc2.grid_forget()
            self.incorrect.grid_forget()
            self.afficheroutil()
            self.pw=[]

        if self.pw==[0,5,0,9,1,9,9,6]:
            self.cred.place(x=0,y=50)
            self.pw=[]
        elif self.pw!=[1,2,3,4] and self.pw!=[]:
            self.incorrect.grid(row=1,column=3)
            #self.incorrect.grid_forget()
            self.pw=[]

    def oublie(self):
        self.pad0.grid_forget()
        self.pad1.grid_forget()
        self.pad2.grid_forget()
        self.pad3.grid_forget()
        self.pad4.grid_forget()
        self.pad5.grid_forget()
        self.pad6.grid_forget()
        self.pad7.grid_forget()
        self.pad8.grid_forget()
        self.pad9.grid_forget()

    def afficheroutil(self):
        self.oublie()
        self.valid.grid_forget()
        self.corriger.grid_forget()
        self.annuler.grid_forget()
        self.mqttb=MQTTb()
        self.mqttb.client.loop_start()
        
        if self.outil=='coffrage':
            
            a=10
            o=40
            n=1
            global boutons
            global plab
            global clab
            bcoffr.config(bg='yellow')
            bpie.config(bg='grey')
            bcapt.config(bg='grey')
            tt.place_forget()
            
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
            bcapt.config(bg='grey')
            
            
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
        framec.place(x=0,y=30)
        framep.place(x=0,y=230)

class capteurs():
    def __init__(self,parent):
        global num
        try:
            num.oublie()
            num.valid.grid_forget()
            num.corriger.grid_forget()
            num.annuler.grid_forget()
            num.correct.grid_forget()
            num.blanc1.grid_forget()
            num.blanc2.grid_forget()
            num.incorrect.grid_forget()
            if len(num.pw)==1:
                num.pw1.grid_forget()
            if len(num.pw)==2:
                num.pw2.grid_forget()
            if len(num.pw)==3:
                num.pw3.grid_forget()
            if len(num.pw)>=4:
                num.pw4.grid_forget()
        except NameError:
            print('num pas definit')
        bpie.config(bg='grey')
        bcoffr.config(bg='grey')
        bcapt.config(bg='yellow')
        for i in boutons:
            i.button.place_forget()
        for j in plab:
            j.place_forget()
        for i in boutons:
            i.button.place_forget()
        for j in clab:
            j.place_forget()
        f1.place_forget()
        b1.place_forget()
        tt.place_forget()
        framep.place_forget()
        framec.place_forget()
        self.initialize()
    def initialize(self):
        #self.button = tk.Button(fenetre,text="Open File",command=self.OnButtonClick).pack(side=tk.TOP)
        self.canvasFig=pltlib.figure(1)
        fenetre.config(bg='white')
        Fig = matplotlib.figure.Figure(figsize=(8,4),dpi=100)
        FigSubPlot = Fig.add_subplot(111)
        x=['1','2','3','4']
        self.y=[0,0,0,0]
        self.line1 = FigSubPlot.bar(x,self.y)
        FigSubPlot.set_xlabel('Capteurs')
        FigSubPlot.set_ylabel('Pression')
        FigSubPlot.axis([0,4,0,1000])
        self.canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(Fig, master=fenetre)
        self.ax = self.canvas.figure.axes[0]
        self.ax.set_xlim(-1,4)
        self.ax.set_ylim(0, 1000)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=150,y=0)
        self.canvas._tkcanvas.place(x=0,y=0)
        self.boucle()

    def boucle(self):
        self.mqttb=MQTTb()
        self.mqttb.client.loop_start()
        
        self.refreshFigure()
    def refreshFigure(self):
        for rect, h in zip(self.line1,self.y):
            rect.set_height(h)
        self.canvas.draw()
        
        print('graph raffraichit')
    def OnButtonClick(self):
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        x=[1,2,3,4]
        y=[300,870,604,330]
        #for num in range(0,1000):x.append(num*.001+1)
        # just some random function is given here, the real data is a UV-Vis spectrum
        #for num2 in range(0,1000):y.append(sc.math.sin(num2*.06)+sc.math.e**(num2*.001))
        X = x
        Y = y
        self.refreshFigure(X,Y)
    
    def suppr(self):
        self.mqttb.client.loop_stop(force=False)
        self.canvas._tkcanvas.delete("ALL")
        self.canvas._tkcanvas.place_forget()
 


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
def _quit():
    fenetre.quit()
    fenetre.destroy()
quitter=tk.Button(fenetre,text='Quitter')
quitter.bind('<ButtonPress-1>',lambda event:_quit())
quitter.place(x=725,y=440)

for i in boutons:
    i.button.config(state=NORMAL)

def capt():
    global c
    c=capteurs(None)


bcoffr=tk.Button(fenetre,text='Coffrage',font=(70),height=3,width=10)
bcoffr.bind('<ButtonPress-1>',lambda event:numpad(fenetre,'coffrage'))
bcoffr.place(x=400,y=425)
bpie=tk.Button(fenetre,text='Pieds',font=70,height=3,width=10)
bpie.bind('<ButtonPress-1>',lambda event:numpad(fenetre,'pieds'))
bpie.place(x=550,y=425)
bcapt=tk.Button(fenetre,text='Capteurs',font=(70),height=3,width=10)
bcapt.bind('<ButtonPress-1>',lambda event:capt())
bcapt.place(x=250,y=425)

fenetre.geometry("800x600+10+10")
fenetre.overrideredirect(True)
fenetre.geometry("{0}x{1}+0+0".format(fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()))
fenetre.mainloop()

GPIO.cleanup()
