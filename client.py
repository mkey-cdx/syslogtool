#!/usr/bin/python3

import socket
import os
import configparser

# Get config data.
config = configparser.ConfigParser()
config.read("client.ini")

host = config.get("Config", "host")
port = int(config.get("Config", "port"))
file_path = config.get("Config", "file_path")
file_name = config.get("Config", "file_name")
user = os.environ['USER']


# Initialize client socket.
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))
print("Connected on {}".format(port))

# Send GET_LOG request.
socket.send(b'GET_LOG')

# Get server response.
response = socket.recv(255)

if (response == b'OK'):
    # File provided. Execute rsync to get it.
    print("File provided on server. Downloading...")
    os.system(str.format("rsync -vz -e ssh {0}@{1}:{2}{3} .", user, host, file_path, file_name))
    socket.send(b'OK')
elif (response == b'KO'):
    print("ERROR: file not found. Check .ini file")

socket.close()
print("Connection closed")

