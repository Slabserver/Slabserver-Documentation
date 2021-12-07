# diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.container import Docker
from diagrams.custom import Custom

from urllib.request import urlretrieve

#Pterodactyl
pterodactyl_url = "https://avatars.githubusercontent.com/u/16179146"
pterodactyl_icon = "pterodactyl.png"
urlretrieve(pterodactyl_url, pterodactyl_icon)

with Diagram(filename="bots", show=True, direction="TB"):
    with Cluster("Dedicated Ubuntu Server"):

        pterodactyl = Custom("Pterodactyl", pterodactyl_icon)

        with Cluster("Bots"):
            emojirolesbot = Docker("Emoji Roles Bot")
            modbot = Docker("Modbot")
            applicationbot = Docker("Application Bot")
            playerlistbot = Docker("Playerlist Bot")    
            snackerinactivitybot = Docker("Snacker/Inactvity Bot")
            musicbot = Docker("Music Bot")
            chester = Docker("Chester")
            ergobot = Docker("ErGoBot")

        bots = [ergobot, musicbot, playerlistbot, emojirolesbot, snackerinactivitybot, chester, modbot, applicationbot]
        pterodactyl >> Edge(color="#004da4") >> bots