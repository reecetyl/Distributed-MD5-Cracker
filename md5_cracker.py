import hashlib
import sys
import string
import itertools
import socket
import json

dictionary_filepath = './dictionary.txt'

done = False

def crack_md5(solution, start, stop, path_to_dict_file):
    filename = open(path_to_dict_file)

    currentLine = 0
    while currentLine < start:
        filename.readline()
        currentLine += 1

    while currentLine < stop:

        m = hashlib.md5()
        line = filename.readline()[:-1]
        currentLine += 1
        m.update(line.encode())
        guess = m.hexdigest()
        print("Guessing: " + line)

        if guess == solution:
            return line

    return -1 # no solution found

def connect_to_server():

    host = socket.gethostname()
    port = 8080

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = "ready at " + host
    #print("sending message")
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()

    #print("Received from server: " + data)
    #print(type(data))
    data = data.split()
    hash = data[0]
    start = int(data[1])
    stop = int(data[2])

    answer = crack_md5(hash, start, stop, dictionary_filepath)

    if answer == -1:
        answer = "failure"

    client_socket.send((answer).encode())

    return answer

while True:
    ans = connect_to_server()
    if ans != "failure":
        break
