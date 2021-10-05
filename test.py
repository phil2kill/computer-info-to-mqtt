#------------ImportFiles
import configparser
import paho.mqtt.client as mqtt 
import time
import os
#------------add it as a executable function
config = configparser.ConfigParser()



#------------Donload file as readable/writeable
config.read('ripple.ini')


#------------prints all of the funktions in ripple
for section in config.sections():

    #---------print top class
    print(section)
    #---------once there is one top class we add the connected keys and contents and then jump to the next top class and repeat
    for key in config[section]:
        print (section,"-",key,"=",config[section] [key])




#--------paramters of mqtt server
client = mqtt.Client(config ['mqtt']["client-id"])

#-------check to seee if funktion client is working
#print("The type is : ",type(client))


#--------paramters of mqtt server
client.username_pw_set(config ['mqtt']["user"], config ['security']["key-value"])


#--------mqqtt call back funktion
#client.on_connect=on_connect


#--------connect to mqtt
client.connect(config ['mqtt']["broker"]) 






#--------loop to keep server published on certain operations
while True:
    
    client.publish("my-topic", "Hello" )
    client.publish(config ['mqtt']["topic-pub"], config["component"] ["uuid"] )


    time.sleep(3)
    
