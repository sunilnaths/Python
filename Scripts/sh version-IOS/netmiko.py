import napalm
import json
import os
import sys
import re
from log import ssh1
import netmiko
from netmiko import ConnectHandler

if len(sys.argv) < 3:
    print("File missing please try again")
    exit()

netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException,
                netmiko.ssh_exception.NetMikoAuthenticationException)
username, password = ssh1()

def connect():
    #####SSH to device, if sys.argv[1] is host#####
    if re.match (sys.argv[1],"host"):
        host = open ('host')
        for IP in host:
            cisco = {
            'device_type': 'cisco_ios',
            'host': IP,
            'username' : username,
            'password': password
            }
            net_connect = ConnectHandler(**cisco)
            print ('='*79)
            print ("Cisco Device IP...", IP )
            neighbor(net_connect)
            interface(net_connect)
    #####SSH to device, if sys.argv[1] is host#####
    elif re.match (sys.argv[1],"host1"):
        host = open ('host1')
        for IP in host:
            cisco = {
            'device_type': 'cisco_ios',
            'host': IP,
            'username' : username,
            'password': password
            }
            net_connect = ConnectHandler(**cisco)
            print ('='*79)
            print ("Cisco Device IP...", IP )
            neighbor(net_connect)
            interface(net_connect)

def neighbor (net_connect):
    #####show cdp neighbor#####
    output = net_connect.send_command('show cdp neighbor')
    print("-----------Cdp Neighbor-----------")
    output = output.splitlines()[3:]
    print ('\n'.join(output))
    print ('\n')

def interface (net_connect):
    #####Show IP interface brief####
    print("-----------Show IP interface-----------")
    output1 = net_connect.send_command('show ip int br')
    print (output1)

def main():
    connect()

if __name__ == '__main__':
    main()
