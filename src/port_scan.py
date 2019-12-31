#!/usr/bin/env python

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
    print("##############################################")
    print("| Welcome to the Simple Python Port Scanner. |")
    print("##############################################")
    target = input("[+] Enter Target IP: ")
    print("Choose one of the following options below.")
    print("(1) Specify a single port")
    print("(2) Specify a port range")
    print("(3) Specify a list of ports")
    menu_opt1 = input("Your choice: ")
    menu_opt2 = input("What port(s) would you like to scan? ")

    if menu_opt1 == "1":
        single_port(target, menu_opt2)
    elif menu_opt1 == "2":
        pass
    elif menu_opt1 == "3":
        pass
    else:
        print("Well...that was unexpected.")

def single_port(target, port):
    for portNumber in range(int(port), int(port) + 1):
        print("Scanning port", portNumber)
        if scanner(target, portNumber):
            print('[*] Port', portNumber, '/tcp','is open')
        else:
            print('[*] Port', portNumber, '/tcp','is closed')

def scanner(target, port):
    try:
        sock.connect((target, port))
        return True
    except:
        return False

if __name__ == "__main__":
    main()