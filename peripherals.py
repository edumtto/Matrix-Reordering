import rls
import mat_loader
import graph
import multiprocessing as mp
import sys

class Peripherals:

    def __init__(self, a, b, diameter):
        self.a = a
        self.b = b
        self.diameter = diameter

    def copy(self, p):
        self.a = p.a
        self.b = p.b
        self.diameter = p.diameter

    def toStr(self):
        return 'Peripherals: ({},{}) Diameter = {}'.format(self.a,self.b, self.diameter)


def exaustive_peripheral_search(m, fromV = None, toV = None, output = None, thread = None):
    dimension = m.get_dimension()

    begin = fromV if fromV else 0
    end = toV if toV else dimension

    if thread:
        print "Thread {} range({},{})".format(thread, begin,end)

    V = range(begin, end)
    V_size = end - begin

    iter = 0
    p = Peripherals(0, 0, 0)

    for v in V:
        rls_v = rls.buildRLS(m, v)
        '''
        print rls_v.levelsArray
        '''
        p_v = Peripherals(v, rls_v.lastLevel()[0], rls_v.numLevels() - 1)
        if p_v.diameter > p.diameter:
            p.copy(p_v)
        
        iter += 1
        percentage = 100 * float(iter)/V_size
        
        if thread:
            if iter % 100 == 0:
                print 'Thread {}: node {} checked - {:0.2f}%'.format(thread,v,percentage)
        #else:
        #    sys.stdout.write("\r{} / {} - {:0.2f}%".format(v,V_size,percentage))
        #    sys.stdout.flush()

    #print p.toStr()
    if output:
        output.put(p)
    return p

def parallel_exaustive_peripheral_search(m):

    output = mp.Queue()
    processes = []
    dimension = len(m)
    set_nodes = dimension/4
    print 'set nodes =', set_nodes

    processes.append(mp.Process(target=exaustive_peripheral_search,
                                 args=(m, 0, set_nodes, output, 1)))
    processes.append(mp.Process(target=exaustive_peripheral_search,
                                 args=(m, set_nodes, set_nodes*2, output, 2)))
    processes.append(mp.Process(target=exaustive_peripheral_search,
                                 args=(m, set_nodes*2, set_nodes*3, output, 3)))
    processes.append(mp.Process(target=exaustive_peripheral_search,
                                 args=(m, set_nodes*3, dimension, output, 4)))
    
    for p in processes:
        p.start()

    for p in processes:
        p.join()

    # Get process results from the output queue
    results = [output.get() for p in processes]
    print [p.toStr() for p in results]

    return get_most_peripheral(results)


def get_most_peripheral(periph_ls):
    p = Peripherals(0, 0, 0)

    for a in periph_ls:
        if a.diameter > p.diameter:
            p.copy(a)

    return p


'''Main'''
if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    print 'importing ', filename
    mat = mat_loader.load(filename)
    '''
    mat_loader.show_graph_with_labels(mat)
    '''
    print ' '
    p = exaustive_peripheral_search(mat)
    print 'Pseudo-perifericos: {a} e {b}, Diametro: {diameter}'.format(
        a=p.a, b=p.b, diameter=p.diameter)