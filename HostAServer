# Multithreaded P2P Server
# 4/17/21
# Cooper Myers
# CIS 457 Data Communications

import socket
import threading
import sys
import os
import struct
import time


# Beginning Message to Server
print ("\nFTP server is running.\n\nTo begin, connect a client.\n")

# Storing Server Data Information
server_ip = 'localhost'
server_port = 2309
BUFFER_SIZE = 1024

# Creating Server Socket, Binding, then Listening
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))

server_socket.listen()
print("The Server is ready to recieve!")

def command_menu(connection_socket):
    
    while True:
           print ("\n\nWaiting for instruction")
           data = connection_socket.recv(BUFFER_SIZE).decode('utf-8')
      
           dataParam = data.split()
           # dataParam[0] is the command
           # dataParam[2] is the location
      
           # Print Requested Command to Screen
           print ("\nRecieved instruction: {}".format(dataParam[0]))
    
           # If Command Matches go to Following Helper Method
           if dataParam[0] == "RETR":
               retr(dataParam[2])            
               
           elif dataParam[0] == "QUIT":
               quit()
       
       
def quit():
    # Close the server
    connection_socket.close()
    print("Successfully disconnected from client")
    return

def retr(fileName): 
    
    files = [file for file in os.listdir('.') if os.path.isfile(file)]
    
    for file in files:
        if file == fileName:
            fileName = os.path.join(os.getcwd(), fileName)
            document = open(str(fileName), 'rb')
            openDocument = document.read()
            
        if not isinstance(openDocument, bytes):
            connection_socket.send(openDocument.encode('utf-8'))
        else:
            connection_socket.send(openDocument)
            
    return

while True:
    connection_socket, addr = server_socket.accept()
    threading.Thread(target=command_menu, args=(connection_socket,)).start()
