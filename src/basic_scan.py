#!/usr/bin/env python

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input("[+] Enter Target IP: ")
# port = input("[+] Port, port range, or selected port list: ")

def scanner01(port):
    try:
        sock.connect((target, port))
        return True
    except:
        return False

for portNumber in range(22, 25):
    print("Scanning port", portNumber)
    if scanner01(portNumber):
        print('[*] Port', portNumber, '/tcp','is open')