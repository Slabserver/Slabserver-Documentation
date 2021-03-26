# diagram.py
from urllib.request import urlretrieve

from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.container import Docker
from diagrams.onprem.database import MariaDB
from diagrams.saas.chat import Discord
from diagrams.custom import Custom

#Pterodactyl
pterodactyl_url = "https://avatars.githubusercontent.com/u/16179146"
pterodactyl_icon = "pterodactyl.png"
urlretrieve(pterodactyl_url, pterodactyl_icon)

#phpMyAdmin
phpmyadmin_url = "https://upload.wikimedia.org/wikipedia/commons/4/4f/PhpMyAdmin_logo.svg"
phpmyadmin_icon = "pterodactyl.png"
urlretrieve(phpmyadmin_url, phpmyadmin_icon)

#Dynmap
dynmap_url = "https://camarosa.xyz/img/dynmap.png"
dynmap_icon = "dynmap.png"
urlretrieve(dynmap_url, dynmap_icon)

with Diagram(filename="main_network", show=True):

    with Cluster("Dedicated Ubuntu Server"):

        dynmap = Custom("Dynmap", dynmap_icon)
        applicationbot = Docker("Application Bot")

        with Cluster("Bungee Network 1"):
            proxy1 = Docker("Proxy 1")
            survival = Docker("Survival")
            resource = Docker("Resource")
            proxy1 >> Edge(color="darkgreen") << survival
            proxy1 >> Edge(color="darkgreen") << resource
    
        with Cluster("MySQL / MariaDB"):
            maindb = MariaDB("Survival Databases")
            resourcedb = MariaDB("Resource Databases")
            phpmyadmin = Custom("phpMyAdmin", phpmyadmin_icon)

    applications = Discord("#applications")
    ingamechat = Discord("#ingamechat")


    applications >> applicationbot
    applicationbot >> proxy1
    survival >> maindb
    survival >> dynmap
    resource >> resourcedb
    survival >> ingamechat
    maindb >> phpmyadmin
    resourcedb >> phpmyadmin