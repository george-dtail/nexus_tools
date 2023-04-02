import json
import os

import pymel.core as pm

import nexus_tools
from nexus_tools import constants, functions


_STORED_SHAPE = list()

# ----------------------------------------------------------------------------------------------------------------------
class ApplyShapeFromList(nexus_tools.NexusTool):

    Name = 'Shapes : Apply Shape From List'

    Icon = 'load.png'

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super(ApplyShapeFromList, self).__init__()

        self.options['Overwrite Shape'] = False
        self.options['Shape'] = []

        self._shape_list = ''
        self._get_shape_list()

    # ------------------------------------------------------------------------------------------------------------------
    def run(self):
        # -- Get our shape file
        # -- We have our dict, now we need to send this to our json file
        shape = self._shape_list[self.options['Shape']]

        selection = pm.selected()[-1]
        selection_shapes = selection.getShapes()

        if self.options['Overwrite Shape']:
            pm.delete(selection_shapes)

        for key in self._shape_list.keys():
            if key == self.options['Shape']:
                for shape in self._shape_list.get(key, {}):
                    shape_curve = pm.curve(
                        name=shape['name'],
                        point=json.loads(shape['cvs']),
                        degree=int(shape['degree'])
                    )

                    pm.parent(
                        shape_curve.getShape(),
                        selection,
                        shape=True,
                        addObject=True
                    )

                    pm.delete(shape_curve)

        self._get_shape_list()

        return True

        # ------------------------------------------------------------------------------------------------------------------

    def _get_shape_list(self):
        filepath = functions.get_resources(file='shapes.json', file_only=True, icon=False)

        if not os.path.isfile(filepath):
            print('No path can be given for {}'.format(filepath))
            return False

        with open(filepath, 'r') as shape_file:
            self._shape_list = json.load(shape_file)

        self.options['Shape'] = list(self._shape_list.keys())


# ----------------------------------------------------------------------------------------------------------------------
class SaveShapeToList(nexus_tools.NexusTool):

    Name = 'Shapes : Save Shape To List'

    Icon = 'save.png'

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super(SaveShapeToList, self).__init__()

        self.options['Shape Name'] = ''

    # ------------------------------------------------------------------------------------------------------------------
    def run(self):
        selection = pm.selected()[0]

        shapes = selection.getShapes()

        shape_info_list = []

        for s in shapes:

            cvs = []

            for i in range(len(s.getCVs())):
                cvs.append(list(s.getCV(i)))

            curve_dict = dict(
                name=str(s),
                cvs=str(cvs),
                degree=str(s.degree()),
            )

            # -- Now that we have our data, we will add it into a list that will be applied
            # -- To the controller's curve_info attribute
            shape_info_list.append(curve_dict)

        if self.options['Shape Name'] == '':
            self.options['Shape Name'] = str(selection)

        # -- We have our dict, now we need to send this to our json file
        filepath = functions.get_resources(file='shapes.json', file_only=True, icon=False)

        if os.path.isfile(filepath):
            with open(filepath) as shape_file:
                stored_shapes = json.load(shape_file)

                stored_shapes[self.options['Shape Name']] = shape_info_list

            with open(functions.get_resources(file='shapes.json', file_only=True, icon=False), 'w') as json_file:
                shape_list = json.dump(stored_shapes, json_file, indent=4)

            print('{} has been stored.'.format(self.options['Shape Name']))

            return True

        if not os.path.isfile(filepath):
            with open(filepath, 'w') as shape_file:
                new_shape = {
                    self.options['Shape Name']: shape_info_list
                }

                json.dump(new_shape, shape_file, indent=4)

            print('{} has been stored.'.format(self.options['Shape Name']))

            return True


# ----------------------------------------------------------------------------------------------------------------------
class CopyShape(nexus_tools.NexusTool):

    Name = 'Shapes : Copy Shape'

    Icon = 'auto_repair.png'

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super(CopyShape, self).__init__()

    # ------------------------------------------------------------------------------------------------------------------
    def run(self):
        # -- Clear our clipboard
        _STORED_SHAPE.clear()

        selection = pm.selected()[0]

        shapes = selection.getShapes()

        for s in shapes:

            cvs = []

            for i in range(len(s.getCVs())):
                cvs.append(list(s.getCV(i)))

            curve_dict = dict(
                name=str(s),
                cvs=str(cvs),
                degree=str(s.degree()),
            )

            # -- Now that we have our data, we will add it into a list that will be applied
            # -- To the controller's curve_info attribute
            _STORED_SHAPE.append(curve_dict)


# ----------------------------------------------------------------------------------------------------------------------
class PasteShape(nexus_tools.NexusTool):

    Name = 'Shapes : Paste Shape'

    Icon = 'auto_repair.png'

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super(PasteShape, self).__init__()

    # ------------------------------------------------------------------------------------------------------------------
    def run(self):
        # -- Get our selected
        selection = pm.selected()[-1]

        # -- Get the shapes of that selected object and delete it
        selection_shapes = selection.getShapes()
        pm.delete(selection_shapes)

        # -- Read our stored shape and apply it to our selected transform node
        data = str(_STORED_SHAPE).replace("'", "\"")

        shapes = json.loads(data)

        for shape in shapes:
            shape_curve = pm.curve(
                name=shape['name'],
                point=json.loads(shape['cvs']),
                degree=int(shape['degree'])
            )

            pm.parent(
                shape_curve.getShape(),
                selection,
                shape=True,
                addObject=True
            )

            pm.delete(shape_curve)

        return True


# ----------------------------------------------------------------------------------------------------------------------
class MirrorShape(nexus_tools.NexusTool):

    Name = 'Shapes : Mirror Shape'

    Icon = 'auto_repair.png'

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super(MirrorShape, self).__init__()

    # ------------------------------------------------------------------------------------------------------------------
    def run(self):
        pass


# ----------------------------------------------------------------------------------------------------------------------
class ColourShape(nexus_tools.NexusTool):

    Name = 'Shapes : Colour Shape'

    Icon = 'paint-bucket.png'

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super(ColourShape, self).__init__()

    # ------------------------------------------------------------------------------------------------------------------
    def run(self):
        selection = pm.selected()[0]

        functions.set_controller_colour(selection)

        functions.set_outline_colour(selection)

        return True
