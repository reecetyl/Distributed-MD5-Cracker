import hashlib
import sys
import string
import itertools
import socket
from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cs655'
socketio = SocketIO(app)
chunk_size = 1000
clients = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connection')
def connectionMessage(json):
    print('Web portal connected: ' + str(json))
    clients.append(request.sid)
    print(clients)

@socketio.on('submitted hash')
def submittedHash(json_message):
    print('Submitted hash: ' + str(json_message))
    data = json_message["data"]
    numWorkers = json_message["numWorkers"]
    crack_hash(data)

def crack_hash(hash):
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('0.0.0.0', 8080))
    serv.listen(5)
    print("server setup at ")
    conn, addr = serv.accept()
    print("Connection from: " + str(addr))
    while True:
        data = conn.recv(1024).decode()
        if "ready at" in data:
            conn.send((hash + " 0" + " 380204032").encode())
            break # remove later when multiple clients
    
    # listen for response from client (success or failure)
    while True:
        data = conn.recv(1024).decode()
        if "Success! " in data:
            print(data)
            break
    solution = data.split()[1]

    socketio.emit('solution', solution, broadcast=True)
    conn.close()





if __name__ == '__main__':
    socketio.run(app)