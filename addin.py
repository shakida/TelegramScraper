#!/bin/env python3
# Modified by shakida
# Telegram ac: http://t.me/shakida69
# Please give me credits if you use any codes from here.

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, UserChannelsTooMuchError, UserIdInvalidError, FloodWaitError
from telethon.tl.functions.channels import InviteToChannelRequest
import configparser
import os, sys
import csv
import traceback
import time
import random

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

def banner():
    print(f"""
{re}╔╦╗{cy}┌─┐┬  ┌─┐{re}╔═╗  ╔═╗{cy}┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
{re} ║ {cy}├┤ │  ├┤ {re}║ ╦  ╚═╗{cy}│  ├┬┘├─┤├─┘├┤ ├┬┘
{re} ╩ {cy}└─┘┴─┘└─┘{re}╚═╝  ╚═╝{cy}└─┘┴└─┴ ┴┴  └─┘┴└─

            Version: 1.4
     Modified by shakida69 | https://t.me/shakida
        """)

cpass = configparser.RawConfigParser()
cpass.read('config.data')

try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    SLEEPING = cpass['cred']['sleeptime']
    client = TelegramClient(phone, api_id, api_hash)
except KeyError:
    os.system('clear')
    banner()
    print("\033[91m[!] Please run \033[92mpython3 setup.py\033[91m first !!!\n")
    sys.exit(1)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    os.system('clear')
    banner()
    client.sign_in(phone, input(gr+'[+] Enter the verification code: '+cy))

os.system('clear')
banner()
input_file = sys.argv[1]
users = []
with open(input_file, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {
            'username': row[0],
            'id': int(row[1]),
            'access_hash': int(row[2]),
            'name': row[3],
        }

        users.append(user)

chats = []
last_date = None
chunk_size = 200
groups=[]
SLEEPING = SLEEPING
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue

print(gr+'[+] Choose a group to add members: '+re)
for i, group in enumerate(groups):
    print(str(i) + '- ' + group.title)
g_index = input(gr+"Enter a Number: "+re)
target_group=groups[int(g_index)]
target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)

print(cy+"[1] Add member by user ID\n[2] Add member by username ")
mode = int(input(gr+"Input: "+re))
n = 0

for user in users:
  #  n += 1
 #   if n % 50 == 0:
      try:
           print(cy+"Try to adding {}".format(user['id']))
           if mode == 1:
              if user['username'] == "":
                   continue
              user_to_add = client.get_input_entity(user['username'])
           elif mode == 2:
              user_to_add = InputPeerUser(user['id'], user['access_hash'])
           else:
              sys.exit(re+"[!] Invalid Mode Selected. Please Try Again.")
           client(InviteToChannelRequest(target_group_entity,[user_to_add]))
           print(gr+"[✓] successfully added")
           print(cy+f"[•] Sleep time: {SLEEPING} sec")
           time.sleep(int(SLEEPING))
           continue
      except PeerFloodError as e:
           print(re+f"[!] {e}")
           continue
      except FloodWaitError as e:
           print(re+f"[!] {e}")
           return time.sleep(int(f'{e[10:15]}'))
           continue
      except UserPrivacyRestrictedError as e:
           print(re+f"[!] {e}")
           continue
      except UserChannelsTooMuchError as e:
           print(re+f"[!] {e}")
           continue
      except UserIdInvalidError as e:
           print(re+f"[!] {e}")
           continue
      except:
           traceback.print_exc()
           print(re+"[!] Unexpected Error ...")