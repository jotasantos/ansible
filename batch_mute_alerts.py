#!/usr/bin/env python2

import requests
import getpass
from sys import exit

USER = "api"
PASSWORD = getpass.getpass("Enter password for user [%s]: " % USER)

API_BASE_URL = "http://observium01.lhr.whatever.co.uk/api/v0/"
ALERTS_URL = API_BASE_URL + "alerts"


def get_all_alerts():
    """ Returns a list of all alerts """
    print ("> Retrieving alerts from %s" % ALERTS_URL)
    r = requests.get(
            ALERTS_URL,
            headers={'Accept': 'application/json'},
            auth=(USER, PASSWORD)
            )

    if r.status_code == 200:
        alerts = r.json().get('alerts',[])
        # pop OK ones
        for id in alerts.keys():
            if alerts[id]['status'] != 'FAILED':
                alerts.pop(id)
        count = len(alerts)

        if count:
            print ("> Retrieved %d alerts in FAILED status.\n") % count
            exceptions = raw_input("Enter alert IDs to exclude in csv (e.g. 12345,23456,34567): ")
            if exceptions:
                ids = exceptions.strip().strip(',').replace(' ', '').split(',')
                for id in ids: # verify entered IDs
                    if alerts.get(id) is None:
                        print ("> Alert ID not found: %s" % id)
                    else:
                        alerts.pop(id)
                        print ("> Excluded alert %s" % id)
            return alerts
        else:
            return []
    else:
        print ("Failed to retrieved alerts:", r.status_code, URL)
        return []


# def ignore_alert(id):
#     """ Set ignore_until_ok = 1 for given alert ID """
#     r = requests.put(
#             ALERTS_URL + '/%s/' % id,
#             json={'ignore_until_ok':'1'},
#             auth=(USER, PASSWORD)
#             )
#     if r.status_code == 200:
#         print "Alert %s: ignore_until_ok = 1" % id
#     else:
#         print "Failed to ignore alert %s:" % id, r.status_code

def ignore_alert(id):
    """ Set ignore_until_ok = 1 for given alert ID """
    r = requests.put(
            ALERTS_URL + '/%s/' % id,
            json={'ignore_until':'2035-01-02 12:00:00'},
            auth=(USER, PASSWORD)
            )
    if r.status_code == 200:
        print ("Alert %s: ignore_until = 2035-01-02 12:00:00" % id)
    else:
        print ("Failed to ignore alert %s:" % id, r.status_code)


def mock_ignore_alert(id):
    """ Set ignore_until_ok = 1 for given alert ID """
    print ("Alert %s: ignore_until_ok = 1" % id)


def ignore_all_by_id(alerts):
    """ Loop ignore given alerts """
    total = len(alerts)
    current = 1

    print ("")
    answer = raw_input("Confirm set %d alerts to ignore_until 2035-01-02 12:00:00 ? [y/n]: " % total)

    if answer in "yY":
        pass
    else:
        print ("Exit.")
        exit(0)

    for id in alerts.keys():
        #print "%d/%d" % (current, total),
        ignore_alert(id)
        current += 1


if __name__ == '__main__':
    ignore_all_by_id(get_all_alerts())
