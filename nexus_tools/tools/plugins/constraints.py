import pymel.core as pm

import nexus_tools
from nexus_tools import constants, functions


# ----------------------------------------------------------------------------------------------------------------------
class AimAt(nexus_tools.NexusTool):

    Name = 'Constraints : Aim At'

    Icon = 'join.png'

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super(AimAt, self).__init__()

        self.options['Aim This'] = ''
        self.options['At This'] = ''
        self.options['Up Target'] = ''

    # ------------------------------------------------------------------------------------------------------------------
    def run(self):
        if self.options['Aim This'] == '':
            self.options['Aim This'] = pm.selected()[0]

        if self.options['At This'] == '':
            self.options['At This'] = pm.selected[1]

        temp_aim_constraint = pm.aimConstraint(self.options['At This'], self.options['Aim This'])

        pm.delete(temp_aim_constraint)

        return True


# ----------------------------------------------------------------------------------------------------------------------
class TransformConstraint(nexus_tools.NexusTool):

    Name = 'Constraint : Transform Constraint'

    Icon = 'transform.png'

    def __init__(self):
        super(TransformConstraint, self).__init__()

    # ------------------------------------------------------------------------------------------------------------------
    def run(self):
        selection = pm.selected()

        pm.parentConstraint(selection[0], selection[1], maintainOffset=True)
        pm.scaleConstraint(selection[0], selection[1], maintainOffset=True)

        return True
