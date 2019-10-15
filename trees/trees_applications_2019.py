# -*- coding: utf-8 -*-
"""
Sep 2019
S3 - trees part 3
"""

from algopy import tree, treeasbin
from algopy import queue

"""
tree -> parent vector
"""
    
def __parents(T, p):
    for child in T.children:
        p[child.key] = T.key
        __parents(child, p)

def __parentsbin(B, p):
    C = B.child
    while C != None:
        p[C.key] = B.key
        __parentsbin(C, p)
        C = C.sibling        

def parents(T, n):
    p = [None] * n      # or [-1] * n to avoid dealing with the root!
    p[T.key] = -1
    if type(T) == tree.Tree:    # little "trick" to write a single call function
        __parents(T, p)
    else:
        __parentsbin(T, p)
    return p


"""
tree -> dot
"""

# warning: the following versions do not work if keys are not unique 
# see algopy/tree.py for a version that uses id

def dot(T):
    """Write down dot format of tree.

    Args:
        T (Tree).

    Returns:
        str: String storing dot format of tree.

    """

    s = "graph {\n"
    q = queue.Queue()
    q.enqueue(T)
    while not q.isempty():
        T = q.dequeue()
        for child in T.children:
            s = s + "   " + str(T.key) + " -- " + str(child.key) + "\n"
            q.enqueue(child)
    s += "}"
    return s

def dotBin(B):
    """Write down dot format of tree.

    Args:
        B (TreeAsBin).

    Returns:
        str: String storing dot format of tree.

    """

    s = "graph {\n"
    q = queue.Queue()
    q.enqueue(B)
    while not q.isempty():
        B = q.dequeue()
        C = B.child
        while C:
            s = s + "   " + str(B.key) + " -- " + str(C.key) + "\n"
            q.enqueue(C)
            C = C.sibling
    s += "}"
    return s

'''
tree -> list representation
'''

def tree2list(T):
    s = '(' + str(T.key)
    for child in T.children:
        s += tree2list(child)
    s += ')'
    return s

def treeAsBin2list(B):
    s = '(' + str(B.key)
    C = B.child
    while C != None:
        s += treeAsBin2list(C)
        C = C.sibling
    s += ')'
    return s
    

"""
    levels(B: TreeAsBin) returns a list of levels (as lists of keys)
"""

def levels(B):
    q = queue.Queue()
    q.enqueue(B)
    q2 = queue.Queue()
    Levels = []
    L = []
    while not q.isempty():
        B = q.dequeue()
        L.append(B.key)
        C = B.child
        while C:
            q2.enqueue(C)
            C = C.sibling
        if q.isempty():
            (q, q2) = (q2, q)
            Levels.append(L)
            L = []
    return Levels
    


"""
equality Tree & TreeAsBin
"""

# with return in loop
def same(T, B):
    if T.key != B.key:
        return False
    else:
        Bchild = B.child
        for Tchild in T.children:
            if Bchild == None or not(same(Tchild, Bchild)):
                return False
            Bchild = Bchild.sibling
    return Bchild == None

def same2(T, B):
    if B.key != T.key:
        return False
    i = 0
    C = B.child
    while i < T.nbchildren and C != None:
        if not same2(T.children[i], C):
            return False
        i += 1
        C = C.sibling
    return C == None and i == T.nbchildren

# without return in the loop
def same3(T, B):
    if T.key != B.key:
         return False
    else:
         Bchild = B.child
         i = 0
         while i < T.nbChildren and Bchild and same3(T.children[i], Bchild):
             i += 1
             Bchild = Bchild.sibling
         return i == T.nbChildren and Bchild == None
         

"""
TreeAsBin -> Tree
"""

def treeasbin2tree(B):
    T = tree.Tree(B.key, [])
    child = B.child
    while child != None:
        T.children.append(treeasbin2tree(child))
        child = child.sibling
    return T


    
"""
Tree -> TreeAsBin
"""

def TreeToTreeAsBin(T):
    B = treeasbin.TreeAsBin(T.key, None, None)
    if T.nbchildren != 0:
        B.child = TreeToTreeAsBin(T.children[0])
        S = B.child
        for i in range(1, T.nbchildren):    
            S.sibling = TreeToTreeAsBin(T.children[i])
            S = S.sibling
    return B

def Tree2TreeAsBin(T):
    B = treeasbin.TreeAsBin(T.key, None, None)
    firstchild = None
    for i in range(T.nbchildren-1, -1, -1):
        C = Tree2TreeAsBin(T.children[i])
        C.sibling = firstchild
        firstchild = C
    
    B.child = firstchild
    return B



"""
"list representation" -> Tree (int keys)
"""

def __list2tree(s, i=0): 
        i = i + 1 # to skip the '('
        key = ""
        while s[i] != '(' and s[i] != ')':  # s[i] not in "()"
            key += s[i]
            i += 1
        T = tree.Tree(int(key), [])
        while s[i] != ')':
            (C, i) = __list2tree(s, i)
            T.children.append(C)
        i += 1
        return (T, i)

def list2tree(L):
    (T, _) = __list2tree(L)
    return T


