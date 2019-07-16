from queue import Queue
import graph

# heapify(), heappush() and heappop()

# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)
# build distance table
def build_distance_table(graph, source):
    distance_table = {}
    for v in range(graph._numVertices):
        distance_table[v] = (None, None)
    distance_table[source] = (0, source)
    l = [(0, source)]
    heapq.heapify(l)
    while l:
        current_vertex = heapq.heappop(l)[1]
        current_distance =distance_table[current_vertex][0]
        for vertex in graph.get_adjacent_vertices(current_vertex):
            distance = current_distance + graph.get_edge_weight(vertex, current_vertex)
            if distance_table[vertex][0] is None or distance < distance_table[vertex][0]:
                distance_table[vertex] = (distance, current_vertex)
                heapq.heappush(l, (distance, vertex))
    return distance_table

def shortest_path(graph, source, destination):
    dt =build_distance_table(graph, source)
    path = [destination]

    previous_vertex = dt[destination][1]
    while previous_vertex is not None and previous_vertex is not source:
        path = [previous_vertex] + path
        previous_vertex = dt[previous_vertex][1]

    if previous_vertex is None:
        print('There is no path btw %s and %s'%(source, destination))
    else:
        return [source]+path

if __name__ == '__main__':
    g = graph.AdjacencySetGrapgh(8, directed = False)
    g.add_edge(0, 1,1)
    g.add_edge(1, 2,2)
    g.add_edge(1, 3,6)
    g.add_edge(2, 3,2)
    g.add_edge(1, 4,3)
    g.add_edge(3, 5,1)
    g.add_edge(5, 4,3)
    g.add_edge(3, 6,1)
    g.add_edge(6, 7,1)
    g.add_edge(0, 7,8)
    print(shortest_path(g, 0, 6))
    print(shortest_path(g, 4, 7))
    print(shortest_path(g, 7, 0))
    print(shortest_path(g, 7, 4))
