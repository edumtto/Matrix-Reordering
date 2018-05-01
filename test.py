import mat_loader
import gps
import arany
import uv_algorithms
import rls
import peripherals
import time

mat_names = [
    'mat.mtx',
    'sample.mtx',
    'bcspwr01.mtx',
    'can24.mtx',
    'bcspwr02.mtx',
    'fidap001.mtx',
    'rail_5177.mtx',
    'dw8192.mtx',
    'fidapm08.mtx'
]
for mat_name in mat_names:
    filename = 'matrices/' + mat_name
    print 'importing ', filename
    mat = mat_loader.load(filename)
    
    start_time = time.time()
    #p = gps.iterative_gps(mat, 15, min_degree=True)
    #p = arany.arany_method(mat, min_degree=True, min_width=True)
    #p = uv_algorithms.nonReversible_uv(mat, min_degree=True, min_width=True)
    #p = uv_algorithms.noConsequent_uv(mat, min_degree=True, min_width=True)
    p = uv_algorithms.noConsequent_u(mat, min_degree=True, min_width=True)
    #p = uv_algorithms.maximumSwing_uv(mat, min_degree=True, min_width=True)
    print 't: {t} s,\t per: {a} e {b},\t diam: {diameter}'.format(
        t=(time.time() - start_time), a=p.a, b=p.b, diameter=p.diameter)

    print ' '
