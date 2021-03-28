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

with Diagram(filename="main_network", show=True, direction="LR") as diag:

    applications = Discord("#applications")
    blankingamechat = Blank("BlankIngameChat")
    ingamechat = Discord("#ingamechat")

    with Cluster("Dedicated Ubuntu Server"):




        applicationbot = Docker("Application Bot")

        dynmap = Custom("Dynmap", dynmap_icon)
        blankdynmap = Blank("Blank Dynmap") 

        with Cluster("Bungee Network 1"):
            proxy1 = Docker("Proxy 1")
            blank1 = Blank("blank1")
            resource = Docker("Resource")
            survival = Docker("Survival")
            blank = Blank("blank")

            proxy1 - blank1
            proxy1 >> Edge(color="darkgreen") << survival
            proxy1 >> Edge(color="darkgreen") << resource
            proxy1 - blank



        with Cluster("          MariaDB"):
            # blank2 = Blank("blank2")    
            maindb = MariaDB("Main Network Databases")
            # blank3 = Blank("blank3")
            # blank4 = Blank("blank4")
            # proxydb = MariaDB("Proxy Databases")
            phpmyadmin = Custom("phpMyAdmin", phpmyadmin_icon)


    # blank3 = Blank("blank3")

    applications >> applicationbot
    applicationbot >> proxy1

    survival >> maindb
    resource >> maindb
    # proxy1 >> proxydb
    # blank2 - phpmyadmin
    # proxydb << phpmyadmin
    maindb << phpmyadmin
    # blank3 - phpmyadmin
    survival >> ingamechat
    resource >> blankdynmap
    survival >> dynmap
    # resource >> blankingamechat
    # resource - Edge(penwidth="0.0") - blank
    # resource - Edge(penwidth="0.0") - blank2