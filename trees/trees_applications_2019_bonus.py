# -*- coding: utf-8 -*-
"""
Sep 2019
S3 - trees part 3: other versions - bonus
"""

from algopy import tree, treeasbin


"""
tree -> parent vector
"""

# using "binary structure" (without the parent in parameter!)  
def __parentsbin2(B, p):
    if B.child:
        p[B.child.key] = B.key 
        __parentsbin2(B.child, p)
    if B.sibling:
        p[B.sibling.key] = p[B.key]
        __parentsbin2(B.sibling, p)

def parents(T, n):
    p = [-1] * n      
    __parentsbin2(T, p)
    return p
    
'''
tree -> list representation
'''

# Bonus (easy): using "binary structure"    
def treeAsBin2list2(B):
    s = '(' + str(B.key)
    if B.child:
        s += treeAsBin2list2(B.child)
    s += ')'
    if B.sibling:
        s += treeAsBin2list2(B.sibling)
    return s
    

"""
    levels(B: TreeAsBin) returns a list of levels (as lists of keys)
"""

# BONUS: with DFS

# an interesting version (Agola Maxime)

def __levelsDFS_bin(T, L, depth):
    L[depth].append(T.key)
    if T.child:
        if depth + 1 == len(L):
            L.append([])
        __levelsDFS_bin(T.child, L, depth+1)
    if T.sibling:        
        __levelsDFS_bin(T.sibling, L, depth)

def levelsDFS_bin(T):
    L = [[T.key]]
    if T.child:
        L.append([])
        __levelsDFS_bin(T.child, L, 1)
    return L
    
# an amazing version (Pierre Marie Callies)

def __merge(L1, L2):
        
    for i in range(min(len(L1), len(L2))):
        L1[i] = L1[i] + L2[i]
    if len(L2) > len(L1):
        L1 += L2[(len(L2)-len(L1))+1:]
    return L1 
    
    
def levelsDFS_bin2(B):
    if B == None:
        return []
    else:
        print(B.key)
        return __merge([[B.key]] + levelsDFS_bin2(B.child), 
                       levelsDFS_bin2(B.sibling))
                       
"""
equality Tree & TreeAsBin
"""

def same_bin(T,B) :
    return T.key == B.key and _same_bin(T,B.child,0)

def _same_bin(T,B,i) :
    if not B :
        return i>=T.nbchildren
    elif i>=T.nbchildren :
        return False
    else :
        C = T.children[i]
        return C.key == B.key and _same_bin(C,B.child,0) and _same_bin(T,B.sibling,i+1)

"""
TreeAsBin -> Tree
"""

# Bonus: using "binary structure"
def __treeasbin2tree2(B, parent):
    '''
    convert B -> added as new child of parent
    '''
    newChild = tree.Tree(B.key)
    parent.children.append(newChild)
    if B.sibling:
        __treeasbin2tree2(B.sibling, parent)
    if B.child:
        __treeasbin2tree2(B.child, newChild)

def treeasbin2tree_2(B):
    T = tree.Tree(B.key)
    if B.child:
        __treeasbin2tree2(B.child, T)
    return T
    
    
"""
Tree -> TreeAsBin
"""

# Bonus: using binary structure
def __tree2treeasbin(parent, i):
    '''
    build child #i of parent
    '''
    if i == parent.nbchildren:
        return None
    else:
        child_i = treeasbin.TreeAsBin(parent.children[i].key)
        child_i.sibling = __tree2treeasbin(parent, i+1)
        child_i.child = __tree2treeasbin(parent.children[i], 0)
        return child_i
    
def tree2treeasbin_2(T):
    return treeasbin.TreeAsBin(T.key, __tree2treeasbin(T, 0), None)

"""
"list representation" -> TreeAsBin (int keys)
"""

# this last one can be left as bonus (needs a real "confidence in recursivity!)
def __list2treeasbin(s, i=0): 
    if i < len(s) and s[i] == '(':   
        i = i + 1 # to pass the '('
        key = ""
        while not (s[i] in "()"):
            key = key + s[i]
            i += 1
        B = treeasbin.TreeAsBin(int(key))
        (B.child, i) = __list2treeasbin(s, i)
        i = i + 1   # to pass the ')'
        (B.sibling, i) = __list2treeasbin(s, i)
        return (B, i)
    else:
        return (None, i)

def list2treeasbin(s):
    return __list2treeasbin(s)[0]