class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, vertices):
        self.graph[vertices[0]].append(vertices[1])
        self.graph[vertices[1]].append(vertices[0])

    def get_neighbors(self, vertex):
        return self.graph[vertex]

    def get_incident_edges(self, vertex):
        edges = []
        for v in self.graph[vertex]:
            edges.append((vertex, v))
        return edges

    def is_reachable(self, v1, target): #iterative DFS
        # order 1 solution is run DFS on the graph, each component is the visited list, if nodes in same component, then reachable
        # else, it is not
        # run DFS on each unvisited node
        def dfs(graph, v1):
            visited = []
            to_visit = [v1]
            while to_visit:
                curr = to_visit.pop(0)
                if curr in visited:
                    break
                visited.append(curr)
                for vertex in self.get_neighbors(curr):
                    if vertex not in visited: 
                        to_visit.append(vertex)
            return visited

        components = []
        visited = []
        unvisited = list(self.graph.keys())

        i = 0
        while i < len(unvisited):
            visited += dfs(self.graph, self.graph.keys()[0])
            # subtract visited nodes from unvisited, bundle this def into preprocessing and call another function for the search
            

    def __repr__(self):
        return str(self.graph)
