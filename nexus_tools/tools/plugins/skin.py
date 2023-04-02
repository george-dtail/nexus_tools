import pymel.core as pm

import nexus_tools
from nexus_tools import constants, functions


# ----------------------------------------------------------------------------------------------------------------------
class DetachSkin(nexus_tools.NexusTool):

    Name = 'Skin : Detach Skin'

    Icon = 'skin.png'

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super(DetachSkin, self).__init__()

    # ------------------------------------------------------------------------------------------------------------------
    def run(self):
        skin_clusters = pm.ls(type='skinCluster')

        for skin_cluster in skin_clusters:
            skin_cluster.moveJointsMode(True)

        return True


# ----------------------------------------------------------------------------------------------------------------------
class ReattachSkin(nexus_tools.NexusTool):

    Name = 'Skin : ReAttach Skin'

    Icon = 'skin.png'

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super(ReattachSkin, self).__init__()

    # ------------------------------------------------------------------------------------------------------------------
    def run(self):
        skin_clusters = pm.ls(type='skinCluster')

        for skin_cluster in skin_clusters:
            skin_cluster.moveJointsMode(False)

        return True
