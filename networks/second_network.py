# diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.container import Docker
from diagrams.saas.chat import Discord
from diagrams.custom import Custom

from urllib.request import urlretrieve

#Pterodactyl
pterodactyl_url = "https://avatars.githubusercontent.com/u/16179146"
pterodactyl_icon = "pterodactyl.png"
urlretrieve(pterodactyl_url, pterodactyl_icon)

with Diagram(filename="second_network", show=True):

    with Cluster("Dedicated Ubuntu Server"):

        applicationbot = Docker("Application Bot")

        with Cluster("Bungee Network 2"):
            proxy2 = Docker("Proxy 2")
            modded = Docker("Modded")
            creative = Docker("Creative")
            minigames = Docker("Minigames")
            
            proxy2 >> Edge(color="darkgreen") >> modded
            proxy2 >> Edge(color="darkgreen") >> creative
            proxy2 >> Edge(color="darkgreen") >> minigames

    applications = Discord("#applications")
    ingamechat = Discord("#modded_ingamechat")

    applications >> applicationbot
    applicationbot >> proxy2
    modded >> ingamechat