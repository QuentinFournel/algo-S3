# -*- coding: utf-8 -*-
"""
November 2019
S3 tutorial
"""

from algopy import graph, queue

"""
connected components: DFS or BFS
"full" traversal
Marks: the number of the component (here 0 for unmarked)
"""

# DFS

def __components(G, s, cc, no):
    cc[s] = no
    for adj in G.adjlists[s]:
        if cc[adj] == 0:
            __components(G, adj, cc, no)

def components(G):
    cc = [0] * G.order
    no = 0
    for s in range(G.order):
        if cc[s] == 0:
            no += 1
            __components(G, s, cc, no)
    return (no, cc)

# BFS

def __componentsBFS(G, s, cc, nocc):

    q = queue.Queue()
    q.enqueue(s)
    cc[s] = nocc
    while not q.isempty():
        s = q.dequeue()
        for adj in G.adjlists[s]:
            if cc[adj] is None:
                q.enqueue(adj)
                cc[adj] = nocc
                
            
def componentsBFS(G):
    cc = [None] * G.order
    k = 0
    for s in range(G.order):
        if cc[s] is None:
            k += 1
            __componentsBFS(G, s, cc, k)
    return (k, cc)


"""
diameter: BFS (as for all problems dealing with the "distances")
Here, the graph is a tree (does not work for any graph)
Marks: the distance form the first vertex (= the depth in the spanning tree / None for unmarked)
"""

def __distances(G, s):
    dist = [None] * G.order
    dist[s] = 0
    q = queue.Queue()
    q.enqueue(s)
    while not q.isempty():
        s = q.dequeue()
        for adj in G.adjlists[s]:
            if dist[adj] == None:
                dist[adj] = dist[s] + 1
                q.enqueue(adj)
                
    return (s, dist[s])

def diameter(G):
    (s2, _) = __distances(G, 0)
    (_, diam) = __distances(G, s2)
    return diam


"""
bipartite: both traversals
"full" traversal
Marks: for each vertex s, Set[s] is 0 for unmarked, 1 for first set (or color) -1 for second one
"""



# with DFS
def __bipartite(G, s, Set):
    for adj in G.adjlists[s]:
        if Set[adj] == 0:
            Set[adj] = -Set[s]
            if not __bipartite(G, adj, Set):
                return False
        else:
            if Set[adj] == Set[s]:
                return False
    return True
    
def bipartite(G):
    Set = [0] * G.order
    for s in range(G.order):
        if Set[s] == 0:
            Set[s] = 1
            if not __bipartite(G, s, Set):
                return False
    return True

# with BFS
def __bipartiteBFS(G, s, Set):
    q = queue.Queue()
    q.enqueue(s)
    Set[s] = 1  
    while not q.isempty():
        s = q.dequeue()
        for adj in G.adjlists[s]:
            if Set[adj] == 0:       
                Set[adj] = -Set[s]
                q.enqueue(adj)
            else:
                if Set[s] == Set[adj]:
                    return False
    return True 
    
def bipartiteBFS(G):
    Set = [0] * G.order
    for s in range(G.order):
        if Set[s] == 0:
            if not __bipartiteBFS(G, s, Set):
                return False
    return True


"""
Euler: DFS or BFS
"""

# DFS

def __isEulerian(G, s, M):
    """
    returns (nb, odd) = (nb met vertices, nb odd vertices)
    stops as soon as the third odd vertex is met
    """
    M[s] = True
    nb = 1
    deg = len(G.adjlists[s])
    odd = 0
    for adj in G.adjlists[s]:
        if adj == s:    # loop!
            deg += 1
        if not M[adj]:
            (n, o) = __isEulerian(G, adj, M)
            nb += n
            odd += o
            if odd > 2:
                return (nb, odd)
    odd += deg % 2
    return (nb, odd)
    
def isEulerian(G):
    M = [False] * G.order
    (nb, odd) = __isEulerian(G, 0, M)
    return (nb == G.order) and (odd < 3)
    
# BFS

def __isEulerianBFS(G, s, M):
    q = queue.Queue()
    q.enqueue(s)
    M[s] = True
    (odd, nb) = 0
    while not q.isempty():
        s = q.dequeue()
        deg = 0
        nb += 1
        for adj in G.adjlists[s]:
            deg += 1
            if not M[adj]:
                q.enqueue(adj)
                M[adj] = True
        odd += deg % 2
        if odd > 2:
            return (nb, odd)
    return (nb, odd)
                
                



"""
Topological sort: DFS
"""

def dfsSuff(G, s, M, L):
    M[s] = True
    for adj in G.adjlists[s]:
        if not M[adj]:
            dfsSuff(G, adj, M, L)
    L.insert(0, s)

def topologicalOrderDFS(G):
    M = [False] * G.order
    L = []
    for s in range(G.order):
        if not M[s]:
            dfsSuff(G, s, M, L)
    return L
    
