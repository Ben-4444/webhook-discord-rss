#!/usr/bin/env python3

import json


print("Nom du flux :")
key = input()

print("Nom du webhook :")
username = input()

print("URL du flux rss :")
rss_url = input()

print("URL du webhook :")
url_webhook = input()

print("URL avatar :")
url_avatar = input()

guid ="/root/rss-discord/GUID/" + key + ".guid"

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
    f.close()
