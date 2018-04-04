'''
    Author: Eduardo Motta de Oliveira
'''
import mat_loader
import peripheral
import random

class Peripherals:

    def __init__(self, a, b, dist):
        self.a = a
        self.b = b
        self.dist = dist

    def copy(self, p):
        self.a = p.a
        self.b = p.b
        self.dist = p.dist
    

def recursive_rls(m, u, iter):

    rls = peripheral.buildRLS(m, u)
    p = Peripherals(u, rls.lastLevel()[0], rls.numLevels() - 1)

    if iter == 1:
        return p

    for v in rls.lastLevel():
        p_v = recursive_rls(m, v, iter - 1)
        if p_v.dist > p.dist:
            p.copy(p_v)

    return p

'''Original GPS'''
def gps(m):

    dimension = len(m)
    u = random.randint(0, dimension - 1)
    print 'Comecando busca por', u

    p = recursive_rls(m, u, 3)
    print 'Pseudo-perifericos: {a} e {b}, distancia: {dist}'.format(a=p.a, b=p.b, dist=p.dist)
        

'''Main'''
if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    print 'importing ', filename
    mat = mat_loader.load(filename)
    '''
    mat_loader.show_graph_with_labels(mat)
    '''
    print ' '
    gps(mat)
