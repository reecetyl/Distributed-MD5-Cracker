#!/bin/sh

sudo apt-get update

sudo pip3 install hashlib
sudo pip3 install itertools
sudo pip3 install ssocket
sudo pip3 install threading
sudo pip3 install flask
sudo pip3 install flask_socketio

sudo wget https://github.com/reecetyl/Distributed-MD5-Cracker/blob/master/server.py

sudo python3 server.py
