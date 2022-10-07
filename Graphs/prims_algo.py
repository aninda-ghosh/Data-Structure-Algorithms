import graphlib
import heapq    

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        # This is the adjacency matric of the graph
        self.graph = [[-1 for column in range(vertices)] for row in range(vertices)]
        # List of visited nodes
        self.visited = []   
        # Priority queue to store the distance of the currently being visited nodes
        self.pq = []        
       

    def add_conection(self, u, v, distance, directed):
        # This function forms the graph by establishing some connection weights
        self.graph[u][v] = distance
        if not directed:    # If we want an undirected graph let's add the distance both ways
            self.graph[v][u] = distance

    def prims(self, start_vertex):
        # initialize all the vertex weights as infinity.
        self.D = {v:float('inf') for v in range(self.v)}


        self.D[start_vertex] = 0  #Distance of the first vertex is always 0
        cost_of_attachment = 0
        heapq.heappush(self.pq, (cost_of_attachment, start_vertex))  #Push the first vertex in the priority queue and it's corresponding distance is 0

        while len(self.pq):
            (distance, current_index) = heapq.heappop(self.pq)
            self.visited.append(current_index)
            for neighbor in range(self.v):
                if(self.graph[current_index][neighbor] != -1):  # Find Neighbors
                    cost_of_attachment = self.graph[current_index][neighbor]
                    if neighbor not in self.visited:
                        # If the node is not visited take a judgement based on the cost of attachment of that node.
                        if cost_of_attachment < self.D[neighbor]:
                            self.D[neighbor] = cost_of_attachment
                        heapq.heappush(self.pq, (cost_of_attachment, neighbor))
        
        return self.D
                    
connection_type = 0 # 0 for undirected & 1 for directed

if __name__ == "__main__":
    g = Graph(6)
    g.add_conection(0, 1, 4, connection_type)
    g.add_conection(0, 5, 7, connection_type)
    g.add_conection(1, 5, 11, connection_type)
    g.add_conection(1, 4, 20, connection_type)
    g.add_conection(1, 2, 9, connection_type)
    g.add_conection(2, 3, 2, connection_type)
    g.add_conection(3, 4, 1, connection_type)
    g.add_conection(4, 5, 1, connection_type)

    print(g.prims(1))        

