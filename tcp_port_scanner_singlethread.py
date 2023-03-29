#!/usr/bin/env python3

""" Scan a range of port numbers on host one by one and time how long it takes using single threaded process in python. """
__author__ = 'Chris Weaver'

# Import time to mesure time
import time
# Imports AF_INET = IPV4
from socket import AF_INET
# Imports SOCK_STREAM = TCP
from socket import SOCK_STREAM
# Imports socket function
from socket import socket
 
# returns True if a connection can be made, False otherwise
def test_port_number(host, port):
    # create and configure the socket
    with socket(AF_INET, SOCK_STREAM) as sock:
        # set a timeout of a few seconds
        sock.settimeout(0.5)
        # connecting may fail
        try:
            # attempt to connect
            sock.connect((host, port))
            # a successful connection was made
            print(f'Connected to: {host}:{port}')
            return True
        except:
            # ignore the failure
            print(f'failed to connect to: {host}:{port}')
            return False
 
# scan port numbers on a host
def port_scan(host, ports):
    print(f'Scanning {host}...')
    # scan each port number
    for port in ports:
        # If return is true prints open text
        if test_port_number(host, port):
            print(f'> {host}:{port} open')
 
# define host and port numbers to scan
HOST = 'scanme.nmap.org'
PORTS = range(65535)

# start timer for metrics
start = time.perf_counter()

# Test host and port open.
port_scan(HOST, PORTS)

# finish timer for metrics
finish = time.perf_counter()
# Print scan time.
print(f'scan completed in {finish - start:0.4f} seconds')