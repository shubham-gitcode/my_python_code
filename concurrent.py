import socket
import sys
import threading
import traceback
from threading import Thread
from configparser import SafeConfigParser
import logging

#creating n configriing logger
logging.basicConfig(filename="concurrent_server.log"
                    format='%(asctime)s %(message)s',filemode='w')

logger=logging.getLogger()

logger.setLevel(logging.DEBUG)


#create a socket
def create_socket():
    try:
        global host
        global port
        global sock
        print("Creating server socket...")
        sock=socket.socket()
        print("Server socket created")

    except socket.error as msg:
        logger.debug("Socket Creation error : " + str(msg))
        sys.exit()


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
        logger.debug("Socket Binding error : " + str(msg))
        logger.debug("Retrying....")
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
            logger.debug("Connection established failed.")
            traceback.print_exc()

    sock.close()


# Server logic for read, write communication 
def accept_thread(connect_client,addr):
    thread_active = True
  
    while thread_active:  
        _input=connect_client.recv(1024).decode()
        
        if _input == 'exit':
            print("Client is requesting to quit")
            connect_client.close()
            print("Connection with " + str(addr[0]) + ":" + str(addr[1]) + " is closed")
            thread_active = False
        
        else:
            print("Data from User " + str(addr[0]) + ":" + str(addr[1]) + "-->" + str(_input))
            
            _input = ''
            while len(_input) == 0:
                _input = input("Echoing to " + str(addr[0]) + ":" + str(addr[1]) + "--> ")
            connect_client.send(_input.encode())  # send data to the client

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
