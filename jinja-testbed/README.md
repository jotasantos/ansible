# This is a place to test the jinja2 templates result before integrating them in more complex Ansible projects

## Overview
The current example configures a set of interface in the IOS boxes with the IPv6 and also add IS-IS configuration if present in the yml fileinformation 
This directory contains:

## Features
* `iface_isis.j2`   - Jinja2 template parsing ip into ios format as well as adding is-is configuration.
* `ansible.cfg`     - Ansible configuration file (sets connection and NAPALM plugin directory)
* `3-router.virl`   - 
* `setup.sh` - sets environment variables to select Ansible inventory and configuration files.

## ToDo

- Generate the NSAP ip from any arbitrary ipv4 loopback IP. At the moment we are using three octects with fix values (172.17.0) and then we use the last octect which varies from router to router
- Implement ipv6 addresses and ospv3 with ipv6 address family