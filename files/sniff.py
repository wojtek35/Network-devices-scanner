import scapy.all as scapy
from scapy.all import *
from configparser import ConfigParser
from win10toast import ToastNotifier
import time
import os
import sys



config = ConfigParser() # 
file = 'config.ini'
config.read(file)

def sniff_ips(ip_address):
    data = ''
    conf.verb = 0
    ether = Ether(dst="ff:ff:ff:ff:ff:ff") # create an Ethernet packet
    arp = ARP(pdst = ip_address) # create an ARP packet
    answer, unanswered = srp(ether/arp, timeout = 2) # send packets to the network and capture responses

    for sent, received in answer:
        data = received.summary() # save detected addresses to a variable
    return data