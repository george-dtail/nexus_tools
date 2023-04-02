import pymel.core as pm

import nexus_tools
from nexus_tools import constants, functions


# ----------------------------------------------------------------------------------------------------------------------
class ScaleJoints(nexus_tools.NexusTool):

    Name = 'Joints : Scale Radius'

    Icon = 'joint.png'

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super(ScaleJoints, self).__init__()

    # ------------------------------------------------------------------------------------------------------------------
    def run(self):
        joints = pm.ls(type='joint')

        for j in joints:
            j.attr('radius').set(j.attr('radius').get() + 1)

        return True


# ----------------------------------------------------------------------------------------------------------------------
class ReduceJoints(nexus_tools.NexusTool):

    Name = 'Joints : Reduce Radius'

    Icon = 'joint.png'

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super(ReduceJoints, self).__init__()

    # ------------------------------------------------------------------------------------------------------------------
    def run(self):
        joints = pm.ls(type='joint')

        for j in joints:
            j.attr('radius').set(j.attr('radius').get() - 1)

        return True


# ----------------------------------------------------------------------------------------------------------------------
class MoveOrientsToRotations(nexus_tools.NexusTool):

    Name = 'Joints : Orients To Rotations'

    Icon = 'rotation.png'

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super(MoveOrientsToRotations, self).__init__()

    def run(self):
        pass


# ----------------------------------------------------------------------------------------------------------------------
class MoveRotationsToOrients(nexus_tools.NexusTool):
    Name = 'Joints : Orients To Rotations'

    Icon = 'rotation.png'

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super(MoveRotationsToOrients, self).__init__()

    def run(self):
        pass
