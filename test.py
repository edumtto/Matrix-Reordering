import mat_loader
import gps
import rls
import peripherals
import time

mat_names = [
    'mat.mtx',
    'matrix_example.mtx',
    'matrix_example_ilup.mtx',
    'sample.mtx',
    'bcspwr01.mtx',
    'fidap001.mtx'
]
for mat_name in mat_names:
    filename = 'matrices/' + mat_name
    print 'importing ', filename
    mat = mat_loader.load(filename)

    start_time = time.time()
    p = peripherals.findPeripherals(mat)
    print 't: {t} s,\t per: {a} e {b},\t diam: {diameter}'.format(
        t=(time.time() - start_time), a=p.a, b=p.b, diameter=p.diameter)

    start_time = time.time()
    p = gps.gps(mat)
    print 't: {t} s,\t per: {a} e {b},\t diam: {diameter}'.format(
        t=(time.time() - start_time), a=p.a, b=p.b, diameter=p.diameter)

    print ' '
