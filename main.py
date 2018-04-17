'''
    Author: Eduardo Motta de Oliveira
'''
import mat_loader
import rls
import peripherals
import gps
import sys
import plot

if len(sys.argv) < 2:
    print 'Usage: python main.py ./matrices/mat.mtx'
    sys.exit (1)

filename = sys.argv[1]
print 'importing ', filename
mat = mat_loader.load(filename)

visited = [False for i in range(len(mat))]
visited[3] = True
visited[0] = True

plot.plot_graph(mat, filename, visited)
'''
plot.show_graph_pyplot(mat)
'''

print ' '
p = gps.iterative_gps(mat, 10)
print 'Pseudo-perifericos: {a} e {b}, Diametro: {diameter}'.format(
    a=p.a, b=p.b, diameter=p.diameter)