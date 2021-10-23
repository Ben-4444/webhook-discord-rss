#!/usr/bin/env python3

import json


print("nom du flux :")
key = input()

print("nom du webhook :")
username = input()

print("url du flux rss :")
rss_url = input()

print("url du webhook :")
url_webhook = input()

print("url avatar :")
url_avatar = input()

guid ="/root/rss-discord/GUID/" + key + ".guid"

with open("/root/rss-discord/db.json", "r") as json_file:
    DICO = json.load(json_file)


DICO["URL"][key] = rss_url
DICO["WEBHOOK"][key] = url_webhook
DICO["USERNAME"][key] = username
DICO["AVATAR"][key] = url_avatar
DICO["GUID"][key] = guid

print(json.dumps(DICO, sort_keys=True, indent=4))

with open('/root/rss-discord/db.json', 'w') as f:
    f.write(json.dumps(DICO, sort_keys=True, indent=4))
f.close()
