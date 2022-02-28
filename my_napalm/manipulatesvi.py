#!/usr/bin/env python
from lib2to3.pgen2 import driver
import sys
from termios import IEXTEN
import time
import napalm
import os
import json

output = {'Vlan100': {'ipv4': {'10.0.34.204': {'prefix_length': 31}}}, 'Vlan723': {'ipv4': {'10.3.1.251': {'prefix_length': 24}}}, 'Vlan724': {'ipv4': {'10.3.2.251': {'prefix_length': 24}}}, 'Vlan748': {'ipv4': {'192.168.1.0': {'prefix_length': 31}}}, 'Vlan998': {'ipv4': {'169.254.21.66': {'prefix_length': 29}}}, 'loopback0': {'ipv4': {'10.0.32.15': {'prefix_length': 32}}}, 'Ethernet1/49': {'ipv4': {'10.0.34.122': {'prefix_length': 31}}}}

svis = {key:val for key, val in output.items() 
    if key.startswith("Vlan")}


print(svis)
for item in svis.items():
    print(item[0],item[1]["ipv4"])
