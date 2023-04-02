from PySide2 import QtWidgets, QtCore
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from PySide2.QtGui import QIcon


from .tools import core
from . import functions


# ----------------------------------------------------------------------------------------------------------------------
class NexusTools(QtWidgets.QWidget):
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, parent=None):
        super(NexusTools, self).__init__(parent=parent or QtWidgets.QMainWindow())

        # -- Set the basic settings
        self.setGeometry(0, 1000, 500, 0)
        self.setMinimumWidth(500)
        self.setMinimumHeight(600)

        # -- If we have a style sheet, we can set it here
        # self.setStyleSheet("border: 2px solid grey")

        # -- Create the main layout and add our list
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        # -- Add a search bar
        self.search_bar = QtWidgets.QLineEdit()
        self.layout.addWidget(self.search_bar)

        # -- Add our list widget
        self.item_list = ListWidget()
        self.layout.addWidget(self.item_list)

        # -- Add the item options widget
        self.item_options = QtWidgets.QVBoxLayout()
        self.layout.addLayout(self.item_options)

        # -- Connect our search bar
        self.search_bar.textChanged.connect(self.item_search_edited)

        # -- Populate our object list and connect the output
        self.populate_object_list(search=False)
        self.item_list.currentItemChanged.connect(self.populate_item_options)
        self.item_list.itemDoubleClicked.connect(self.run_item)

        # -- Create a run button at the bottom to make using the tools more accessible
        self.run_button = QtWidgets.QPushButton('Run')
        self.layout.addWidget(self.run_button)
        self.run_button.clicked.connect(self.run_item)

    # ------------------------------------------------------------------------------------------------------------------
    def item_search_edited(self):
        self.populate_object_list(search=True)

    # ------------------------------------------------------------------------------------------------------------------
    def populate_object_list(self, search, *args, **kwargs):
        """"""
        # -- Clear the tools list
        self.item_list.clear()

        # -- If we are searching, we'll
        if search:
            for item in core.get_item_list():
                if self.search_bar.text() in str(item.Name):
                    list_item = QtWidgets.QListWidgetItem(item.Name)
                    list_item.setIcon(QIcon(
                        functions.get_resources(
                            file=item.Icon,
                            icon=True,
                            file_only=True
                        )
                    ))

                    self.item_list.addItem(
                        list_item
                    )

        if not search or self.search_bar.text() == '':
            for item in core.get_item_list():
                list_item = QtWidgets.QListWidgetItem(item.Name)
                list_item.setIcon(QIcon(
                    functions.get_resources(
                        file=item.Icon,
                        icon=True,
                        file_only=True
                    )
                ))

                self.item_list.addItem(
                    list_item
                )

    # ------------------------------------------------------------------------------------------------------------------
    def populate_item_options(self, *args, **kwargs):
        """"""
        self.item_options_list = list()

        functions.clear_widgets(self.item_options)

        item_name = self.item_list.currentItem().text()
        item = core.get_item(item_name)

        if not item:
            print(f'Could not get options for tool {item_name}')

        for item_option in item.options:
            layout, widget = functions.get_widget_options(item.options[item_option], item_option)
            self.item_options.addLayout(layout)
            self.item_options_list.append(widget)

    # ------------------------------------------------------------------------------------------------------------------
    def run_item(self, *args, **kwargs):
        """"""
        if not self.item_list.currentItem():
            print('No item has been selected')
            return

        item_name = self.item_list.currentItem().text()

        item = core.get_item(item_name)

        if not item:
            print('Could not get item named : {}'.format(item_name))
            return

        for option in item.options:

            # -- This will get the names of the setting we want to set and
            # -- set them in the tool.
            for widget_option in self.item_options_list:
                value = functions.get_values(widget_option)
                widget_name = widget_option.objectName()

                if option == widget_name:
                    item.options[option] = value

        item.run()


class ListWidget(QtWidgets.QListWidget):
    """"""
    def __init__(self):
        super(ListWidget, self).__init__()

        self.setIconSize(QtCore.QSize(32, 32))
        self.setAlternatingRowColors(True)


# ----------------------------------------------------------------------------------------------------------------------
class DockableCreator(MayaQWidgetDockableMixin, QtWidgets.QMainWindow):
    """"""
    def __init__(self, *args, **kwargs):
        super(DockableCreator, self).__init__(*args, **kwargs)


# ----------------------------------------------------------------------------------------------------------------------
def launch(*args, **kwargs):
    """"""
    window = DockableCreator(parent=functions.return_maya_main_window())
    widget = NexusTools(parent=window)

    window.setCentralWidget(widget)

    window.setWindowTitle('Nexus Tools')

    window.show(dockable=True)
