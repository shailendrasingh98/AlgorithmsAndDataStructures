from queue import Queue
import graph


# Implementing unweighted shortet path algorithm in python

def build_distance_table(g, source):
    # A dictionary mapping from vertex number to tuple of
    # (distance from source, last vertex on path from source)
    distance_table = {}
    for i in range(g._numVertices):
        distance_table[i] = (None, None)

    # The distance to the source from itself is 0
    distance_table[source] = (0, source)

    q = Queue()
    q.put(source)

    while not q.empty():
        current_vertex = q.get()
        #The distance of current vertex from source
        current_distance = distance_table[current_vertex][0]

        for neighbor in g.get_adjacent_vertices(current_vertex):
            # only update the distance table if no current distance
            # is found in table
            if distance_table[neighbor][0] is None:
                distance_table[neighbor] = (1 + current_distance,current_vertex)

                #Enqueue this only if it has other adjacent vertices to explore
                if len(g.get_adjacent_vertices(neighbor)) > 0:
                    q.put(neighbor)
    return distance_table

def shortet_path(g, source, destination):

    distance_table = build_distance_table(g, source)
    #print(distance_table)
    # use array as stack
    path = [destination]
    previous_vertex = distance_table[destination][1]

    while previous_vertex is not None and previous_vertex is not source:
        path = [previous_vertex] + path
        previous_vertex = distance_table[previous_vertex][1]

    #print(previous_vertex)
    if previous_vertex is None:
        print('Shortet path does not exist btw %s and %s' %(source, destination))
    else:
        path = [source] + path
        print('Shortet path btw %s and %s is :' %(source, destination))
        print(*path)

if __name__ == '__main__':
    g = graph.AdjacencySetGrapgh(8, directed = False)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(1, 4)
    g.add_edge(3, 5)
    g.add_edge(5, 4)
    g.add_edge(3, 6)
    g.add_edge(6, 7)
    g.add_edge(0, 7)
    shortet_path(g, 0, 3)
    shortet_path(g, 0, 5)
    shortet_path(g, 0, 6)
    shortet_path(g, 7, 4)

    g = graph.GraphUsingDefualtDict(4)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(0, 1)
    g.add_edge(2, 3)
    g.add_edge(1, 2)
    shortet_path(g, 0, 3)
