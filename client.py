import socket
from configparser import SafeConfigParser
import logging

#creating n configriing logger
logging.basicConfig(filename="client.log",
                    format='%(asctime)s %(message)s',filemode='w')

logger=logging.getLogger()

logger.setLevel(logging.DEBUG)


#creating client socket
def create_socket():
    global host
    global port
    global client
    try:
        client=socket.socket()
        print('Client Socket created')
    except:
        logger.debug("Client Socket creation failed")
        sys.exit()
    

#connecting the client with server 
def connect_server():
    global host
    global port
    global client
    
    client.connect((host, port))
    message=''
    
    while True:
        message = ''
        while len(message) == 0:
            message=input('Enter message -> ')
        client.send(message.encode())
        if message=='exit':
            break
        print('Waiting for msg reply from server...')
        data=client.recv(1024).decode()
        print('Received from server: ' + data)

    client.close()
    print('Connection with Server terminated')


#reading data from the config file
def read_configfile():
    global host
    global port
    global server
    try:
       parser = SafeConfigParser()
       parser.read('config.ini')

       host = parser.get('client_info', 'host')
       port = int(parser.get('client_info', 'PORT NO.'))
    except:
        logger.debug("Config File not opened or created")
        sys.exit()

#sequentially adding the codes to exceute
def main():
    read_configfile()
    create_socket()
    connect_server()


#starting of program

main()

#end of program


