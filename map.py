import socket
import time
de = time.time()
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



while True:
        #host = raw_input("IP or localhost : ")
        host = "10.101.200.28"
        x = raw_input("Min : ")
        y = raw_input("Max : ")

        x = int(x)
        y = int(y )+  1
		
        if x > y:
                print "min greater than max"
        else:
                break

print "Lancement test de ports : "

for i in range(x,y):
        print "Test connection : " + str(i)
        sock = socket.socket()
        res = sock.connect_ex((host, i))
        if res != 0:
                print "                 Port closed"
        else:
                print "                 Port opened       " + listPorts[str(i)]
        sock.close()

fi = time.time()
print "Operation finished in " + str( (fi - de)/1000  ) + " seconds"
