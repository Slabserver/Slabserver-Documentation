# diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.container import Docker
from diagrams.custom import Custom

from urllib.request import urlretrieve

#Pterodactyl
pterodactyl_url = "https://avatars.githubusercontent.com/u/16179146"
pterodactyl_icon = "pterodactyl.png"
urlretrieve(pterodactyl_url, pterodactyl_icon)

with Diagram(filename="game_servers_ungrouped", show=True, direction="TB"):
    with Cluster("Dedicated Ubuntu Server"):

        pterodactyl = Custom("Pterodactyl", pterodactyl_icon)

        with Cluster("Game Servers"):
            proxy1 = Docker("Proxy Network 1")
            proxy2 = Docker("Proxy Network 2")
            survival = Docker("Survival")
            resource = Docker("Resource")
            creative = Docker("Creative")
            modded = Docker("Modded")
            minigames = Docker("Minigames")
            gmod = Docker("Gmod")
            snapshot = Docker("Snapshot")
            terraria = Docker("Terraria")
            misc = Docker("Misc. Servers")

            servers = [misc, gmod, terraria, snapshot, minigames, modded, creative, resource, survival, proxy2, proxy1]

            pterodactyl >> Edge(color="#004da4") >> servers
           