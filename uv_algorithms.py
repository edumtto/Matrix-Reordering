'''
    Author: Eduardo Motta de Oliveira
'''
import mat_loader
import rls
import peripherals
import random
import util

def build_uv_rls(m, min_degree = False, no_conseq = False):
    dimension = len(m)
    checked = [False for i in range(dimension)]

    u = ( util.get_min_degree_node(m)
            if min_degree
            else random.randint(0, dimension - 1) )

    rls_u = rls.buildRLS(m, u, max_w=0, no_conseq=no_conseq)

    v = util.min_degree_node_from_set(m, rls_u.lastLevel())
    rls_v = rls.buildRLS(m, v, max_w=0, no_conseq=no_conseq)

    return u, v, rls_u, rls_v, dimension


'''Non-Reversible (u,v)'''
def nonReversible_uv(m, min_degree = False, min_width = False):

    u, v, rls_u, rls_v, dimension = build_uv_rls(m, min_degree)

    reversible_set = util.get_reversible_set(rls_u.levelsArray, 
                                            rls_v.levelsArray)

    ''' V - R(u,v) '''
    V = set(range(dimension))
    for r in reversible_set:
        for i in r:
            V.remove(i)
    
    #print V
    p = util.return_most_peripheral(u, rls_u, v, rls_v)
    return util.grow_set_and_check_peripherals(m, V,
                                                min_width=min_width,
                                                initial_p=p)

'''No Consequent (u,v)'''
def noConsequent_uv(m, min_degree = False, min_width = False):

    u, v, rls_u, rls_v, dimension = build_uv_rls(m, min_degree,
                                                 no_conseq=True)
    ''' Q(u) U Q(v) - {u, v} '''
    no_conseq_set = rls_u.noConsequents.union(rls_v.noConsequents)

    if u in no_conseq_set:
        no_conseq_set.remove(u)
    #no_conseq_set.remove(v)   
    
    p = util.return_most_peripheral(u, rls_u, v, rls_v)
    return util.grow_set_and_check_peripherals(m, no_conseq_set,
                                                min_width=min_width,
                                                initial_p=p)


'''No Consequent (u)'''
def noConsequent_u(m, min_degree = False, min_width = False):

    u = ( util.get_min_degree_node(m)
            if min_degree
            else random.randint(0, dimension - 1) )

    rls_u = rls.buildRLS(m, u, max_w=0, no_conseq=True)
    no_conseq_u = rls_u.noConsequents

    p = peripherals.Peripherals(u, rls_u.lastLevel()[0], rls_u.numLevels() - 1)
    return util.grow_set_and_check_peripherals(m, no_conseq_u, 
                                                min_width=min_width,
                                                initial_p=p)


'''Maximum Swing (u,v)'''
def maximumSwing_uv(m, min_degree = False, min_width = False):

    u, v, rls_u, rls_v, dimension = build_uv_rls(m, min_degree,
                                                 no_conseq=False)

    reversible_set = util.get_reversible_set(rls_u.levelsArray, 
                                            rls_v.levelsArray)

    nodes_swing = [0 for i in range(dimension)]
    for l in reversible_set:
        for w in l:
            ''' Node will not be checked'''
            nodes_swing[w] = -1 

    max_swing = 0
    h_u = rls_u.numLevels()

    for i in range(1, h_u):
        for w in rls_u.getLevel(i):
            if nodes_swing[w] != -1:
                swing_w = i + get_node_level(w, rls_v)
                #print "swing of {}: {}".format(w, swing_w)
                nodes_swing[w] = swing_w
                if swing_w > max_swing:
                    max_swing = swing_w

    '''print "u, v = {}, {}".format(u, v)
    print reversible_set
    print nodes_swing
    print "max swing =", max_swing
    '''

    max_swing_set = []
    for i in range(1, dimension):
        #print "{} == {} ?".format(nodes_swing[i], max_swing)
        if nodes_swing[i] == max_swing:
            max_swing_set.append(i)

    print "max swing set =", max_swing_set
    p = util.return_most_peripheral(u, rls_u, v, rls_v)
    return util.grow_set_and_check_peripherals(m, max_swing_set,
                                                min_width=min_width,
                                                initial_p=p)


def get_node_level(n, rls):
    h = rls.numLevels()

    for i in range(h):
        if n in rls.getLevel(i):
            #print "level of {} in v: {}".format(n, i)
            return i