#!/usr/bin/env python3

import json
import os

#fonction clear console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#fonction affiche les commandes
def help_rss():
    print("\nBienvenue dans la console de gestions du rss-discprd.py")
    print("Ici, vous pouvez ajouter, supprimer ou modifier une entré rss\n")
    print("Commandes : catdb / add / remove / alter / exit\n")

#fonction ajouter un flux rss
def new_feed(key,username,rss_url,url_webhook,url_avatar):

    guid =f"/root/rss-discord/GUID/{key}.guid"

    with open("/root/rss-discord/db.json", "r") as json_file:
        DICO = json.load(json_file)

    if key in DICO['URL'] :
        print(f"ERROR : Le nom du flux {key} existe deja dans le fichier db.json")
    else :
        DICO["URL"][key] = rss_url
        DICO["WEBHOOK"][key] = url_webhook
        DICO["USERNAME"][key] = username
        DICO["AVATAR"][key] = url_avatar
        DICO["GUID"][key] = guid

        print(json.dumps(DICO, sort_keys=True, indent=4))
        print(f"SUCCESS : Le flux {key} a bien été enregistré dans le fichier db.json")

        with open('/root/rss-discord/db.json', 'w') as f:
            f.write(json.dumps(DICO, sort_keys=True, indent=4))

#fonction suprimer un flux rss
def remove_feed(key,check):

    with open("/root/rss-discord/db.json", "r") as json_file:
        DICO = json.load(json_file)

    if key in DICO['URL'] :
        DICO["GUID"].pop(key)
        DICO["URL"].pop(key)
        DICO["WEBHOOK"].pop(key)
        DICO["AVATAR"].pop(key)
        DICO["USERNAME"].pop(key)
        if check == "y":
            print(json.dumps(DICO, sort_keys=True, indent=4))
            with open('/root/rss-discord/db.json', 'w') as f:
                f.write(json.dumps(DICO, sort_keys=True, indent=4))
            print("SUCCESS : Le flux a bien été supprimé dans le fichier db.json")
        else :
            print("Annulation remove !")

    else :
        print("ERROR : Le nom du flux (key) n'existe pas dans le fichier db.json")

#fonction modifier un flux rss
def alter_feed(key,value,change):
    with open("/root/rss-discord/db.json", "r") as json_file:
        DICO = json.load(json_file)

    if key in DICO['URL'] :

        if value.lower() == "url":
            value = "URL"
            DICO[value][key] = change
            modif = True
        if value.lower() == "webhook":
            value = "WEBHOOK"
            DICO[value][key] = change
            modif = True
        if value.lower() == "username":
            value = "USERNAME"
            DICO[value][key] = change
            modif = True
        if value.lower() == "avatar":
            value = "AVATAR"
            DICO[value][key] = change
            modif = True

        if modif :
            print(json.dumps(DICO, sort_keys=True, indent=4))
            print("SUCCESS : Le flux a bien été modifié dans le fichier db.json")
            with open('/root/rss-discord/db.json', 'w') as f:
                f.write(json.dumps(DICO, sort_keys=True, indent=4))
        else :
            print(f"ERROR : La valaur {value} a modifier n'existe pas")

    else :
        print(f"ERROR : Le nom du flux {key} n'existe pas dans le fichier db.json")
