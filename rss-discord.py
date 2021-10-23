#!/usr/bin/env python3

# Module requis
import feedparser
import requests
import time
import json
from pathlib import Path

with open("/root/rss-discord/db.json", "r") as json_file:
        DICO = json.load(json_file)

def code(URL, WEBHOOK, USERNAME, AVATAR_URL, GUID):
    print(DICO['USERNAME'][k])
    feed = feedparser.parse(URL)

    # Récupération du flux
    for entry in feed.entries:
        # Recherche si le GUID du post rss existe dans le fichier
        fichier = open(GUID, 'r').read().find(entry.guid)
        # Si le GUID existe il renvois 0 sinon -1 | On print les infos et on ecrit le guid du post dans le fichier GUID
        if fichier == -1 :
            print(entry.title)
            print(entry.link)
            print(entry.updated)
            print(entry.guid)
            fichier = open(GUID, "a")
            fichier.write("\n" + entry.guid)
            fichier.close()
            # Partie config webhook discord
            data = {}
            data["content"] = entry.title + "\n" + entry.link + "\n" + entry.updated
            data["username"] = USERNAME
            data["avatar_url"] = AVATAR_URL
            result = requests.post(WEBHOOK, json = data)
            time.sleep(1)
        else :
            print("exist")

    print('\n')

for (k, v) in DICO['URL'].items():

    guid_file = Path(DICO['GUID'][k])
    guid_file.touch(exist_ok=True)
    code(DICO['URL'][k], DICO['WEBHOOK'][k], DICO['USERNAME'][k], DICO['AVATAR'][k], DICO['GUID'][k])

json_file.close()
