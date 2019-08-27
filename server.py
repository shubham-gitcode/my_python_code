import socket
from configparser import SafeConfigParser
import logging

logging.basicConfig(filename="single_server.log",
                    format='%(asctime)s %(message)s',filemode='w')

logger=logging.getLogger()

logger.setLevel(logging.DEBUG)

#creating socket for server
def create_socket():
    global host
    global port
    global server
    global connection_no
    
    try:
        server=socket.socket()
        print('Server Socket Created')
#    except socket.error as msg:
    except:
        logger.debug('Server socket creation failed')
        sys.exit()

#binding the server socket with host ip address and port no
def bind_socket():
    global host
    global port
    global server
    global connection_no
    
    try:
        server.bind((host, port))
        server.listen(connection_no)  # listen for client connection
    except:
        logger.debug('Binding Failed')
        sys.exit()


#accepting clients request to establish connection
def accept_connection():
    print('Waiting for Client connection...')
    client, address = server.accept() 
    print("Connection from : " + str(address) + "established")

    while True:
        print('Waiting for Msg/req from client....')
        data=client.recv(1024).decode()
        if data=='exit':
            print("Client requesting to terminate connection")
            break
        
        print("Data from user : " + str(address[0]) + "  " + str(address[1]) + " -> " + str(data))
        data = ''
        while len(data) == 0:
            data=input('Enter msg/req : ')
        client.send(data.encode())
    
    client.close()
    
    print('Connection terminated with client : ' + str(address))
    print('Server going down')

#reading data from the config file
def read_configfile():
    global host
    global port
    global server
    global connection_no
    parser = SafeConfigParser()
    parser.read('config.ini')

    host = parser.get('server_info', 'HOST')
    port = int(parser.get('server_info', 'PORT NO.'))
    connection_no = int(parser.get('server_info', 'Clients'))



# Sequentially placing the functions for every step 
#for connection establishment
def main():
    read_configfile()
    create_socket()
    bind_socket()
    accept_connection()


#starting of program

main()

#end of program
