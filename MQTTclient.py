import paho.mqtt.client as mqttc

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
        

    def on_publish(self,client, obj , mid):
        print("Publication reussie")

    def publish(self,payload):
        self.client.publish(topic='TOPIC',qos=2,payload=payload)

    def __init__(self):
        self.client=mqttc.Client(client_id='CLIENTID',clean_session=False)
        self.client.username_pw_set(username='USRNAME',password=None)
        self.client.on_connect=self.on_connect
        self.client.on_message=self.on_message
        self.client.on_publish=self.on_publish
        self.client.connect(host='IP',port=1883)
        self.client.subscribe(topic='NOMDUTOPIC',qos=2)