#!/usr/bin/env python

import subprocess
import re

res = subprocess.run(["/usr/bin/nmcli", "device", "show"], stdout=subprocess.PIPE).stdout.decode('utf-8')
match_ipv6 = re.findall (r'IP6.ADDRESS.*', res)
for i in match_ipv6:
    print("ip address delete " + i.split()[1] + " dev wlp59s0")



