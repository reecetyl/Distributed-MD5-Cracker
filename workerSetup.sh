#!/bin/sh

sudo apt update

sudo apt install python3-pip

sudo pip3 install hashlib
sudo pip3 install itertools
sudo pip3 install socket
sudo pip3 install json

sudo python3 generate_dictionary.py 
