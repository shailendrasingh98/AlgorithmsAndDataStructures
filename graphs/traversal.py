from queue import Queue
import graph
import numpy as np

def breadth_first_search(graph, start = 0):
    q = Queue()
    q.put(start)
    visited = np.zeros(graph._numVertices)
    while not q.empty():
        vertex = q.get()

        if visited[vertex] ==1:continue
        print('Visit: ', vertex)
        visited[vertex] =1
        for v in graph.get_adjacent_vertices(vertex):
            if visited[v] !=1:
                q.put(v)

# Function to print a BFS of graph
def BFS(graph, s = 0):

    # Mark all the vertices as not visited
    visited = [False] * (len(graph))

    # Create a queue for BFS
    queue = []

    # Mark the source node as
    # visited and enqueue it
    queue.append(s)
    visited[s] = True

    while queue:

        # Dequeue a vertex from
        # queue and print it
        s = queue.pop(0)
        print (s, end = " ")

        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        for i in graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

def depth_first(graph, visited, current = 0):
    if visited[current] ==1:
        return

    visited[current] = 1
    print('Visited: ', current)
    for vertex in graph.get_adjacent_vertices(current):
        depth_first(grapgh, visited, vertex)




if __name__ == '__main__':
    g = graph.AdjacencyMatrixGrapgh(4)
    g.add_edge(0, 3)
    g.add_edge(1, 3)
    g.add_edge(0, 1)
    g.add_edge(2, 3)
    g.add_edge(1, 2)
    breadth_first_search(g)

    g = graph.GraphUsingDefualtDict(4)
    g.add_edge(0, 3)
    g.add_edge(1, 3)
    g.add_edge(0, 1)
    g.add_edge(2, 3)
    g.add_edge(1, 2)
    BFS(g.graph)
