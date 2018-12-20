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
conf.verb = 0
resPort = []
listPorts = {
'21':'ftp',
'22':'ssh',
'23':'telnet',
'25':'smtp',
'69':'tftp',
'80':'http',
'88':'kerberos',
'109':'pop2',
'110':'pop3',
'115':'sftp',
'123':'ntp',
'137':'netbios-ns',
'138':'netbios-dgm',
'139':'netbios-ssn',
'143':'imap',
'161':'snmp',
'220':'imap3',
'389':'ldap',
'443':'https',
'445':'microsoft-ds',
'636':'ldaps',
'694':'ha-cluster',
'873':'rsync',
}

print "-" * 60
print "-" * 60

ART = """
 _____            _                                         
|_   _|          | |                                        
  | |_ __ _   _  | |_ ___     ___  ___  ___ __ _ _ __   ___ 
  | | '__| | | | | __/ _ \   / _ \/ __|/ __/ _` | '_ \ / _ \
  | | |  | |_| | | || (_) | |  __/\__ \ (_| (_| | |_) |  __/
  \_/_|   \__, |  \__\___/   \___||___/\___\__,_| .__/ \___|
           __/ |                                | |         
          |___/                                 |_|                                                                                               
        >   Author: ...
"""
print ART
print "-" * 60
print "-" * 60
print "\n"

#port min et port max
while True:
        #host = raw_input("IP or localhost : ")
        host = "<host to scan>"
        x = raw_input("Min : ")
        y = raw_input("Max : ")

        x = int(x)
        y = int(y )+  1
		
        if x > y:
                print "min greater than max"
        else:
                break

print 'Lancement tes de ports : '
de = time.time()
#boucle sur ports selected
for i in range(x,y):
        print "Test connection : " + str(i)
        p = IP()
        t = TCP()
        p.dst = host
        t.dport = i
        pack = p / t
        res = sr1(pack)
        #print res.flags
        #condition port ouvert
        if res['TCP'].flags == 'SA':
            #condition port dans la liste des protocoles
            if str(i)in  listPorts:
                print "     Port " + str(i)+ " open            " + listPorts[str(i)]
            else:
                print "     Port " + str(i)+ " open            "
            #liste port ouverts
            resPort.append(str(i))
            #increment ports ouverts
            ite = ite + 1
        else :
            print "     Port closed"


fi = time.time()
print str(ite) + " port(s) open : "

for j in  resPort:
    print j
    
print "\nOperation finished in " + str(fi - de ) + " seconds"    
