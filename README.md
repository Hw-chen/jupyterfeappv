# jupyterfeappv
jupyter-feappv

To Build Docker Image 

docker build -t imageName .


To Run 

docker run -p 8888:8888 imageName


In Jupyter, start a new terminal and run 

python server.py


When using notebook, paste the client.py to start


Now feappv('someString') in notebook will send the string and for now, the server will return hello world ! 
