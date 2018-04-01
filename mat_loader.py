
'''
    Author: Eduardo Motta de Oliveira
'''
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def load(file):

    f = open (file, "r")
    if f.mode == "r":
        lines = f.readlines()
        k = 0
        while lines[k][0] == '%':
            k = k + 1

        h = lines[k][0:-1].split(' ')

        print 'Dimensoes: {m}x{n}, nao nulos: {nnul}'.format(m=h[0], n=h[1], nnul=h[2])
        
        mat = [ [ 0.0 for i in range(int(h[0])) ] for j in range(int(h[1])) ]

        for l in lines[k:]:
            str = l[0:-1].split()

            i = int(str[0]) - 1
            j = int(str[1]) - 1
            mat[i][j] = float(str[2])
    
        '''
        for row in mat:
            print row
        '''
        return mat

    return None

def show_graph_with_labels(adj_mat):
    G = nx.from_numpy_matrix(np.array(adj_mat)) 
    nx.draw(G, with_labels=True)
    plt.show()


if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    print 'opening ', filename
    mat = load(filename)
    show_graph_with_labels(mat)
