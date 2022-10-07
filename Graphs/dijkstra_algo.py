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
        if not directed:  # If we want an undirected graph let's add the distance both ways
            self.graph[v][u] = distance

    def dijkstra(self, start_vertex):
        # Let's have a list which stores all the distance for each nodes from the specified starting position,
        # we will initialize it with infinity
        self.D = {v: float('inf') for v in range(self.v)}

        self.D[start_vertex] = 0  # Distance of the first vertex is always 0
        heapq.heappush(self.pq, (
        0, start_vertex))  # Push the first vertex in the priority queue and it's corresponding distance is 0

        while len(self.pq):
            (dist, current_vertex) = heapq.heappop(self.pq)
            self.visited.append(
                current_vertex)  # Append the visited nodes in the list to keep a track of the visited nodes

            # Need to check who are the neighbors of the current node
            for neighbor in range(self.v):
                # Since we are iterating through the neighbor list we check if there exists a connection then we
                # update our distance accordingly.
                if self.graph[current_vertex][neighbor] != -1:
                    distance = self.graph[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_distance = self.D[neighbor]
                        new_distance = self.D[current_vertex] + distance
                        # If the new distance to the neighbor is less then expand the graph to incorporate the lesser
                        # one and discard the old one
                        if new_distance < old_distance:
                            self.D[neighbor] = new_distance
                            # Since we have found the neighbor we want to include we will push it to the priority
                            # queue for visiting next time.
                            heapq.heappush(self.pq, (new_distance, neighbor))

        return self.D


connection_type = 1  # 0 for undirected & 1 for directed

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
    print(g.graph)
    print(g.dijkstra(0))
