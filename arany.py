'''
    Author: Eduardo Motta de Oliveira
'''
import mat_loader
import rls
import peripherals
import random
import util

'''Original Arany'''
def arany_method(m, min_degree = False, min_width = False):

    dimension = len(m)
    checked = [False for i in range(dimension)]

    u = ( util.get_min_degree_node(m)
            if min_degree
            else random.randint(0, dimension - 1) )

    rls_u = rls.buildRLS(m, u)
    #checked[u] = True
    #print rls_u.levelsArray

    v = rls_u.lastLevel()[0]
    rls_v = rls.buildRLS(m, v)
    #print rls_v.levelsArray

    reversible_set = util.get_reversible_set(rls_u.levelsArray, 
                                      rls_v.levelsArray)
    #print reversible_set

    m_uv = reversible_set[len(reversible_set) // 2]
    #print m_uv

    a = m_uv.pop()
    rls_a = rls.buildRLS(m, a)

    last_level = rls_a.lastLevel()
    return util.grow_set_and_check_peripherals(m, last_level, min_width)