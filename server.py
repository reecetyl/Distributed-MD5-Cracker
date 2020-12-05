import hashlib
import sys
import string
import itertools
import socket
import threading
from flask import Flask, render_template, request
from flask_socketio import SocketIO

HOSTNAME = '0.0.0.0'
PORT = 8080

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'cs655'
socketio = SocketIO(app)
chunk_size = 1000
done_flag = False
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOSTNAME, PORT))
server.listen(5)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connection')
def connectionMessage(json):
    #print('Web portal connected: ' + str(json))
    clients.append(request.sid)
    #print(clients)

@socketio.on('submitted hash')
def submittedHash(json_message):
    #print('Submitted hash: ' + str(json_message))
    hash = json_message["data"]
    numWorkers = json_message["numWorkers"]
    # crack_hash(data)
    begin = 0
    stop = begin + chunk_size


    while not done_flag:
        server.listen(1)
        clientSocket, clientAddress = server.accept()
        newThread = ClientThread(hash, clientAddress, clientSocket, begin, stop)
        newThread.start()
        begin += chunk_size
        stop += chunk_size
    
class ClientThread(threading.Thread):
    def __init__(self, hash, clientAddress, clientSocket, begin, stop):
        threading.Thread.__init__(self)
        self.hash = hash
        self.clientAddress = clientAddress
        self.clientSocket = clientSocket
        self.begin = begin
        self.stop = stop
        #print("New Connection added: ", clientAddress)

    def run(self):
        # Receive ready message
        while True:
            data = self.clientSocket.recv(1024).decode()
            if "ready at" in data:
                self.clientSocket.send((self.hash + " " + str(self.begin) + " " + str(self.stop)).encode())
                break

        # Receive success or fail message
        while True:
            data = self.clientSocket.recv(1024).decode()
            if data and data != "failure":
                socketio.emit('solution', data, broadcast=True)
                global done_flag
                done_flag = True
                self.clientSocket.close()
                break
            elif data == "failure":
                break
        self.clientSocket.close()

        
if __name__ == '__main__':
    socketio.run(app)