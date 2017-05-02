import socket               

def feappv(args):
    s = socket.socket()         
    host = "127.0.0.1"
    port = 8000 
    s.connect((host, port))
    s.send(args.encode()) 
    data = s.recv(1024).decode()
    print (data)
    
    s.close      
