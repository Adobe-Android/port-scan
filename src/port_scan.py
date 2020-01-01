#!/usr/bin/env python

import socket
import os
import time
import sys

# Useful option for showing connection exceptions
debug_mode = False

def main():
    # Allows for graceful program exit when using Ctrl-C
    try:
        menu()
        while True:
            continue_program = input("  [+] Would you like to continue? (Y/N): ").lower()
            if continue_program == 'y' or continue_program == 'yes':
                clear()
                menu()                
            else:
                sys.exit()
    except KeyboardInterrupt:
        pass

def clear(): 
  
    # For Windows NT based systems
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # For POSIX systems (Linux, macOS, FreeBSD, OpenBSD, NetBSD, and more) 
    else: 
        _ = os.system('clear') 

def menu():
    print("##############################################")
    print("| Welcome to the Simple Python Port Scanner. |")
    print("|                Version 0.1                 |")
    print("##############################################")
    target = input(" [+] Enter Target IP: ")
    print("##############################################")
    print("| Choose one of the following options below. |")
    print("| (1.) Scan a single port                    |")
    print("| (2.) Scan a port range                     |")
    print("| (3.) Scan a list of ports                  |")
    print("##############################################")
    menu_opt1 = input("  Your choice: ")
    menu_opt2 = input("  What port(s) would you like to scan? ")
    print("##############################################")
    clear()

    if menu_opt1 == "1":
        end_position = int(menu_opt2) + 1
        test_ports_by_range(target, menu_opt2, end_position)
    elif menu_opt1 == "2":
        tmp_str = menu_opt2.split(',')
        start_position = int(tmp_str[0].strip())
        end_position = int(tmp_str[-1].strip()) + 1
        test_ports_by_range(target, start_position, end_position)
    elif menu_opt1 == "3":
        port_list = menu_opt2.split(',')
        trimmed_port_list = list(map(str.strip, port_list))
        test_specific_ports(target, trimmed_port_list)
    else:
        print("Well...that was unexpected.")
        print("Please choose from one of the options above.")

def test_specific_ports(target, port_list):
    
    for portNumber in port_list:
        print("Scanning port", portNumber, 'on IP address', target)
        if scanner(target, int(portNumber)):
            print('  [*] Port', portNumber, '/tcp','is open')
        else:
            print('  [*] Port', portNumber, '/tcp','is closed')

def test_ports_by_range(target, start_position, end_position):
    
    for portNumber in range(int(start_position), end_position):
        print("Scanning port", portNumber, 'on IP address', target)
        if scanner(target, portNumber):
            print('  [*] Port', portNumber, '/tcp','is open')
        else:
            print('  [*] Port', portNumber, '/tcp','is closed')

def scanner(target, port):
    try:
        # Properly creates a new socket for each test connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((target, port))
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        return True
    except Exception as e:
        if debug_mode == True:
            print(e)
        return False

if __name__ == "__main__":
    main()