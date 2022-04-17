# Multithreaded FTP Server
# 3/23/31
# Cooper Myers
# CIS 457 Data Communications

import socket
import struct
import random
import time

server_ip = 'localhost'
server_port = 2309
buffer_size = 1024

# Creating Client Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

new_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect Method From Client Input
def connect():
    print ("CONNECT <server name/IP address> <server port>")
    connectionData =  input()

    separator = ' '
    connectTemp = connectionData.split(separator, -1)

    paramOne = 'CONNECT'
    connectIP = '127.0.0.1' if connectTemp[1] == 'localhost' else connectTemp[1]
    
    connectPort = connectTemp[2]

    # If Client Says "CONNECT" Then Connect
    if connectTemp[0].upper() == paramOne: 
        client_socket.connect((connectIP, int(connectPort)))
        client_socket.send(paramOne.encode('utf-8'))
        
        time.sleep(3)
        
        client_socket.send(new_server_port.encode('utf-8'))
        
        #newData = client_socket.recv(buffer_size).decode('utf-8')
        #print(newData)
        
        
# Anything Below is the Client Menu that Automatically Prompts


print ("""\n\nWelcome to the P2P client.
        \n\nCall one of the following functions:
        \nCONNECT           : Connect to server
        \nRETR              : Retrieve file
        \nQUIT              : Exit\n""")

while True:

    # Listen for a command
    prompt = input("\nEnter a command: ")
       
    if prompt[:7].upper() == "CONNECT":
        connect()

    elif prompt[:4].upper() == "RETR":
        retr()
        
    elif prompt[:4].upper() == "QUIT":
        quit()
    
    else:
        print ("Command not recognized; please try again")
