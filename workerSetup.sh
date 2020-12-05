#!/bin/sh

sudo apt update

sudo apt install python-pip

sudo pip install hashlib
sudo pip install itertools
sudo pip install socket
sudo pip install json

sudo python3 generate_dictionary.py 
