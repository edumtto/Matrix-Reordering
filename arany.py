'''
    Author: Eduardo Motta de Oliveira
'''
import graph
import mat_loader
import rls
import peripherals
import random
import util

def build_uv_rls(m, min_degree = False, no_conseq = False):
    dimension = m.get_dimension()
    checked = [False for i in range(dimension)]

    u = ( util.get_min_degree_node(m)
            if min_degree
            else random.randint(0, dimension - 1) )

    rls_u = rls.buildRLS(m, u, max_w=0, no_conseq=no_conseq)

    v = util.min_degree_node_from_set(m, rls_u.lastLevel())
    rls_v = rls.buildRLS(m, v, max_w=0, no_conseq=no_conseq)

    return u, v, rls_u, rls_v, dimension
    
'''Original Arany'''
def arany_method(m, min_degree = False, min_width = False):

    u, v, rls_u, rls_v, dimension = build_uv_rls(m, min_degree,
                                                 no_conseq=False)

    reversible_set = util.get_reversible_set(rls_u.levelsArray, 
                                      rls_v.levelsArray)

    m_uv = reversible_set[len(reversible_set) // 2]
    #print m_uv

    a = m_uv.pop()
    rls_a = rls.buildRLS(m, a)

    last_level = rls_a.lastLevel()
    
    p = util.return_most_peripheral(u, rls_u, v, rls_v)
    return util.grow_set_and_check_peripherals(m, last_level,
                                                min_width=min_width,
                                                initial_p=p)