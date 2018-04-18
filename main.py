'''
    Author: Eduardo Motta de Oliveira
'''
import mat_loader
import rls
import peripherals
import gps
import arany
import sys
import plot
import time

def print_fill_in(m):
    range_dim = range(len(mat))
    for i in range_dim:
        print '|',
        for j in range_dim:
            print '{}'.format('x' if mat[i][j] != 0 else ' '),
        print '|'


if len(sys.argv) < 2:
    print 'Usage: python main.py ./matrices/mat.mtx'
    sys.exit (1)

filename = sys.argv[1]
print 'importing ', filename
mat = mat_loader.load(filename)

#plot.plot_graph(mat, filename)
#plot.show_graph_pyplot(mat)
#print_fill_in(mat)  

print ' '
start_time = time.time()

#p = gps.iterative_gps(mat, 50)
p = arany.arany_method(mat)

print 'Pseudo-perifericos: {a} e {b}, Diametro: {diameter}'.format(
    a=p.a, b=p.b, diameter=p.diameter)
print 'Tempo: {}s'.format(time.time() - start_time)