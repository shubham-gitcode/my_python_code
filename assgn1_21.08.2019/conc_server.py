from multiprocessing import Process
import os
import socket
import sys

HOST='0.0.0.0'
PORT=input('Enter port No.: ')
data=''

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,int(PORT)))
server.listen()

while True:
    print('Waiting to accept client connection...')
    client, caddr=server.accept()
    print(caddr)
    print("Connected from : " + str(caddr))
    if os.fork()==0:
        while data!='exit':
            print("Waiting for msg/req from client...")
            data=client.recv(1024).decode()
            if not data:
                print("Client Abnormally terminated")
                break
            else:
                print("From connected user -> " + str(data))
                client.send(data.encode())
                if data == 'exit':
                    print("Client Formally Terminating connection")
                    break
        
        client.close()
        print(caddr)

print("Server Going Down")
server.close()
