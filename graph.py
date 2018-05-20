# http://www.bogotobogo.com/python/python_graph_data_structures.php

import numpy


# list of list of dictionaries
'''
class Graph:

    def __init__(self, dimension):
        self.dimension = dimension # Integer
        self.adjacencies = [ set() for i in range(dimension) ]

    def add_edge(self, u, v, weight = 0):
        self.adjacencies[u].add(v)
    
    def __str__(self):
        s = ''
        for i in range(self.dimension):
            s = s + str(i) + ' ->'
            for v in self.adjacencies[i]:
                s = s + ' ' + str(v)
            s = s + '\n'
        return s

    def get_dimension(self):
        return self.dimension

    def __len__(self):
        return self.dimension

    def get_neighbours(self, v):
        return self.adjacencies[v]

    def get_degree(self, v):
        return len(self.adjacencies[v])


'''

class Graph:

    def __init__(self, dimension):
        self.dimension = dimension # Integer
        self.mat = [ [ 0.0 for i in range(dimension) ] for j in range(dimension) ]

    def add_edge(self, u, v, weight = 1.0):
        self.mat[u][v] = weight
    
    def __str__(self):
        s = ''
        for i in range(self.dimension):
            s = s + str(self.mat[i]) + '\n'
        return s

    def get_dimension(self):
        return self.dimension

    def __len__(self):
        return self.dimension

    def get_neighbours(self, v):
        n = []
        for i in range(self.dimension):
            if self.mat[v][i] != 0:
                n.append(i)

        return n

    def get_degree(self, v):
        return numpy.count_nonzero(self.mat[v])
    
    #def __getitem__(a, b):
    #    if 



''' Tests
g = Graph(10)
g.add_edge(0, 3)
g.add_edge(0, 5)
g.add_edge(6, 7)
g.add_edge(0, 2)

print g.get_neighbours(0)

print g

'''

    

