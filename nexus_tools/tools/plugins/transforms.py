import pymel.core as pm

import nexus_tools
from nexus_tools import constants, functions


# ----------------------------------------------------------------------------------------------------------------------
class MatchTransform(nexus_tools.NexusTool):

    Name = 'Transform : Match Transform'

    Icon = 'auto_repair.png'

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super(MatchTransform, self).__init__()

        self.options['Match This'] = ''
        self.options['To This'] = ''

        self.options['Match'] = ['Transform', 'Location', 'Rotation']

    # ------------------------------------------------------------------------------------------------------------------
    def run(self):
        if self.options['Match This'] == '':
            self.options['Match This'] = pm.selected()[0]

        if self.options['To This'] == '':
            self.options['To This'] = pm.selected()[-1]

        if self.options['Match'] == 'Transform':
            pm.matchTransform(self.options['Match This'], self.options['To This'])

        if self.options['Match'] == 'Location':
            pm.matchTransform(self.options['Match This'], self.options['To This'])

        if self.options['Match'] == 'Rotation':
            pm.matchTransform(self.options['Match This'], self.options['To This'])

        self.options['Match'] = ['Transform', 'Location', 'Rotation']

        return True


# ----------------------------------------------------------------------------------------------------------------------
class LocatorAtCentre(nexus_tools.NexusTool):

    Name = 'Transform : Locator At Selection Centre'

    Icon = 'auto_repair.png'

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super(LocatorAtCentre, self).__init__()

    # ------------------------------------------------------------------------------------------------------------------
    def run(self):
        temp_cluster = pm.cluster()
        locator = pm.spaceLocator('LOC_TempLocator_')

        pm.matchTransform(locator, temp_cluster)

        pm.delete(temp_cluster)

        return True
