from PySide2 import QtWidgets, QtGui, QtCore
import os
import pymel.core as pm
from . import constants


# ----------------------------------------------------------------------------------------------------------------------
def get_resources(file, icon, file_only):
    """
    A nice handy function that will get the resources folder from our file structure and allow us to
    access icons and other non-python files such as .JSON files.
    :param file: the name of the file that we are searching for.
    :param icon: the name of the icon that we are searching for.
    :param file_only: if we are only wanting to return the file.
    :return: filename
    """
    if file == '':
        return None

    resource_path = os.path.join(os.path.dirname(__file__), 'resources')

    if resource_path is None:
        print(f'{resource_path} could not be found.')

    if icon:
        icon_path = os.path.join(resource_path, 'icons')
        if file_only:
            return os.path.join(icon_path, file).replace('\'', '/')

    if file_only:
        return os.path.join(resource_path, file).replace('\'', '/')

    else:
        return resource_path


# ----------------------------------------------------------------------------------------------------------------------
def get_widget_options(value, name):
    """"""
    layout = QtWidgets.QHBoxLayout()
    label = QtWidgets.QLabel(name)
    layout.addWidget(label)
    w = None

    if type(value) == int:
        w = QtWidgets.QSpinBox()
        w.setValue(value)
        layout.addWidget(w)

    elif type(value) == float:
        w = QtWidgets.QDoubleSpinBox()
        w.setValue(value)
        layout.addWidget(w)

    elif type(value) == str:
        w = QtWidgets.QLineEdit()
        w.setText(value)
        layout.addWidget(w)

    elif type(value) == bool:
        w = QtWidgets.QCheckBox()
        w.setChecked(value)
        layout.addWidget(w)

    elif type(value) == list:
        w = QtWidgets.QComboBox()
        w.addItems(value)
        layout.addWidget(w)

    w.setObjectName(name)
    return layout, w


# ----------------------------------------------------------------------------------------------------------------------
def clear_widgets(container):
    """
    Clears the container of all child widgets
    :param container:
    :return:
    """
    for i in reversed(range(container.count())):
        child = container.takeAt(i)
        if not child:
            continue

        if isinstance(child, QtWidgets.QWidgetItem):
            widget = child.widget()
            widget.setParent(None)
            widget.deleteLater()

        elif isinstance(child, QtWidgets.QSpacerItem):
            pass

        else:
            clear_widgets(child)


# ----------------------------------------------------------------------------------------------------------------------
def get_values(widget):
    """
    Gets the correct widget to return based on the
    :param widget:
    :return: widget
    """
    # -- Check whether the widget is a SpinBox and return as
    # -- a float/double
    if isinstance(widget, QtWidgets.QDoubleSpinBox):
        return widget.value()

    # -- Check whether the widget is a SpinBox and return as
    # -- an integer
    if isinstance(widget, QtWidgets.QSpinBox):
        return widget.value()

    # -- Check whether the widget is a LineEdit and return as
    # -- a string
    if isinstance(widget, QtWidgets.QLineEdit):
        return widget.text()

    # -- Check whether the widget is a CheckBox and return as
    # -- a bool
    if isinstance(widget, QtWidgets.QCheckBox):
        return widget.isChecked()

    # -- Check whether we're returning a ComboBox and return as
    # -- a list
    if isinstance(widget, QtWidgets.QComboBox):
        return widget.currentText()


# ----------------------------------------------------------------------------------------------------------------------
def return_maya_main_window():
    """
    This handy function will try to return the maya window so that we can use it as our
    main window and allow us to dock the newly created window in Maya.
    :return: Maya Window
    """
    from maya import OpenMayaUI as omui
    from shiboken2 import wrapInstance

    try:
        return wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)

    except:
        pass


# ----------------------------------------------------------------------------------------------------------------------
def check_name_exists(name):
    """
    Thus function will allow us to check whether the exact name already exists within the maya scene
    and then return a + 1 value so that we can concistently name things without duplicates.
    :param name:
    :return:
    """
    same_name = list()

    scene_objects = pm.ls()


# ----------------------------------------------------------------------------------------------------------------------
def get_stripped_name(node):
    """"""
    pass


# ----------------------------------------------------------------------------------------------------------------------
def create_grouping(short_name, side):
    """
    Creates a group structure using set prefixes.
    :param short_name:
    :param side: The side that we will create the grouping for
    :return: origin group [0], offset group [1]
    """
    value = 1

    offset_grp = pm.group(empty=True, name=f'{constants.off}{short_name}_{value}_{side}')
    deform_grp = pm.group(name=f'{constants.dfm}{short_name}_{value}_{side}')
    zero_grp = pm.group(name=f'{constants.zro}{short_name}_{value}_{side}')
    origin_grp = pm.group(name=f'{constants.org}{short_name}_{value}_{side}')

    return origin_grp, offset_grp


# ----------------------------------------------------------------------------------------------------------------------
def create_control(short_name, side):
    """
    Creates a controller nurbs curve.
    :param short_name: stripped name of the new controller
    :param side: the side suffix of the new controller
    :return:
    """

    value = 1

    return pm.circle(name=f'{constants.ctl}{short_name}_{value}_{side}')


# ----------------------------------------------------------------------------------------------------------------------
def create_controller(short_name, side):
    """
    A grouped method for creating a controller and grouping
    :param short_name: stripped name of the new controller
    :param side: the side suffix of the new controller
    :return:
    """
    control = create_control(short_name, side)[0]
    groups = create_grouping(short_name, side)

    set_controller_colour(control)
    set_outline_colour(control)

    pm.parent(control, groups[1])

    return control, groups[0]


# ----------------------------------------------------------------------------------------------------------------------
def set_controller_colour(obj_to_colour):
    """
    Sets the color of the side depending on its suffix.
    :param obj_to_colour:
    :return: True
    """
    obj = pm.PyNode(obj_to_colour)
    # -- Colour our controllers depending on whether they are
    # -- on the left, right or in the center.
    obj.setAttr('overrideEnabled', True)
    obj.setAttr('overrideRGBColors', 1)

    # -- Chose what colour the controller should be, based
    # -- off of the side suffix
    if '_MD' in str(obj):
        obj.setAttr('overrideColorRGB', (1, 1, 0))

    if '_LF' in str(obj):
        obj.setAttr('overrideColorRGB', (0, 0, 1))

    if '_RT' in str(obj):
        obj.setAttr('overrideColorRGB', (1, 0, 0))

    return True


# ----------------------------------------------------------------------------------------------------------------------
def set_outline_colour(obj_to_colour):
    """
    Sets a colour for new objects in the outliner/hierarchy
    :param obj_to_colour: object that we want to colour
    :param colour: list() of 3 integers defining the desired outline colour
    :return: True
    """
    obj = pm.PyNode(obj_to_colour)
    obj.setAttr('useOutlinerColor', 1)
    obj.setAttr('outlinerColor', (0, 1, 1))

    return True
