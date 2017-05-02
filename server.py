import socket
import sys
import subprocess


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8000)
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
                print ('sending data back to the client')
                c.send('Hello World !'.encode())
                #subprocess.run(["/feappv/ver31/main/feappv"])
            else:
                print ('no more data from', addr)
                break
            
    finally:
        c.close()
