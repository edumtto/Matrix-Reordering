'''
    Author: Eduardo Motta de Oliveira
'''
import mat_loader

buildRLS_count = 0
buildRLS_canceled = 0

class RLS:

    def __init__(self):
        self.levelsArray = []
        self.noConsequents = set()

    def addLevel(self, array):
        self.levelsArray.append(array)  

    def addNonConsequent(self, n):
        self.noConsequents.add(n)

    def removeNonConsequent(self, n):
        self.noConsequents.discard(n)

    '''def isPresent(self, vertex):
        for l in self.levelsArray:
            if vertex in l:
                return True
        return False
    '''
    def lastLevel(self):
        return self.levelsArray[-1]

    def getLevel(self, i):
        return self.levelsArray[i]

    def numLevels(self):
        return len(self.levelsArray)

    def width(self):
        max_w = 0
        for l in self.levelsArray:
            w_level = len(l)
            if w_level > max_w:
                max_w = w_level
        return max_w

    def printRLS (self):
        print self.levelsArray

def getNotVisitedAdjacents(m, vertex, visited):
    adj = []
    tam = len(m[0])
    for i in range(tam):
        val = m[vertex][i]
        
        if val != 0:
            if visited[i] == False:
                adj.append(i)
    return adj

def buildRLS(m, root, max_w = 0, no_conseq = False):
    global buildRLS_count, buildRLS_canceled
    buildRLS_count += 1

    limit_width = (max_w != 0)

    rls = RLS()
    visited = [False for j in range(len(m))]
    l = [root]

    while (l):
        if limit_width:
            if len(l) >= max_w:
                buildRLS_canceled += 1
                return None

        rls.addLevel(l)
        for x in l:
            visited[x] = True

        adj_set =set()
        for v in rls.lastLevel():
            adj = getNotVisitedAdjacents(m, v, visited)
            if no_conseq and not adj:
                rls.addNonConsequent(v)
            for a in adj:
                adj_set.add(a)

        for a in adj_set:
            visited[a] = True
        l = list(adj_set)

    if no_conseq:
        for u in rls.lastLevel():
                rls.removeNonConsequent(u)
    
    return rls

def eccentricity (m, root):
    rls = buildRLS(m,root)
    '''
    print 'Ecc: ' + str(rls.numLevels() - 1) + '  ' + str(rls.levelsArray)
    '''
    return rls.numLevels() - 1

def diameter (m):   
    dimension = len(m)
    maxEcc = 0
    for i in range(dimension):
        ecc = eccentricity(m, i)
        if ecc > maxEcc:
            maxEcc = ecc
    return maxEcc

'''Main'''
if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    print 'importing ', filename
    mat = mat_loader.load(filename)

    print ' '
    d = diameter(mat)
    print 'Diameter: ', d
    