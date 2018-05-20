import mat_loader
import gps
import arany
import uv_algorithms
import rls
import peripherals
import time
import sys

def run_method(mat, id):
    if id == 0:
        #return peripherals.exaustive_peripheral_search(mat)
        return peripherals.parallel_exaustive_peripheral_search(mat)
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

'''
    
'''
mat_names = [
    'mat.mtx',
    'sample.mtx',
    'bcspwr01.mtx',
    'can24.mtx',
    'bcspwr02.mtx',
    'fidap001.mtx',
    'rail_5177.mtx',
    'dw8192.mtx',
    'fidapm08.mtx',
    'aft01.mtx'
]


if len(sys.argv) < 2:
    print 'Usage: python test.py 1'
    sys.exit (1)

methods = ['Exaustive','GPS','Arany','Non-Reversible(u,v)',
            'No Consequent(u)','No Consequent(u,v)','MaximumSwing(u,v)']
method_id = int(sys.argv[1])
print ''
print 'Running: {}'.format(methods[method_id])

for mat_name in mat_names:
    filename = 'matrices/' + mat_name
    mat = mat_loader.load(filename)

    start_time = time.time()

    ''' Execution '''
    p = run_method(mat, method_id)
   
    total_time = time.time() - start_time
    print '{},\t{}, \t{}'.format(mat_name, total_time, p.diameter)


    #print 't: {t} s,\t per: {a} e {b},\t diam: {diameter}'.format(
    #    t=(time.time() - start_time), a=p.a, b=p.b, diameter=p.diameter)

    #print ' '
