#!/bin/sh

sudo update


sudo apt install python-pip
sudo apt install git

sudo pip install hashlib
sudo pip install itertools
sudo pip install ssocket
sudo pip install threading
sudo pip install flask
sudo pip install flask_socketio

sudo python3 server.py
