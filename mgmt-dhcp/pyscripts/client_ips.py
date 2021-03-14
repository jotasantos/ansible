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

# remove from the list the gateway and 192.x addresses from the list
regex1 = re.compile("^192\.168\.222\.\d{1,3}$")
regex2 = re.compile("^10\.8\.11\.1$")
res_list_ips = [i for i in res_list_ips if not (regex1.match(i) or regex2.match(i))]

filel='/etc/hosts' 
hosts_result = {}
fileh = open(filel, 'w')
fileh.write('127.0.0.1	localhost\n127.0.1.1	ubuntu1804-pfne\nff02::1 ip6-allnodes\nff02::2 ip6-allrouters\n')
for i in range(len(res_list_ips)):
	device1 = driver(res_list_ips[i], 'ansible', 'ansible')
	device1.open()
	#hosts_result[res_list_ips[i]] = device1.get_facts()['fqdn']
	#print(device1.get_facts()['fqdn']+res_list_ips[i])
	fileh.write(res_list_ips[i] + " " + device1.get_facts()['fqdn'] + '\n')
	device1.close()
fileh.close()
