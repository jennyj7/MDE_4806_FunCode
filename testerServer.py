import socket

#Set host and port
HOST = '127.0.0.1'
PORT = 9990

#Create Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)

#update command line to show it is waiting for a connection
print("[Server 01] Waiting for a connection")

while (1):

    connection , address = s.accept()
    
    #recieve data from client
    command = connection.recv(1024)
    
    #update commannd line
    print("[Server 02] Connection accepted")
    print("[Server 03] Read data: ", command.decode())
            
    #Send data back to first raspberry pi
    contents = "LED On"
    connection.send(contents.encode())  
    connection.close()     
            
    #update command line
    print("[Server 08] Sent Information Back to Client")
    print("[Server 09] Waiting for a new connection")  
