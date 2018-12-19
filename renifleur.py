#imports
from scapy.all import *
import time
import os
clear = lambda: os.system('cls')
clear()
#declare de variables
ite = 0
i = 0
t = 0
p =0
resPort = []
conf.verb=0
print "-" * 60
print "-" * 60

print "-" * 60
print "-" * 60
print "\n"
def httpHeader(packet):
        httpPacket = str(packet)
        test = httpPacket.find('POST')
        if test != -1:
            print str(bytes(packet[TCP].payload))
        
sniff(prn=httpHeader, filter="tcp port 80")
