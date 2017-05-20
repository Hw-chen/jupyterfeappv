import socket
import sys
import subprocess
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("127.0.0.1", 8000)
print ('starting up on %s port %s' % server_address)
s.bind(server_address)

s.listen(5)

while True:

    print ('waiting for a connection')
    c, addr = s.accept() 
    try:
        print ('connection from', addr)
        while True:
            data = c.recv(1024)
            print ('received "%s"' % data )
            if data:
                data = data.decode()
                print ('sending data back to the client')
                print (data)
                if data == 'picture':
                    path = os.path.abspath('example.jpg')
                    print (path)
                    c.send(path.encode())
                else:
                    print ('here')
                    c.send('Hello World !'.encode())                 
                #subprocess.run(["/feappv/ver31/main/feappv"])
            else:
                print ('no more data from', addr)
                break
            
    finally:
        c.close()
