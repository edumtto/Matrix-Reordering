'''
    Author: Eduardo Motta de Oliveira
'''
import mat_loader
import rls
import peripherals
import gps
import arany
import uv_algorithms
import sys
import plot
import time

'''
def print_fill_in(m):
    range_dim = range(len(mat))
    for i in range_dim:
        print '|',
        for j in range_dim:
            print '{}'.format('x' if mat[i][j] != 0 else ' '),
        print '|'
'''

def run_method(mat, id):
    if id == 0:
        return peripherals.exaustive_peripheral_search(mat, thread = 1)
        #return peripherals.parallel_exaustive_peripheral_search(mat)
    if id == 1:
        return gps.iterative_gps(mat, 3, min_degree=True)
    if id == 2:
        return arany.arany_method(mat, min_degree=True, min_width=True)
    if id == 3: 
        return uv_algorithms.nonReversible_uv(mat, min_degree=True, min_width=True)
    if id == 4:
        return uv_algorithms.noConsequent_u(mat, min_degree=True, min_width=True)
    if id == 5:
        return uv_algorithms.noConsequent_uv(mat, min_degree=True, min_width=True)
    if id == 6:
        return uv_algorithms.maximumSwing_uv(mat, min_degree=True, min_width=True)
    
    return None


if len(sys.argv) < 3:
    print 'Usage: python main.py ./matrices/mat.mtx 1'
    sys.exit (1)

filename = sys.argv[1]
print 'importing ', filename
mat = mat_loader.load(filename)

methods = ['Exaustive','GPS','Arany','Non-Reversible(u,v)',
            'No Consequent(u)','No Consequent(u,v)','MaximumSwing(u,v)']
method_id = int(sys.argv[2])
print ''
print 'Running: {}'.format(methods[method_id])

''' Plots '''
#plot.plot_graph(mat, filename)
#plot.show_graph_pyplot(mat)
#print_fill_in(mat)  

print ' '
start_time = time.time()

''' Execution '''
p = run_method(mat, method_id)

print ' '
print 'rls iteractions:', rls.buildRLS_count
print 'rls canceled:', rls.buildRLS_canceled
print ' '

print 'Tempo: {}s'.format(time.time() - start_time)
print 'Pseudo-perifericos: {a} e {b}, Diametro: {diameter}'.format(
    a=p.a, b=p.b, diameter=p.diameter)

