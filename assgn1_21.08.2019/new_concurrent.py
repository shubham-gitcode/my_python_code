import socket
import sys
import threading
import traceback
from threading import Thread
from configparser import SafeConfigParser


#create a socket
def create_socket():
    try:
        global flag
        global host
        global port
        global sock
        flag = 0
        print("Creating server socket...")
        sock = socket.socket()
        print("Server socket created")

    except socket.error as msg:
        print("Socket Creation error : " + str(msg))


#Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global sock
        sock.bind((host,port))
        sock.listen()
        print("Ready to accept client request...")

    except socket.error as msg:
        print("Socket Binding error : " + str(msg))
        print("Retrying....")
        bind_socket()


#Handling connections from multiple clients
#And saving all the connections in an array
def accept_connection():
    # infinite loop- do not reset for every requests
    while True:
        connect,address = sock.accept()
       # ip, port = str(address[0]), str(address[1])
        print("Connected with " + str(address[0]) + ":" + str(address[1]))

        try:
            # Create thread of execution for each client request.
            Thread(target=accept_thread, args=(connect,address)).start()
        
        except:
            print("Connection not established.")
            traceback.print_exc()

    sock.close()


# Server logic for read, write communication 
def accept_thread(connect_client,addr):
    global flag
    thread_active = True

    while thread_active:  
        if flag == 0:
            print('Waiting for msg/req from client....')
        _input=connect_client.recv(1024).decode()
        
        if _input == 'exit':
            print("Client is requesting to quit")
            connect_client.close()
            print("Connection with " + str(addr[0]) + ":" + str(addr[1]) + " is closed")
            thread_active = False
         
        else:
            if flag==0:
                flag = 1
                print("Data from User " + str(addr[0]) + ":" + str(addr[1]) + "-->" + str(_input))

                _input = ''
                while len(_input) == 0:
                    _input = input("Echoing to " + str(addr[0]) + ":" + str(addr[1]) + "--> ")
                connect_client.send(_input.encode())  # send data to the client
                flag = 0
            else:
                _input = 'Server is busy...'
                connect_client.send(_input.encode())  # send busy notification to other client connections
               


#reading data from the config file
def read_configfile():
    global host
    global port
    global server
    parser = SafeConfigParser()
    parser.read('config.ini')

    host = parser.get('server_info', 'HOST')
    port = int(parser.get('server_info', 'PORT NO.'))


           
#sequential execution to establish two way communication with multiple clients
def main():
    read_configfile()
    create_socket()
    bind_socket()
    accept_connection()



#starting of program

main()

#end of program
