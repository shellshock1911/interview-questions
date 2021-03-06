"""Given an undirected graph G, find the minimum spanning tree within G. 
   A minimum spanning tree connects all vertices in a graph with the smallest 
   possible total weight of edges. Function should take in and return an 
   adjacency list structured like this:

   {'A': [('B', 2)],
    'B': [('A', 2), ('C', 5)], 
    'C': [('B', 5)]}

    ** Taken from Udacity Machine Learning Nanodegree Program **
"""

from collections import defaultdict

class Edge(object):
    
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

class Graph(object):
 
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.parent = dict()
        self.rank = dict()
    
    def find(self, vertex):
        if self.parent[vertex] == vertex:
            return self.parent[vertex]
        else:
            return self.find(self.parent[vertex])

    def union(self, root1, root2):
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root2] > self.rank[root1]:
            self.parent[root1] = root2
        else:
            self.parent[root1] = root2
            self.rank[root2] += 1      
    
    def make_disjoint_sets(self, vertex):
        self.parent[vertex] = vertex
        self.rank[vertex] = 0

            
def MST(G):
    
    if not G:
        return None
    
    vertices = G.keys()
    edges = []
    
    graph = Graph(vertices, edges)
    
    for key in vertices:
        for value in G[key]:
            graph.edges.append(Edge(key, value[0], value[1]))
    
    min_spanning_tree = []
    
    for vertex in graph.vertices:
            graph.make_disjoint_sets(vertex)
            
    graph.edges = sorted(graph.edges, key= lambda x: x.weight)
    
    for edge in graph.edges:
        root1 = graph.find(edge.vertex1)
        root2 = graph.find(edge.vertex2)
        if root1 != root2:
            min_spanning_tree.append(edge)
            graph.union(root1, root2)
    
    mst_defaultdict = defaultdict(list)
    inverse_defaultdict = defaultdict(list)
    
    for edge in min_spanning_tree:
        mst_defaultdict[edge.vertex1].append((edge.vertex2, edge.weight))
        
    for key in mst_defaultdict:
            for value in mst_defaultdict[key]:
                inverse_defaultdict[value[0]].append((key, value[1]))
    
    for k, v in inverse_defaultdict.items():
        mst_defaultdict[k].extend(v)
    
    return dict(mst_defaultdict)
    
########################################
# Test Cases
########################################

G = {}
print MST(G)
# Output == None
G = None
# Output == None
print MST(G)
G = {
     'A': [('C', 1), ('B', 4), ('D', 3)],
     'B': [('A', 4), ('D', 5)],
     'C': [('A', 1), ('D', 2)],
     'D': [('A', 3), ('B', 5), ('C', 2)]
    }
print MST(G)
# Output == {
#            'A': [('B', 4), ('C', 1)],
#            'B': [('A', 4)]
#            'C': [('A', 1), ('D', 2)],
#            'D': [(C, 2)]
#           }
G = {
     'A': [('B', 1), ('C', 7)],
     'B': [('A', 1), ('C', 5 ), ('D', 4), ('E', 3)],
     'C': [('A', 7), ('B', 5), ('E', 6)],
     'D': [('B', 4), ('E', 2)],
     'E': [('B', 3), ('C', 6), ('D', 2)]
    }
print MST(G)
# Output == {
#            'A': [('B', 1)],
#            'B': [('A', 1), ('C', 5), ('E', 3)],
#            'C': [('B', 5)],
#            'D': [('E', 2)],
#            'E': [('B', 3), ('D', 2)]
#           }