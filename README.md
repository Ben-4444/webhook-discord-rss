<h1><span style="font-size: medium;"><strong>Vous voulez un channel de news sur votre serveur Discord ?</strong></span></h1>
<p><span style="font-size: 14.4px;">Gratuit et illimit&eacute; !</span></p>
<p>https://discord.gg/gXeWmtUB6E</p>
<p><span style="font-size: 14.4px;">Choisissez votre channel annonce parmi ceux disponibles, ou demandez en un nouveau et faite suivre le channel pour retrouver toutes les publications sur votre serveur Discord dans le chann que vous aurez cr&eacute;&eacute;e !</span></p>
<p><span style="font-size: 14.4px;">Il est possible de recuperer les news de tout site / jeu / twitter / youtube / journal / etc ...</span></p>
<p>_________________________________________</p>
<h2>Vous pouvez aussi heberger vous meme le code</h2>
<p>Il suffit de mettre tout les fichiers du git dans un repertoire <span style="font-weight: bold;">rss-discord</span>&nbsp; a la racine de votre /root/</p>
<p>Et de crée un repertoire /GUID/ dans le repertoire /rss-discord/</p>
<p>Ensuite pour gerer les flux et les webhooks, il suffit d'executer le code console.py</p>
<p>A partir de la console, vous pouvez afficher la base de vos flux, les ajouter, les supprimer, ou les modifier</p>
<p>Si vous en ajoutez un, il vous demandera alors les infos necessaire : nom du flux / nom du webhook / url du flux rss / url webhook / url avatar webhook</p>
<p>Il enregistrera les infos dans la base <strong>db.json</strong>&nbsp;ensuite il suffit de lancer le code <strong>rss-discord.py</strong> et il check la <strong>db.json</strong> et actualise les flux</p>
<p>Copié le premier bloc ci dessous afin d'initialiser et configurer les flux RSS et les Webhooks</p>
<p>
    
    git clone https://github.com/Karomy404/webhook-discord-rss.git
    mv webhook-discord-rss/ /root/rss-discord
    mkdir /root/rss-discord/GUID
    chmod +x /root/rss-discord/*.py
    python3 /root/rss-discord/console.py #<--- permet de gerer les flux / webhooks
    
</p>
<p>
    
    python3 /root/rss-discord/rss-discord.py #<--- permet d'executer le code
    
</p>
<br>
<p>Ajouter simplement l'execution du code python&nbsp;<strong style="font-size: 0.9em;">rss-discord.py</strong><span style="font-size: 0.9em;">&nbsp;dans une tache automatique pour qu'il s'execute tout les x temps</span></p>
