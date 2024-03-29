#!/usr/bin/env python3.6
from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException
from netmiko import NetmikoTimeoutException
from napalm import get_network_driver
import re

MGMT_ROUTER_IP="192.168.222.2"
USER="ansible"
PASSWORD="ansible"
regex1 = re.compile("^192\.168\.222\.\d{1,3}$")
regex2 = re.compile("^10\.8\.11\.1$")
#get_network_driver('ios')
driver_ios = get_network_driver('ios')
driver_junos = get_network_driver('junos')
driver_nxos = get_network_driver('nxos')
device_mgmt_rt = driver_ios('192.168.222.2', 'ansible', 'ansible')
device_mgmt_rt.open()

def arp_to_list():
	res=device_mgmt_rt.get_arp_table()
	res_list_ips = []
	for i in range(len(res)):
		res_list_ips.append(res[i]['ip'])
	# remove from the list the gateway and 192.x addresses from the list
	res_list_ips = [i for i in res_list_ips if not (regex1.match(i) or regex2.match(i))]
	device_mgmt_rt.close()
	print(res_list_ips)
	return res_list_ips


def arp_to_host_file(arp_list):
    #filel = '/etc/hosts' 
	hosts_result = {}
	fileh = open("/etc/hosts", 'w')
	fileh.write('127.0.0.1	localhost\n127.0.1.1	ubuntu1804-pfne\nff02::1 ip6-allnodes\nff02::2 	ip6-allrouters\n')
	for i in range(len(arp_list)):
		try:
			ip = arp_list[i]
			device_ios = driver_ios(ip, 'ansible', 'ansible')
			device_ios.open()
			fileh.write(ip + " " + device_ios.get_facts()['hostname'] + '\n')
			device_ios.close()
		except :
			print(f'Not responding as IOS for {ip}')
		try:
			ip = arp_list[i]
			device_junos = driver_junos(ip, 'ansible', 'Ansible')
			device_junos.open()
			fileh.write(ip + " " + device_junos.get_facts()['fqdn'] + '\n')
			device_junos.close()
		except:
			print(f'Not responding as JUNOS for {ip}')
		try:
			ip = arp_list[i]
			device_nxos = driver_nxos(ip, 'admin', 'admin')
			device_nxos.open()
			fileh.write(ip + " " + device_nxos.get_facts()['fqdn'] + '\n')
			device_nxos.close()
		except:
			print(f'Not responding as NXOS for {ip}')
	fileh.close()

if __name__ == '__main__':
	arp_list = arp_to_list()
	arp_to_host_file(arp_list)
