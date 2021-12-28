# -*- coding: utf-8 -*-
#!/bin/env python3
# Modified by shakida
# Telegram ac: http://t.me/shakida69
# Please give me credits if you use any codes from here.


import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print(f"""
	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
	{re}╚═╗{cy}├┤  │ │ │├─┘
	{re}╚═╝{cy}└─┘ ┴ └─┘┴
                   V1.4
        Modified by shakida | https://t.me/shakida69
	""")
banner()
print(gr+"[+] Installing requierments ...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()
os.system("touch config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[+] Enter API ID : "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+] Enter Hash : "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] Enter Phone Number with country code: "+re)
cpass.set('cred', 'phone', xphone)
xsleep = input(gr+"[+] Enter sleep time in sec: "+re)
cpass.set('cred', 'sleeptime', xsleep)
with open('config.data', 'w') as setup:
	cpass.write(setup)
print(gr+"[+] Setup completed!")
