#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S3 - graph tutorial
Find a path between 2 vertices
"""

from algopy import graph, queue

"""
BFS and DFS can be both used to test if there is a path between two vertices.
If we want to find the path, BFS is the one that gives the shortest (in edge number)
try with "graph_12-20.gra" from 0 or 1 to 12
"""


# path with BFS: uses the parent vector to build the path

def __bfs(G, s, dst, p):
    q = queue.Queue()
    q.enqueue(s)
    p[s] = -1    
    while not q.isempty():
        s = q.dequeue()
        for adj in G.adjlists[s]:
            if p[adj] is None: 
                p[adj] = s
                if adj == dst:
                    return True
                q.enqueue(adj)
    return False       
                
def path_bfs(G, src, dst):
    p = [None] * G.order
    path = []
    if __bfs(G, src, dst, p):
        while dst != -1:
            path.insert(0, dst) # or path = [dst] + path
            dst = p[dst]
    return path
    
# with DFS: parent vector can also be used.
# here, the path is built going up

def __dfs(G, s, dst, M, path):
    M[s] = True
    for adj in G.adjlists[s]:
        if not M[adj]:
            if adj == dst or __dfs(G, adj, dst, M, path):
                path.insert(0, adj) 
                return True
    return False

def path_dfs(G, src, dst):
    M = [False] * G.order
    path = []    
    if __dfs(G, src, dst, M, path):
        path.insert(0, src) 
    return path
    
# another version: the recursive function returns the path if found, [] otherwise
def __dfs2(G, s, dst, M):
    M[s] = True
    for adj in G.adjlists[s]:
        if not M[adj]:
            if adj == dst:
                return [dst]
            else:
                path = __dfs2(G, adj, dst, M)
                if path != []:
                    return [adj] + path
    return []

def path_dfs2(G, src, dst):
    M = [False] * G.order
    path = __dfs2(G, src, dst, M)
    if path:
        return [src] + path
    else:
        return []
    
    

    
    
    
    
                
