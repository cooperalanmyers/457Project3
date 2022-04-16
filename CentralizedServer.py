# Cooper Myers
# 4/18/21

import sys
import _thread
import socket

# Threading Examples:
# https://www.dev2qa.com/how-to-use-python-thread-example/#:~:text=Use%20Python%20_thread%20Module.%201%20The%20example%20module,start%20a%20new%20thread.%20...%20More%20items...%20



socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverAddr = ('localhost', '2309')
socket.bind(serverAddr)
socket.listen()




# Users Table

userName = []
connectionSpeed = []
hostName = []

# Other Info

currentUsers = []
fileDescriptions = []







while True:
    print("Server is waiting for a connection!\n")
    
    connectionSocket, clientAddr = socket.accept()
    _thread.start_new_thread(clientThread, (connectionSocket,))

socket.close()




