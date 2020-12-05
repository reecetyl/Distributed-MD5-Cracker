#!/bin/sh

sudo apt update

sudo pip3 install hashlib
sudo pip3 install itertools
sudo pip3 install socket
sudo pip3 install json

sudo wget https://github.com/reecetyl/Distributed-MD5-Cracker/blob/master/md5_cracker.py

sudo wget https://github.com/reecetyl/Distributed-MD5-Cracker/blob/master/generate_dictionary.py

sudo python3 generate_dictionary.py 
