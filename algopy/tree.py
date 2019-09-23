# -*- coding: utf-8 -*-
"""General Tree module.


*Warning:* All the functions defined in this module are assumed to receive a non-None
value for their ``ref/T`` parameter.

"""

from . import queue
from .queue import Queue


class Tree:
    """Simple class for general tree.

    Attributes:
        key (Any): Node key.
        children (List[Tree]): Node children.

    """
    def __init__(self, key=None, children=None):
        """Init general tree, ensure children are properly set.

        Args:
            key (Any).
            children (List[Tree]).

        """

        self.key = key

        if children == None:
            self.children = []
        else:
            self.children = children

    @property
    def nbchildren(self):
        """Number of children of node."""

        return len(self.children)


###############################################################################
# load and save
# use the "list" representation: (o A1 A2 ... AN).

def tree2list(T):
    #FIXME
    pass

def savetree(T, filename):
    fout = open(filename, mode='w')
    fout.write(tree2list(T))
    fout.close()
    
    
def __loadtree(s, typelt,i=0): 
    #FIXME
    pass

def loadtree(path, typelt=int):
    # Open file and get full content
    file = open(path, 'r')
    content = file.read()
    # Remove all whitespace characters for easier parsing
    content = content.replace('\n', '').replace('\r', '') \
                     .replace('\t', '').replace(' ', '')
    file.close()
    # Parse content and return tree
    (T, _) = __loadtree(content, typelt)
    return T

    
###############################################################################
# Display

def dot(ref):
    """Write simple down dot format of tree.

    Args:
        ref (Tree).

    Returns:
        str: String storing dot format of tree.

    """

    #FIXME
    pass

def display(ref):
    """Render a Tree for in-browser display.

    *Warning:* Made for use within IPython/Jupyter only.

    Args:
        ref (Tree).

    Returns:
        Source: Graphviz wrapper object for tree rendering.

    """

    # Ensure all modules are available
    try:
        from graphviz import Source
        from IPython.display import display
    except:
        raise Exception("Missing module: graphviz.")
    # Generate dot and return display object
    dot_source = dot(ref)
    display(Source(dot_source))
