from temps import temps
from temps import random_string
import socket
import time

#host = "localhost"
#port = 6996 

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#creates socket with socket object s;
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#s.bind((host,port))
#s.listen(2)

#clientsocket, address = s.accept()
#print(f"Connection from {address} has been done")
####clientsocket.send(bytes("Welcome to server\n","utf-8"))

#while True:
#    msg = temps()
#    clientsocket.send(bytes(msg,"utf-8"))
#    time.sleep(1)


import paho.mqtt.client as paho
broker="iot.eclipse.org"
port=1883
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
                   

while True:
    msg = temps()
    ret= client1.publish("LocationDataMrinq",bytes(msg,"utf-8"))          #publish and location data is topic name
    time.sleep(1)
