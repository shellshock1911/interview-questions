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
    
    def makeset(self, vertex):
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
            graph.makeset(vertex)
    graph.edges = sorted(graph.edges, key= lambda x: x.weight)
    for edge in graph.edges:
        root1 = graph.find(edge.vertex1)
        root2 = graph.find(edge.vertex2)
        if root1 != root2:
            min_spanning_tree.append(edge)
            graph.union(root1, root2)
    
    mst_defaultdict = defaultdict(list)
    for edge in min_spanning_tree:
        mst_defaultdict[edge.vertex1].append((edge.vertex2, edge.weight))
        
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
#            'C': [('D', 2)]
#           }