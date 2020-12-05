#!/bin/sh

sudo apt update


sudo apt install python3-pip
sudo apt install git

sudo pip3 install hashlib
sudo pip3 install itertools
sudo pip3 install ssocket
sudo pip3 install threading
sudo pip3 install flask
sudo pip3 install flask_socketio

sudo python3 server.py
