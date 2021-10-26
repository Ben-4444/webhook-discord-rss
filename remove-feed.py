#!/usr/bin/env python3

import json


key = input("Nom du flux a supprimé : ")

with open("/root/rss-discord/db.json", "r") as json_file:
    DICO = json.load(json_file)

if key in DICO['URL'] :
    del DICO["GUID"][key]
    del DICO["URL"][key]
    del DICO["WEBHOOK"][key]
    del DICO["AVATAR"][key]
    del DICO["USERNAME"][key]
    print(json.dumps(DICO, sort_keys=True, indent=4))
    with open('/root/rss-discord/db.json', 'w') as f:
        f.write(json.dumps(DICO, sort_keys=True, indent=4))
    print("SUCCESS : Le flux a bien été enregistré dans le fichier db.json")

else :

    print(json.dumps(DICO, sort_keys=True, indent=4))
    print(f"ERREUR : Le nom du flux {key} existe deja dans le fichier db.json")

