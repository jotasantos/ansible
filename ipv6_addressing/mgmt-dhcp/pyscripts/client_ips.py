#!/usr/bin/env python3.6
from netmiko import ConnectHandler
from napalm import get_network_driver
import re

MGMT_ROUTER_IP="192.168.222.2"
USER="ansible"
PASSWORD="ansible"
regex1 = re.compile("^192\.168\.222\.\d{1,3}$")
regex2 = re.compile("^10\.8\.11\.1$")
get_network_driver('ios')
driver = get_network_driver('ios')
device = driver('192.168.222.2', 'ansible', 'ansible')
device.open()

def arp_to_list():
	res=device.get_arp_table()
	res_list_ips = []
	for i in range(len(res)):
		res_list_ips.append(res[i]['ip'])
	# remove from the list the gateway and 192.x addresses from the list
	res_list_ips = [i for i in res_list_ips if not (regex1.match(i) or regex2.match(i))]
	print(res_list_ips) 
	return res_list_ips
def arp_to_host_file(arp_list):
    #filel = '/etc/hosts' 
	hosts_result = {}
	fileh = open("/etc/hosts", 'w')
	fileh.write('127.0.0.1	localhost\n127.0.1.1	ubuntu1804-pfne\nff02::1 ip6-allnodes\nff02::2 	ip6-allrouters\n')
	for i in range(len(arp_list)):
		device1 = driver(arp_list[i], 'ansible', 'ansible')
		device1.open()
		#hosts_result[arp_list[i]] = device1.get_facts()['fqdn']
		#print(device1.get_facts()['fqdn']+arp_list[i])
		fileh.write(arp_list[i] + " " + device1.get_facts()['fqdn'] + '\n')
		device1.close()
	fileh.close()

if __name__ == '__main__':
	arp_list = arp_to_list()
	arp_to_host_file(arp_list)
