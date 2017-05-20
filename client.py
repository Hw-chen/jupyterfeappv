import socket     
import subprocess          
import os
import sys
from IPython.display import Image, display

s = socket.socket()         
host = "127.0.0.1"
port = 8000 
s.connect((host, port))


def feappv(arg):	

    s.send(arg.encode()) 
    data = s.recv(1024).decode()
    print (data)    

    s.close      

def feappvDraw():	


    s.send('picture'.encode()) 
    data = s.recv(1024).decode()
    display(Image(filename=data))    
    s.close      

