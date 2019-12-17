# -*- coding: utf-8 -*-
"""
Graphs: traversals - BFS and DFS
"""

from algopy import graph, graphmat, queue

#------------------------------------------------------------------------------
# ex 2.1

"""
Breadth-first search (BFS)
"""

# simple BFS, vertices are marked with booleans, with adjacency matrix
# display vertices, on line per tree

def __BFS(Gmat, s, M):
    q = queue.Queue()
    q.enqueue(s)
    M[s] = True
    while not q.isempty():
        x = q.dequeue()
        print(x)
        for y in range(Gmat.order):
            if Gmat.adj[x][y]:    # x is adjacent to y
                if not M[y]:  # y is not marked
                    M[y] = True
                    q.enqueue(y)
                

def BFS(Gmat):
    M = [False] * Gmat.order
    for s in range(Gmat.order):
        if not M[s]:    #s is not marked
            __BFS(Gmat, s, M)
        print()


# BFS that builds the parent vector, used to mark vertices, 
# with adjacency lists representation

def __BFS_forest(G, s, p):
    q = queue.Queue()
    q.enqueue(s)
    p[s] = -1   # root
    while not q.isempty():
        x = q.dequeue()
        for y in G.adjlists[x]:
            if p[y] == None:
                q.enqueue(y)
                p[y] = x

def BFS_forest(G):
    p = [None] * G.order
    for s in range(G.order):
        if p[s] is None:
            __BFS(G, s, p)
    return p    # represents the spanning forest
    
    
#------------------------------------------------------------------------------
# ex 2.2 q2.4

"""
Depth first traversal (DFS)
"""

# simple DFS with adjacency lists
def __dfs(G, x, M):
    M[x] = True    # usually vertices are marked here
    print(x, end=' ')
    for y in G.adjlists[x]:
        if not M[y]: 
            __dfs(G, y, M)
                
def dfs(G):
    M = [False] * G.order
    for s in range(G.order):
        if not M[s]:
            __dfs(G, s, M)
        print()

            
# q.3(c) graph depth-first traversal with back edge detection (with adjacency matric)
# vertices are marked with parents)
            
def __dfs_backedges(Gmat, x, P):
    for y in range(Gmat.order):
        if Gmat.adj[x][y]:
            if P[y] == None: 
                P[y] = x      # vertices have to be marked here (x needed)
                print(x, "->", y)     # tree edge
                __dfs_backedges(Gmat, y, P)
            else:
                if y != P[x]:
                    print(x, '->', y, "back edge")    
                    # unless adj -> s is a back edge! *
                
def dfs_backedges(Gmat):
    P = [None] * Gmat.order #parent vector
    for s in range(Gmat.order):
        if P[s] == None:
            P[s] = -1       # s is a root
            __dfs_backedges(Gmat, s, P)
    return P

# *vertices can be marked with their depths in trees: allows to detect back edges only once!
# but usually the two versions here are sufficient (we do not care about the second encounter...)

# another version, where vertices are marked with booleans

def __dfs_backedges2(Gmat, x, p, M):    # p is x's parent
    M[x] = True
    for y in range(Gmat.order):
        if Gmat.adj[x][y]:
            if not M[y]:
                print(x, "->", y)     # tree edge
                __dfs_backedges2(Gmat, y, x, M)
            else:
                if y != p:
                    print(x, '->', y, "back edge")    
                    # unless adj -> s is a back edge! *
                
def dfs_backedges2(Gmat):
    M = [False] * Gmat.order
    for s in range(Gmat.order):
        if not M[s]:
            __dfs_backedges(Gmat, s, -1, M)

# q.4(c) digraph depth-first traversal -> prefix and suffix numbering with a single counter
# to detect edge types (with adjacency list representation)

def __dfs_digraph(G, x, pref, suff, cpt):
    cpt += 1
    pref[x] = cpt
    for y in G.adlists[x]:
        if pref[y] == None:
           # x -> y: tree edge
           cpt = __dfs_digraph(G, y, pref, suff, cpt)
        else:
            if pref[x] < pref[y]:
                print (x, "->",  y, "forward")
            else:
                if suff[y] == None:     # y has not been "marked" in suffix
                    print (x, "->",  y, "back")
                else:
                    print (x, "->",  y, "cross")
    cpt += 1
    suff[x] = cpt
    return cpt

# reminder: int values are "unmutable" => cpt cannot be passed by reference
# that why the function returns cpt!

def dfs_digraph(G):
    pref = [None] * G.order
    suff = [None] * G.order 
    cpt = 0
    for s in range(G.order):
        if pref[s] == None:
            cpt = __dfs_digraph(G, s, pref, suff, cpt)
    return(pref, suff)
