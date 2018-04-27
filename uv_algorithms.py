'''
    Author: Eduardo Motta de Oliveira
'''
import mat_loader
import rls
import peripherals
import random
import util


def build_uv_rls(m, min_degree = False):
    dimension = len(m)
    checked = [False for i in range(dimension)]

    u = ( get_min_degree_node(m)
            if min_degree
            else random.randint(0, dimension - 1) )

    rls_u = rls.buildRLS(m, u)
    #checked[u] = True
    #print rls_u.levelsArray

    v = rls_u.lastLevel()[0]
    rls_v = rls.buildRLS(m, v)
    #print rls_v.levelsArray

    return u, v, rls_u, rls_v, dimension





'''(u,v) Algorithms'''
def nonReversible_uv(m, min_degree = False, min_width = False):

    u, v, rls_u, rls_v, dimension = build_uv_rls(m, min_degree)

    # R(u,v)
    reversible_set = util.get_reversible_set(rls_u.levelsArray, 
                                            rls_v.levelsArray)
    #print reversible_set

    # V - R(u,v)
    V = set(range(dimension))
    for r in reversible_set:
        for i in r:
            V.remove(i)
    
    #print V
    
    return util.grow_set_and_check_peripherals(m, V, min_width)



