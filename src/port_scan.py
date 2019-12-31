#!/usr/bin/env python

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
    print("##############################################")
    print("| Welcome to the Simple Python Port Scanner. |")
    print("##############################################")
    target = input(" [+] Enter Target IP: ")
    print("##############################################")
    print("| Choose one of the following options below. |")
    print("| (1.) Specify a single port                 |")
    print("| (2.) Specify a port range                  |")
    print("| (3.) Specify a list of ports               |")
    print("##############################################")
    menu_opt1 = input("  Your choice: ")
    menu_opt2 = input("  What port(s) would you like to scan? ")
    print("##############################################")

    if menu_opt1 == "1":
        end_position = int(menu_opt2) + 1
        test_ports(target, menu_opt2, end_position)
    elif menu_opt1 == "2":
        text = menu_opt2.split(',')
        start_position = int(text[0].strip())
        end_position = int(text[-1].strip()) + 1
        test_ports(target, start_position, end_position)
    elif menu_opt1 == "3":
        pass
    else:
        print("Well...that was unexpected.")

def test_ports(target, port, end_position):
    
    for portNumber in range(int(port), end_position):
        print("Scanning port", portNumber, 'on IP address', target)
        if scanner(target, portNumber):
            print('  [*] Port', portNumber, '/tcp','is open')
        else:
            print('  [*] Port', portNumber, '/tcp','is closed')

def scanner(target, port):
    try:
        sock.connect((target, port))
        return True
    except:
        return False

if __name__ == "__main__":
    main()