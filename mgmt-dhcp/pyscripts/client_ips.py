#!/usr/bin/env python3.6
from netmiko import ConnectHandler
from napalm import get_network_driver
from pprint import pprint as pp
import re

MGMT_ROUTER_IP="192.168.222.2"
USER="ansible"
PASSWORD="ansible"

get_network_driver('ios')
driver = get_network_driver('ios')
device = driver('192.168.222.2', 'ansible', 'ansible')
device.open()


res=device.get_arp_table()
#pp(device.get_arp_table())

# Extracts the ips from the arp table
res_list_ips = []
for i in range(len(res)):
	res_list_ips.append(res[i]['ip'])

regex = re.compile("^192\.168\.222\.\d{1,3}$")
res_list_ips = [i for i in res_list_ips if not regex.match(i)]

regex = re.compile("^10\.8\.11\.\1$")
res_list_ips = [i for i in res_list_ips if not regex.match(i)]


print(res_list_ips)

 

device.close()


