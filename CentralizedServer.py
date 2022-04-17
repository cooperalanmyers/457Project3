# Cooper Myers
# 4/18/21

import sys
import _thread
import socket

# Threading Examples:
# https://www.dev2qa.com/how-to-use-python-thread-example

# Creating Central Server
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddr = ('localhost', '2309')
socket.bind(serverAddr)
socket.listen()

# Users Table
userName = []
connectionSpeed = []
hostName = []

# Other Info
connections = [] # Used For Holding Connections
userList = []
currentUsers = []
allUsers = [] # Holding User Information
userFileDescriptions = []
fileDescriptions = []
author = []


def clientThread(connectionSocket):
    try:
        
        client = connectionSocket.recv(1024).decode() # Recieving Client Name
        client = client.split(" ") # Splitting Name by Spaces

        connections.append(connectionSocket) # Appending Socket Connection to Array
        userList.append(client[0]) # Appending Client to Array
        userList.append(client[1]) # Appending Client to Array
        userList.append(client[2]) # Appending Client to Array
        
        while True:
            data = connectionSocket.recv(1024).decode()
            command = data.split(" ")
        
            if data:

                # Do a keyword search.
                if command[0] == "KEYWORD_SEARCH":
                    term = command[1] # Term to Find
                    foundWho = ""

                    whoHasTerm = ";".join(s for s in fullDesc if term.lower() in s.lower())
                    whoHasTerm = whoHasTerm.split(";")

while True:
    print("Server is waiting for a connection!\n")
    
    connectionSocket, clientAddr = socket.accept()
    _thread.start_new_thread(clientThread, (connectionSocket,))

socket.close()




