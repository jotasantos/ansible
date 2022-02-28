#!/lxhome/santosja/my_virtual_env/bin/python
from lib2to3.pgen2 import driver
from getpass import getpass
import sys
import time
import napalm
import os
import json

#SWITCHES = ['LDZOOBLL01','LDZOOBLL02','LDZOOBLL03']
SWITCHES = ['LDZSFCML01']

password = getpass(f"Tacacs password: ")
dev_type = 'nxos'
dev_creds={
    'hostname': 'LDZSFIML01',
    'username': 'santosja',
    'password': 'mypassword'
}

driver = napalm.get_network_driver(dev_type)

for switch in SWITCHES:
    dev_creds["hostname"] = switch
    conn = driver(**dev_creds)
    conn.open()
    output = conn.get_interfaces_ip()
    conn.close()
    svis = {key:val for key, val in output.items() 
        if key.startswith("Vlan")}
print(svis)
for item in svis.items():
    print(item[0],item[1]["ipv4"])
