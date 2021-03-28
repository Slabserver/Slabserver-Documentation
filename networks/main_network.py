# diagram.py
from urllib.request import urlretrieve

from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.container import Docker
from diagrams.onprem.database import MariaDB
from diagrams.saas.chat import Discord
from diagrams.generic.blank import Blank
from diagrams.custom import Custom

#Pterodactyl
pterodactyl_url = "https://avatars.githubusercontent.com/u/16179146"
pterodactyl_icon = "pterodactyl.png"
urlretrieve(pterodactyl_url, pterodactyl_icon)

#phpMyAdmin
phpmyadmin_url = "https://upload.wikimedia.org/wikipedia/commons/4/4f/PhpMyAdmin_logo.svg"
phpmyadmin_icon = "phpmyadmin.png"
urlretrieve(phpmyadmin_url, phpmyadmin_icon)

#Dynmap
dynmap_url = "https://camarosa.xyz/img/dynmap.png"
dynmap_icon = "dynmap.png"
urlretrieve(dynmap_url, dynmap_icon)

with Diagram(filename="mainnetwork", show=True, direction="TB"):

    with Cluster("Dedicated Ubuntu Server"):


        applicationbot = Docker("Application Bot")

        dynmap = Custom("Dynmap", dynmap_icon)

        with Cluster(""):
            with Cluster("Bungee Network 1"):
                proxy1 = Docker("Proxy 1")
                resource = Docker("Resource")
                survival = Docker("Survival")   

                proxy1 >> Edge(color="darkgreen") << survival
                proxy1 >> Edge(color="darkgreen") << resource


            with Cluster("          MariaDB"):
                db = MariaDB("Shared Databases")
                phpmyadmin = Custom("phpMyAdmin", phpmyadmin_icon)
            

    applications = Discord("#applications")
    ingamechat = Discord("#ingamechat")


    applications >> applicationbot
    applicationbot >> proxy1
    survival >> db
    resource >> db
    db << phpmyadmin
    survival >> ingamechat
    survival >> dynmap
