import re
from hashlib import md5
from socket import socket

HOST = "saturn.picoctf.net"
PORT = 50561

# Create a socket and connect to the challenge
sock = socket()
sock.connect((HOST, PORT))

# Let's loop!
while True:

    # Receive the data
    data = sock.recv(1024).decode()
    print("DATA = ", data)

    # If "picoCTF" is in the data, we likely have the flag so break the loop
    if "picoCTF" in data:
        break

    # Use regex to search and capture the phrase between the quotes
    phrase = re.search("'(.*)'", data)
    #print("PHRASE=", data)
    match = phrase.group(1)
    #print("MATCH=", match)

    # Calculate the MD5 and send it back!
    hashed = md5(match.encode()).hexdigest()
    sock.send(hashed.encode() + b"\n")

    # Print out the "correct" response string
    print(sock.recv(1024))
