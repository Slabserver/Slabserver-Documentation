# diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.container import Docker
from diagrams.custom import Custom

from urllib.request import urlretrieve

#Backblaze
backblaze_url = "https://img.stackshare.io/service/5918/5bNX_lVF_400x400.png"
backblaze_icon = "backblaze.png"
urlretrieve(backblaze_url, backblaze_icon)

#Restic
restic_url = "https://restic.readthedocs.io/en/latest/_static/logo.png"
restic_icon = "restic.png"
urlretrieve(restic_url, restic_icon)

with Diagram(filename="restic_backblaze", show=True, direction="TB"):

    backblaze = Custom("Backblaze B2 Storage", backblaze_icon)

    with Cluster("Dedicated Ubuntu Server"):

        with Cluster("Game Servers"):
            proxy1 = Docker("Proxy 1")
            proxy2 = Docker("Proxy 2")
            survival = Docker("Survival")
            resource = Docker("Resource")
            creative = Docker("Creative")
            modded = Docker("Modded")
            minigames = Docker("Minigames")
            gmod = Docker("Gmod")
            snapshot = Docker("Snapshot")
            terraria = Docker("Terraria")
            misc = Docker("Misc. Servers")

        restic = Custom("Restic", restic_icon)

        servers = [misc, gmod, terraria, snapshot, minigames, modded, creative, resource, survival, proxy2, proxy1]

        servers << Edge(color="#a81c2b") >> restic
        restic << Edge(color="#a81c2b") >> backblaze
           