# -*- coding: utf-8 -*-
"""General Tree module: first child - right sibling representation.

*Warning:* All the functions defined in this module are assumed to receive a non-None
value for their ``ref/B`` parameter.

"""

from . import queue
from .queue import Queue

class TreeAsBin:
    """
    Simple class for (General) Trees 
    represented as Binary Trees (first child - right sibling)
    """

    def __init__(self, key, child=None, sibling=None):
        """
        Init Tree
        """
        self.key = key
        self.child = child
        self.sibling = sibling


###############################################################################
# load and save

def tree2list(B):
    #FIXME
    pass

def savetree(B, filename):
    fout = open(filename, mode='w')
    fout.write(tree2list(B))
    fout.close()
    
    
def __loadtree(s, typelt, i=0): 
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

def dot(B):
    """Write down simple dot format of tree.

    Args:
        B (TreeAsBin).

    Returns:
        str: String storing dot format of tree.

    """

    #FIXME
    pass

def display(B):
    try:
        from IPython.display import display
        from graphviz import Source
    except:
        raise Exception("Missing module: graphviz and/or IPython.")
    display(Source(dot(B)))
    
