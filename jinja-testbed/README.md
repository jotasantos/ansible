# This is a place to test the jinja2 templates result before integrating them in more complex Ansible projects

## Overview
The current example configures a set of interface in the IOS boxes with the IPv6 and also add IS-IS configuration if present in the yml fileinformation 
This directory contains:

## Features
* `iface_isis.j2`   - Jinja2 template parsing ip into ios format as well as adding is-is configuration.
* `ansible.cfg`     - Ansible configuration file 
* `iface_isis.yml`  - Variables file with cidr and isis information for a single, test, device.
* `results.txt`     - The result ios configuration from parsing the j2 file.


## Usage
We parse the template with the following command. Note the ``template`` variable is required so vars_filem src and dst for the templating is determined:
```ansible-playbook test-jinja.yml --extra-vars template="iface_isis"```

## ToDo

- Generate the NSAP ip from any arbitrary ipv4 loopback IP. At the moment we are using three octects with fix values (172.17.0) and then we use the last octect which varies from router to router
- Implement ipv6 addresses and ospv3 with ipv6 address family