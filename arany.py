'''
    Author: Eduardo Motta de Oliveira
'''
import mat_loader
import rls
import peripherals
import random

'''Original Arany'''
def arany_method(m):

    dimension = len(m)

    #root = random.randint(0, dimension - 1)
    root = get_min_degree_node(m)

    explore = [root]
    checked = [False for i in range(dimension)]
    while iter > 0 and explore:

        u = explore.pop(0)
        rls_u = rls.buildRLS(m, u)
        #checked[u] = True
        #print rls_u.levelsArray

        v = rls_u.lastLevel()[0]
        rls_v = rls.buildRLS(m, v)
        #print rls_v.levelsArray

        reversible_set = get_intersection(rls_u.levelsArray, rls_v.levelsArray)
        #print reversible_set

        m_uv = reversible_set[len(reversible_set) // 2]
        #print m_uv

        a = m_uv.pop()
        rls_a = rls.buildRLS(m, a)
   
        p = peripherals.Peripherals(0, 0, 0)

        for x in rls_a.lastLevel():
            rls_x = rls.buildRLS(m, x)
            p_x = peripherals.Peripherals(x, rls_x.lastLevel()[0], rls_x.numLevels() - 1)

            if p_x.diameter > p.diameter:
                p.copy(p_x)

    return p
    

''' The reversible set R(u,v) is the set of vertices
which lie on a shortest path from u to v.
'''
def get_intersection(ls_u, ls_v):

    intersection = []
    h_u = len(ls_u)

    return [ set(ls_v[i]).intersection(ls_u[h_u - i - 1])
           for i in range(h_u) ]


def get_min_degree_node(m):
    dimension = len(m)

    import numpy
    min_degree_node = 0
    min_degree = numpy.count_nonzero(m[0])

    for i in range(dimension):
        degree = numpy.count_nonzero(m[i])
        if degree < min_degree:
            #print '{} < {}'.format(degree, min_degree)
            min_degree = degree
            min_degree_node = i
    
    print 'min degree node: {}'.format(min_degree_node)
    return min_degree_node