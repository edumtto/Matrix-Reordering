'''
    Author: Eduardo Motta de Oliveira
'''
import graph
import mat_loader
import rls
import peripherals
import random
import plot
import util

import time
import sys

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

def iterative_gps(m, iter, min_degree = False):
    plot_count = 0

    dimension = len(m)
    p = peripherals.Peripherals(0, 0, 0)

    root = ( util.get_min_degree_node(m)
            if min_degree
            else random.randint(0, dimension - 1) )

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


def iterative_gps_test(m, diameter, min_degree = False):
    plot_count = 0

    dimension = len(m)
    p = peripherals.Peripherals(0, 0, 0)

    root = ( util.get_min_degree_node(m)
            if min_degree
            else random.randint(0, dimension - 1) )

    explore = [root]
    checked = [False for i in range(dimension)]
    iter = 0
    while explore:
        #print explore

        v = explore.pop(0)
        rls_v = rls.buildRLS(m, v)
        checked[v] = True
        
        #print rls_v.levelsArray
        
        for w in rls_v.lastLevel():
            if checked[w] == False:
                explore.append(w)

        p_v = peripherals.Peripherals(v, rls_v.lastLevel()[0], rls_v.numLevels() - 1)

        iter = iter + 1

        if p_v.diameter > p.diameter:
            p.copy(p_v)

        if int(p.diameter) == int(diameter):
            print 'min num iter =', iter
            return p
        

        #plot.plot_graph(m, str(plot_count), checked)
        #plot_count = plot_count + 1

    #checked[p.b] = True
    #plot.plot_graph(m, str(plot_count), checked)
    return p


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print 'Usage: python gps.py <matrix> <diameter>'
        sys.exit (1)

    filename = sys.argv[1]
    print 'importing ', filename
    mat = mat_loader.load(filename)

    diameter = sys.argv[2]
    print 'orig diam = ', diameter

    print ' '
    start_time = time.time()

    ''' Execution '''
    p = iterative_gps_test(mat, diameter, min_degree=True)

    print ' '
    print 'rls iteractions:', rls.buildRLS_count
    print 'rls canceled:', rls.buildRLS_canceled
    print ' '

    print 'Tempo: {}s'.format(time.time() - start_time)
    print 'Pseudo-perifericos: {a} e {b}, Diametro: {diameter}'.format(
        a=p.a, b=p.b, diameter=p.diameter)