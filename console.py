#!/usr/bin/env python3

import json
import os

from fonctions import help_rss, cls, new_feed, remove_feed, alter_feed

cls()
help_rss()
var = ""
while var != "exit" :
    var = input("\nconsole rss-discord # ")
    if var == "add" :
        key = input("Nom du flux : ")
        username = input("Nom du webhook : ")
        rss_url = input("URL du flux rss : ")
        url_webhook = input("URL du webhook : ")
        url_avatar = input("URL avatar : ")
        new_feed(key,username,rss_url,url_webhook,url_avatar)
    elif var == "remove" :
        key = input("Nom du flux a supprimer : ")
        check = input(f"Etes vous sur de vouloir supprimer {key} ? (y/n) ")
        remove_feed(key,check)
    elif var == "alter" :
        key = input("Nom de la cle a modifier : ")
        value = input("Nom de la valeur a modifier (URL / WEBHOOK / USERNAME / AVATAR) : ")
        change = input(f"Entrez le nouveaux {value} : ")
        alter_feed(key,value,change)
    elif var == "catdb":
        os.system("cat /root/rss-discord/db.json\n")
    elif var == "help":
        help()
