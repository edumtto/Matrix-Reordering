'''
    Author: Eduardo Motta de Oliveira
'''
import graph

'''
def load(file):

    f = open (file, "r")
    if f.mode == "r":
        lines = f.readlines()
        k = 0
        while lines[k][0] == '%':
            k = k + 1

        h = lines[k][0:-1].split(' ')

        #print 'Dimensoes: {m}x{n}, nao nulos: {nnul}'.format(m=h[0], n=h[1], nnul=h[2])
        
        mat = [ [ 0.0 for i in range(int(h[0])) ] for j in range(int(h[1])) ]

        for l in lines[k:]:
            str = l[0:-1].split()

            i = int(str[0]) - 1
            j = int(str[1]) - 1
            mat[i][j] = float(str[2])
  
        return mat

    return None
'''

def load(file):

    f = open (file, "r")
    if f.mode == "r":
        lines = f.readlines()
        k = 0
        while lines[k][0] == '%':
            k = k + 1

        h = lines[k][0:-1].split(' ')

        print 'Dimensoes: {m}x{n}, nao nulos: {nnul}'.format(m=h[0], n=h[1], nnul=h[2])
        
        dimension = int(h[0])
        g = graph.Graph(dimension)

        for l in lines[k:]:
            strs = l[0:-1].split()

            u = int(strs[0]) - 1
            v = int(strs[1]) - 1
            if u != v:
                g.add_edge(u, v)

        return g

    return None


if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    g = load(filename)
    print g