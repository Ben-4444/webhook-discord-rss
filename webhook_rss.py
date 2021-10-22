#!/usr/bin/env python3

# Module requis
import feedparser
import requests
import time

# URL du flux RSS : <----------------------- A remplir !
url = 'http://exemple.com/rss'
feed = feedparser.parse(url)

# URL du WEBHOOK DISCORD <----------------------- A remplir !
webhook = 'https://url.webhook.discord'

# Récupération du flux
for entry in feed.entries:
    # Recherche si le GUID du post rss existe dans le fichier
    fichier = open('guid', 'r').read().find(entry.guid)
    # Si le GUID existe il renvois 0 sinon -1 | On print les infos et on ecrit le guid du post dans le fichier GUID
    if fichier == -1 :
        print(entry.title)
        print(entry.link)
        print(entry.updated)
        print(entry.guid)
        fichier = open("guid", "a")
        fichier.write("\n" + entry.guid)

        # Partie config webhook discord
        data = {}
        data["content"] = entry.title + "\n" + entry.link + "\n" + entry.updated
        # Nom du webhook ! <----------------------- A remplir !
        data["username"] = ""
        # Avatar du webhook ! <----------------------- A remplir !
        data["avatar_url"] = ""
        result = requests.post(webhook, json = data)
        time.sleep(1)
    else :
        print("exist")

####################################################################################
######################################  RTFM  ######################################
####################################################################################
# Doc webhook discord https://discordapp.com/developers/docs/resources/webhook#execute-webhook
# Doc python ecrire/lire fichier https://python.doctor/page-lire-ecrire-creer-fichier-python
# Doc python chercher dans un fichier https://www.delftstack.com/fr/howto/python/python-find-string-in-file/#utilisez-la-m%25C3%25A9thode-find-pour-rechercher-une-cha%25C3%25AEne-dans-un-fichier-en-python
# Doc python feedparse (recuperer rss) https://tekipaki.hypotheses.org/628#footnote_3_628
# Doc python webhook discord https://gist.github.com/Bilka2/5dd2ca2b6e9f3573e0c2defe5d3031b2
# GitHub dun code similaire qui marche a moitier pour mes besoins https://github.com/Eskimon/zds-discord-bot-rss/blob/master/discord-rss-webhook.py
# Bible des flux http://atlasflux.saynete.net/index.htm
# Twitter RSS https://nitter.net/
# Youtube RSS https://piped.kavin.rocks/
