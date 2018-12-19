# -*- coding: cp1252 -*-
def fibo(ma):
    res=0
    a=0
    b=1
    c=0
    #Affichage premier itération de la suite
    print str(a) + " + " + str(b) + " = " +str( res)
    #Tant que le résultat entré n'est pas atteint
    while res < ma:
        res=a+b
        print str(a) + " + " + str(b) + " = " +str( res)
        a=b
        b=res
		
ma=raw_input("Enter max range for fibo : ")
#set ma as integer
ma=int(ma)
#appelle fonction
fibo(ma)
