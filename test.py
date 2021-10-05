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



#------------create the class        
#config['topsecret.server.com'] = {}


#------------define confine class  as a new funktion
#topsecret = config['topsecret.server.com']


#-------------uses function
#topsecret['Port'] = '50022'     # mutates the parser
#topsecret['ForwardX11'] = 'yes'  # same here





#-------- connescts parameter FowardX11 to Default with the answer yes
#config['DEFAULT']['ForwardX11'] = 'no'





#--------write changes to config file
#with open('ripple.ini', 'w') as configfile:
#   config.write(configfile)







#-----mqqt call back definition
#def on_connect(client, userdata, flags, rc):
#    print("funktion on connect")
#    if rc==0:
#      print("connected ok")
#    else:
#        print ("No connection")






#-----instal mqtt
#pip install -U paho.mqtt.client --use






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

    print('before')

    time.sleep(3)
    
    print ('after')
    os.system("ping  google.com")