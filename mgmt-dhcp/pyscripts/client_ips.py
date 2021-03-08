#!/usr/bin/env python3.6
from netmiko import ConnectHandler
from napalm import get_network_driver
from pprint import pprint as pp

MGMT_ROUTER_IP="192.168.222.2"
USER="ansible"
PASSWORD="ansible"

get_network_driver('ios')
driver = get_network_driver('ios')
device = driver('192.168.222.2', 'ansible', 'ansible')
device.open()


res=device.get_arp_table()

res_list_ips = []
for i in range(len(res)):
	res_list_ips.append(res[i]['ip'])
	
#pp(device.get_arp_table())
print ("The list of results :  "+ str(res_list_ips))
device.close()
