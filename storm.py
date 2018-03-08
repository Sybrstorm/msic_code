#!/bin/python env
import os
#import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
#from ElementTree_pretty import prettify

## Text menu in Python

def print_menu():       ## Your menu design here
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Create VM Network"
    print "2. Create VMs"
    print "3. Show VM Networks"
    print "4. Show VMs"
    print "99. Exit"
    print 67 * "-"

loop=True

while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-4 or 99]: ")

    if choice==1:
        os.system('clear')
        print "You have selected to create a new VM netowork."
        print ""
        print "Define the name of the network: "
        name = raw_input("Network Name: ")
        print "You define your network name as: %s" %(name)
        print ""
        print "Define the network bridge: "
        br = raw_input("Network Bridge: ")
        print "You defined the network bridge as: %s" % (br)
        print "Define the IP address of the network"
        ip = raw_input("IP Address: ")
        print "You defined the IP address as: %s" % (ip)
        print ""
        print "Define netmask"
        netmask = raw_input("Netmask: ")
        print "You defined the netmask as: %s" % (netmask)
        print ""
        print "Define DHCP Start"
        start = raw_input("DHCP start: " )
        print "You defined the start of the DHCP scope as: %s" % (start)
        print ""
        print "Define DHCP Scope End"
        end = raw_input("DHCP Scope End: ")
        print "You defined the end of the DHCP scope as: %s" % (start)
        print ""
        print ""
        print "Network Defined Below"
        print "~~~~~~~~~~~~~~~~~~~~~"
        print ""
        print "Network Name: %s" % (name)
        print "Network Bridge: %s:" % (br)
        print "Network IP: %s" % (ip)
        print "Network DHCP start: %s end: %s" % (start, end)
        print "~~~~~~~~~~~~~~~~~~~~~"
        print ""
        print "Writing network configuration to file"

        network = Element('network')

        net_name = SubElement(network, 'name')
        net_name.text = '%s' % (name)

        uuid = SubElement(network, 'uuid')

        br_id = SubElement(network, 'bridge', name=br, stp='on', delay='0')

        mac = SubElement(network, 'mac', address='')

        domain = SubElement(network, 'domain', name=name)

        ip = SubElement(network, 'ip', address=ip, netmask=netmask)

        dhcp = SubElement(ip, 'dhcp')

        range = SubElement(dhcp, 'range', start=start, end=end)

        with open('%s.xml' % (name), 'a') as write_file:
                write_file.write(tostring(network))

        os.system('virsh net-define %s.xml' % (name))
        os.system('virsh net-start %s' % (name))
        os.system('virsh net-autostart %s' % (name))
        ## You can add your code or functions here
    elif choice==2:
        os.system('clear')
        print "You have selected to create a new VM."
        ## You can add your code or functions here
    elif choice==3:
        os.system('clear')
        print "You have selected to list all available networks."
        ## You can add your code or functions here
    elif choice==4:
        os.system('clear')
        print "You have selected to list all available VMs."
        ## You can add your code or functions here
    elif choice==99:
        print "You have selcted to exit"
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")
