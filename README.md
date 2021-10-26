<h1><span style="font-size: medium;"><strong>Vous voulez un channel de news sur votre serveur Discord ?</strong></span></h1>
<p><span style="font-size: 14.4px;">Gratuit et illimit&eacute; !</span></p>
<p>https://discord.gg/gXeWmtUB6E</p>
<p><span style="font-size: 14.4px;">Choisissez votre channel annonce parmi ceux disponibles, ou demandez en un nouveau et faite suivre le channel pour retrouver toutes les publications sur votre serveur Discord dans le chann que vous aurez cr&eacute;&eacute;e !</span></p>
<p><span style="font-size: 14.4px;">Il est possible de recuperer les news de tout site / jeu / twitter / youtube / journal / etc ...</span></p>
<p>_________________________________________</p>
<h2>Vous pouvez aussi heberger vous meme votre code</h2>
<p>Il suffit de mettre tout les fichiers du git dans un repertoire <span style="font-weight: bold;">rss-discord</span>&nbsp; a la racine de votre /root/</p>
<p>Et de crée un repertoire /GUID/ dans le repertoire /rss-discord/</p>
<p>Ensuite pour ajouter un nouveaux flux lancez le code <strong>new-feed.py</strong></p>
<p>Il vous demandera alors les infos necessaire : nom du flux / nom du webhook / url du flux rss / url webhook / url avatar webhook</p>
<p>Il enregistrera les infos dans la base <strong>db.json</strong>&nbsp;ensuite il suffit de lancer le code <strong>rss-discord.py</strong> et il check la <strong>db.json</strong> et actualise les flux</p>
<br>
<p>
    <code>git clone https://github.com/Karomy404/webhook-discord-rss.git</code><br>
    <code>mv webhook-discord-rss/ /root/rss-discord</code><br>
    <code>mkdir /root/rss-discord/GUID</code><br>
    <code>chmod +x /root/rss-discord/*.py</code>
    <code>python3 /root/rss-discord/new-feed.py</code> pour ajouter un nouveaux flux<br>
    <code>python3 /root/rss-discord/rss-discord.py</code> pour executer le code<br>
  
</p>
<br>
<p>Ajouter simplement l'execution du code python&nbsp;<strong style="font-size: 0.9em;">rss-discord.py</strong><span style="font-size: 0.9em;">&nbsp;dans une tache automatique pour qu'il s'execute tout les x temps</span></p>
