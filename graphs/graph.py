import abc
import numpy as np
from collections import defaultdict

class Graph(abc.ABC):
    """Graph implementation rpr by adjacency matrix"""
    def __init__(self, numVertices, directed = False):
        self._numVertices = numVertices
        self._directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight = 1):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self,v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self,v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass

class AdjacencyMatrixGrapgh(Graph):
    '''Graph representated by adjacency matrix'''
    def __init__(self, numVertices, directed = False):
        super(AdjacencyMatrixGrapgh, self).__init__(numVertices, directed = directed)
        self._matrix = np.zeros((numVertices, numVertices))

    def add_edge(self, v1, v2, weight = 1):
        if v1 >= self._numVertices or v2 >= self._numVertices or v1 <0 or v2 <0:
            raise ValueError('Vertices %d and %d are out of bounds'%(v1, v2))

        if weight<1:
            raise ValueError('Edges can not have weight <1')
        self._matrix[v1][v2] = weight
        if not self._directed:
            self._matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        if v >= self._numVertices or v <0:
            raise ValueError('Vertice %d is out of bounds'%(v))
        adjacent_vertices = []
        for i in range(self._numVertices):
            if self._matrix[v][i] >=1:
                adjacent_vertices.append(i)
        return adjacent_vertices

    def get_indegree(self, v):
        if v >= self._numVertices or v <0:
            raise ValueError('Vertice %d is out of bounds'%(v))
        indegree = 0
        for i in range(self._numVertices):
            if self._matrix[i][v] >=1:
                indegree+=1
        return indegree

    def get_edge_weight(self,v1, v2):
        return self._matrix[v1][v2]

    def display(self):
        for i in range(self._numVertices):
            for v in self.get_adjacent_vertices(i):
                print("%d ==> %d"%(i, v))


class Node:
    def __init__(self, vertexId):
        self._vertexId = vertexId
        self._adjacency_set = set()

    def add_edge(self, v):
        if v== self._vertexId:
            raise ValueError("Vertex %d cann't be adjacent to itself" % v)
        self._adjacency_set.add(v)

    def get_adjacent_vertices(self):
        return sorted(self._adjacency_set)


class AdjacencySetGrapgh(Graph):
    """Graph representated by adjacency set"""

    def __init__(self, numVertices, directed = False):
        super(AdjacencySetGrapgh, self).__init__(numVertices, directed = directed)
        self._vertex_list = []
        for i in range(self._numVertices):
            self._vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight = 1):
        if v1 >= self._numVertices or v2 >= self._numVertices or v1 <0 or v2 <0:
            raise ValueError('Vertices %d and %d are out of bounds'%(v1, v2))

        if weight!=1:
            raise ValueError('Edges can not have weight !=1')
        self._vertex_list[v1].add_edge(v2)
        if not self._directed:
            self._vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        if v >= self._numVertices or v <0:
            raise ValueError('Vertice %d is out of bounds'%(v))

        return self._vertex_list[v].get_adjacent_vertices()

    def get_indegree(self, v):
        if v >= self._numVertices or v <0:
            raise ValueError('Vertice %d is out of bounds'%(v))
        indegree = 0
        for i in range(self._numVertices):
            if v in self.get_adjacent_vertices(i):
                indegree +=1
        return indegree

    def get_edge_weight(self,v1, v2):
        return 1 # as we are using unweighted Graph

    def display(self):
        for i in range(self._numVertices):
            for v in self.get_adjacent_vertices(i):
                print("%d ==> %d"%(i, v))


# This class represents a directed graph
# using adjacency list representation
class GraphUsingDefualtDict(Graph):

    # Constructor
    def __init__(self, numVertices, directed = False):
        super(GraphUsingDefualtDict, self).__init__(numVertices, directed = directed)
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def add_edge(self,v1,v2, weight = 1):
        if v1 >= self._numVertices or v2 >= self._numVertices or v1 <0 or v2 <0:
            raise ValueError('Vertices %d and %d are out of bounds'%(v1, v2))

        if weight != 1:
            raise ValueError('Edges can not have weight != 1')
        self.graph[v1].append(v2)
        if not self._directed:
            self.graph[v2].append(v1)

    def get_adjacent_vertices(self, v):
        if v >= self._numVertices or v <0:
            raise ValueError('Vertice %d is out of bounds'%(v))
        return self.graph[v]

    def get_indegree(self, v):
        if v >= self._numVertices or v <0:
            raise ValueError('Vertice %d is out of bounds'%(v))
        indegree = 0
        for i in range(self._numVertices):
            if v in self.graph(i):
                indegree +=1
        return indegree

    def get_edge_weight(self,v1, v2):
        return 1

    def display(self):
        for i in range(self._numVertices):
            for v in self.get_adjacent_vertices(i):
                print("%d ==> %d"%(i, v))

if __name__ == '__main__':
    g = AdjacencySetGrapgh(4) #for 4 Nodes
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(1, 3)
    g.add_edge(0, 2)
    print(g.get_adjacent_vertices(3))
