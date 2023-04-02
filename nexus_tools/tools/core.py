import inspect
import os

from importlib import machinery

_ITEM_LIST = list()


# ----------------------------------------------------------------------------------------------------------------------
class NexusTool(object):

    # -- The Identifier for the tool
    Name = 'Tool : Undefined'

    Icon = 'auto_repair.png'

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):

        # -- An empty dictionary of options used by the tools
        self.options = dict()

    # ------------------------------------------------------------------------------------------------------------------
    def run(self, *args, **kwargs):

        return None


# ----------------------------------------------------------------------------------------------------------------------
def get_items():
    """"""
    global _ITEM_LIST

    # -- If we have our tools list, we will return those tools.
    if _ITEM_LIST:
        return _ITEM_LIST

        # -- This gets the location directly from this file
    control_location = os.path.dirname(__file__).replace('\'', '/')

    for root, _, files in os.walk(control_location):
        for filename in files:

            filepath = os.path.join(root, filename)

            loader = machinery.SourceFileLoader(
                'NEXUS_TOOL_' + filename.replace('.', '_'),
                filepath
            )

            module = loader.load_module()

            for item_name in dir(module):

                item_object = getattr(module, item_name)

                if inspect.isclass(item_object):

                    if issubclass(item_object, NexusTool):
                        _ITEM_LIST.append(item_object())

    return True


def get_item_list():
    """
    A convenience function that we can run to get our tools.
    :return: a list of tool class instances.
    """

    get_items()

    return _ITEM_LIST


def get_item(name):
    """
    Gets the tool that we want to run using its name.
    param name: The name of the tool that we are running.
    :return: an instance of the tool.
    """
    for item in get_item_list():
        if item.Name == name:
            return item

    return None
