def fibo(ma):
    res=0
    a=0
    b=1
    c=0
    #shows first iteration
    print str(a) + " + " + str(b) + " = " +str( res)
    #while the resutl isn't achieved
    while res < ma:
        res=a+b
        print str(a) + " + " + str(b) + " = " +str( res)
        a=b
        b=res
		
ma=raw_input("Enter max range for fibo : ")
#set ma as integer
ma=int(ma)
#call fonction
fibo(ma)
