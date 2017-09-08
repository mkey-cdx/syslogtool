#!/usr/bin/python3

import socket
import os
import shutil
import configparser

# Get config data.
config = configparser.ConfigParser()
config.read("server.ini")

port = int(config.get("Config", "port"))
file_name = config.get("Config", "file_name")
file_path = config.get("Config", "file_path")
tmp_path = config.get("Config", "tmp_path")


# Initialize server socket.
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', port))
socket.listen(5)
print("Server listening on port:", port)

# Main loop.
while True:
    client, address = socket.accept()
    print("{} is connected".format( address ))
    request = client.recv(255)

    # Check client request.
    if ( request == b'GET_LOG' ):
        print("Received GET_LOG request")

        # Copy file and notify client.
        try:
            shutil.copy2(file_path + file_name, tmp_path)
        except FileNotFoundError:
            client.send(b'KO')
            print("ERROR: file not found. Check .ini file")
            continue
     
        print("File provided in", tmp_path)               
        client.send(b'OK')

        # Clean temp folder if downloaded.
        request = client.recv(255)
        if (request == b'OK'):
            os.remove(tmp_path + file_name)
            print("Cleaned temp folder")

    client.close()

socket.close()
