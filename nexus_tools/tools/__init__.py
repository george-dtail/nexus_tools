"""
# Overview

Nexus Tools is a simple tools menu for Autodesk Maya. It allows the user
to quickly jump between common rigging tools to make the rigging process easier.

A user with knowledge of Python can easily add their own tools by adding new
files under the plugins folder and adding in a new class using
nexus_tools.NexusTool as the base class or adding in a new class in an already
existing file.

The easiest way to use Nexus Tools is to download the Nexus Toolls directory
from GitHub and unzip the file into your _Maya Scripts Location_ which will
likely be a similar path to this:

'''
c:/users/your_name/documents/maya/scripts
'''

Once you have unzipped the file to that location you should launch maya and
run the following command in a python tab:

...
import nexus_tools

nexus_tools.launch()
...

"""

"""
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

"""

The Icons for this project have been sourced by the amazing artists at: 
https://game-icons.net/ 

    Icon Artists {
        Delapouite
        Lorc
        Skoll
        Viscious Speed
        Caro Asercion
        sbed
        Simon (aussiesim)
        DarkZaitzev
        Cathelineau
        Quoting
        Faithtoken
        Lord Berandas
        Willdabeast
        PriorBlue
        Carl Olsen
        Lucas
        Felbrigg
        Pierre Leducq
        Guard13007
        rihlsul
        Kier Heyl
        John Redman	
        Various artists
        Zajkonur
        GeneralAce135
        Zeromancer
        Andy Meneely
        HeavenlyDog
        Pepijn Poolman
        starseeker
        catsu
        SpencerDub
        sparker
        Irongamer
        John Colburn
    }

Please check them out and support their efforts! 

"""

from . import core
from .core import NexusTool
from .core import get_item_list
from .core import get_items
from .core import get_item
