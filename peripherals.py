import rls
import mat_loader

class Peripherals:

    def __init__(self, a, b, diameter):
        self.a = a
        self.b = b
        self.diameter = diameter

    def copy(self, p):
        self.a = p.a
        self.b = p.b
        self.diameter = p.diameter
    

def findPeripherals(m):

    dimension = len(m)
    p = Peripherals(0, 0, 0)
    for v in range(dimension):
        rls_v = rls.buildRLS(m, v)
        print rls_v.levelsArray
        p_v = Peripherals(v, rls_v.lastLevel()[0], rls_v.numLevels() - 1)
        if p_v.diameter > p.diameter:
            p.copy(p_v)

    return p

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
    p = findPeripherals(mat)
    print 'Pseudo-perifericos: {a} e {b}, Diametro: {diameter}'.format(
        a=p.a, b=p.b, diameter=p.diameter)