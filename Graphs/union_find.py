from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        # Let's use adjacency list for defining our graph in a more compressed way
        self.graph = defaultdict(list)

    def add_connection(self, u, v):
        self.graph[u].append(v)

    def find_parent(self, u):
        
