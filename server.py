#!/usr/bin/python3

import socket
import os
import shutil
import configparser

# Get config data
config = configparser.ConfigParser()
config.read("server.ini")

port = int(config.get("Server", "port"))
file_name = config.get("Server", "file_name")
file_path = config.get("Server", "file_path")
tmp_path = config.get("Server", "tmp_path")


# Initialize server socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', port))
socket.listen(5)
print("Server listening on port:", port)

# Main loop
while True:
    client, address = socket.accept()
    print("{} is connected".format( address ))
    request = client.recv(255)

    # Check client request
    if ( request == b'GET_LOG' ):
        print("Received GET_LOG request")
        # Copy syslog file and notify client
        shutil.copy2(file_path + file_name, tmp_path)
        client.send(b'OK')
        print("File provided in", tmp_path)

        # Clean temp folder if downloaded
        request = client.recv(255)
        if (request == b'OK'):
            os.remove(tmp_path + file_name)
            print("Cleaned temp folder")

    client.close()

socket.close()
