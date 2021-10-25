#!/usr/bin/env python3

import json


key = input("Nom du flux : ")

username = input("Nom du webhook :")

rss_url = input("URL du flux rss :")

url_webhook = input("URL du webhook :")

url_avatar = input("URL avatar :")

guid =f"/root/rss-discord/GUID/{key}.guid"

with open("/root/rss-discord/db.json", "r") as json_file:
    DICO = json.load(json_file)

if key in DICO['URL'] :
    print("ERREUR : Le nom du flux (key) existe deja dans le fichier db.json")
else :
    DICO["URL"][key] = rss_url
    DICO["WEBHOOK"][key] = url_webhook
    DICO["USERNAME"][key] = username
    DICO["AVATAR"][key] = url_avatar
    DICO["GUID"][key] = guid

    print(json.dumps(DICO, sort_keys=True, indent=4))
    print("SUCCESS : Le flux a bien été enregistré dans le fichier db.json")

    with open('/root/rss-discord/db.json', 'w') as f:
        f.write(json.dumps(DICO, sort_keys=True, indent=4))
