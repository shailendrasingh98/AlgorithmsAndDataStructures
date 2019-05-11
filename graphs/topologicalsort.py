from queue import Queue
import graph

def topologicalSort(graph):
    indegree_map = {}
    queue = Queue()
    for v in range(graph._numVertices):
        indegree_map[v] = graph.get_indegree(v)

        if indegree_map[v] ==0:
            queue.put(v)
    sorted_list = []
    while not empty():
        vertex = queue.get()
        sorted_list.append(vertex)
        for v in graph.get_adjacent_vertices(vertex):
            indegree_map[v]-=1
            if indegree_map[v] ==0:
                queue.put(v)
    if len(sorted_list) == graph._numVertices:
        raise ValueError('Graph has cycle')
    return sorted_list
