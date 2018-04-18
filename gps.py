'''
    Author: Eduardo Motta de Oliveira
'''
import mat_loader
import rls
import peripherals
import random
import plot

'''Original GPS'''
def recursive_gps(m):

    dimension = len(m, iter)
    u = random.randint(0, dimension - 1)
    return recursive_rls(m, u, iter)
    
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

def iterative_gps(m, iter):
    plot_count = 0

    dimension = len(m)
    p = peripherals.Peripherals(0, 0, 0)

    #root = random.randint(0, dimension - 1)
    root = get_min_degree_node(m)

    explore = [root]
    checked = [False for i in range(dimension)]
    while iter > 0 and explore:

        v = explore.pop(0)
        rls_v = rls.buildRLS(m, v)
        checked[v] = True
        
        #print rls_v.levelsArray
        
        for w in rls_v.lastLevel():
            if checked[w] == False:
                explore.append(w)

        p_v = peripherals.Peripherals(v, rls_v.lastLevel()[0], rls_v.numLevels() - 1)

        if p_v.diameter > p.diameter:
            p.copy(p_v)

        iter = iter - 1

        #plot.plot_graph(m, str(plot_count), checked)
        #plot_count = plot_count + 1

    #checked[p.b] = True
    #plot.plot_graph(m, str(plot_count), checked)
    return p

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
