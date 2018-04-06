'''
    Author: Eduardo Motta de Oliveira
'''
import mat_loader
import rls
import peripherals
import random

'''Original GPS'''
def gps(m):

    dimension = len(m)
    u = random.randint(0, dimension - 1)
    '''
    print 'Comecando busca por', u
    '''
    return recursive_rls(m, u, 3)
    
        
def recursive_rls(m, u, iter):

    rls_u = rls.buildRLS(m, u)
    print rls_u.levelsArray
    p = peripherals.Peripherals(u, rls_u.lastLevel()[0], rls_u.numLevels() - 1)

    if iter <= 1:
        return p
    print 'lastlevel: ',  rls_u.lastLevel()
    for v in rls_u.lastLevel():
        p_v = recursive_rls(m, v, iter - 1)
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
    p = gps(mat)
    print 'Pseudo-perifericos: {a} e {b}, Diametro: {diameter}'.format(
        a=p.a, b=p.b, diameter=p.diameter)
