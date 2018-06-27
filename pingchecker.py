import shlex
import subprocess
from time import sleep
import RPi.GPIO as GPIO
from gpiozero import LED
import time


def ping (a):
	cmd=shlex.split("ping -c1 %s" % a)
	try:
	   output = subprocess.check_output(cmd)
	except subprocess.CalledProcessError as e:
		return False
	else:
		return True

class MQTTclient:
    
    
    def on_connect(self,client,userdata,flags,rc):
        #print('connected (%s)' % client._client_id)
        if rc!=0:
            client.connecte = True
            print("Connecte avec le code retour "+str(rc))
        else:
            client.connecte = False
        
    
    def on_message(self,client,userdata,message):
        print(message.payload)
        self.tme=perf_counter()
        print(str(self.tme))
        if self.time>1000:
            LED(16).off() #do that
        
        

    def on_publish(self,client, obj , mid):
        print("Publication reussie")

    def publish(self,payload):
        self.client.publish(topic='ping',qos=2,payload=payload)

    def __init__(self):
        self.client=mqttc.Client(client_id='mtr',clean_session=False)
        self.client.username_pw_set(username='motor',password=None)
        self.client.on_connect=self.on_connect
        self.client.on_message=self.on_message
        self.client.on_publish=self.on_publish
        self.client.connect(host='192.168.1.124',port=1883)
        self.client.subscribe(topic='ping',qos=2)

mqttclie=MQTTclient()
mqttclie.client.loop_start()
while True:
    #if ping('192.168.1.124'):
        #print ('Bonne connexion')
        
    #else:
        #LED(16).off()
        #print('Perte de connexion')
        #file=open('log.txt')
        #file.write(time.strftime("%H:%M:%S"))
        #file.close
        #sleep(5)
    MQTTclie.publish('cocheck')
    sleep(0.5)

