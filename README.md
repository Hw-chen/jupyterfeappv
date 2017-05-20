# jupyterfeappv
jupyter-feappv

To Build Docker Image 

docker build -t imageName .

To Run 

docker run -p 8888:8888 imageName


In Jupyter, frirst run server.py in a new terminal 

When using notebook, import client to use methods 


client.feappv('someString') in notebook will now send the string to server, and the server will return hello world ! 
client.feappvDraw() will dispaly an example image on notebook
