"""bellman-ford"""

from collections import defaultdict

def bellman_ford(graph, source):
    """bellman-ford code"""
    # Step 1: Initialize distances to all vertices as infinity and the source vertex to 0
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0

    # Step 2: Relax all edges |V| - 1 times, where |V| is the number of vertices
    vertices = list(graph.keys())
    num_vertices = len(vertices)

    # The middle and inner loops ensure every vertex and its outgoing edges
    # are considered in iteration
    for _ in range(num_vertices - 1):
        for v in vertices:
            for neighbor, weight in graph[v]:
                if distances[v] + weight < distances[neighbor]:
                    distances[neighbor] = distances[v] + weight

    # Step 3: Check for negative weight cycles
    for v in vertices:
        for neighbor, weight in graph[v]:
            if distances[v] + weight < distances[neighbor]:
                print("Graph contains negative weight cycle")
                return

    return distances

# Your graph representation
graph_rep = defaultdict(list)
graph_rep[0] = [(1, 11), (2, 5)]
graph_rep[1] = [(3, 2)]
graph_rep[2] = [(1, 4), (3, 6)]
graph_rep[3] = []

SOURCE_VERTEX = 0
shortest_distances = bellman_ford(graph_rep, SOURCE_VERTEX)

# Print the shortest distances from the source vertex to all other vertices
for vertex, distance in shortest_distances.items():
    print(f"Shortest distance from {SOURCE_VERTEX} to {vertex} is {distance}")
