'''
    Author: Eduardo Motta de Oliveira
'''
import mat_loader

buildRLS_count = 0
buildRLS_canceled = 0

class RLS:

    def __init__(self):
        self.levelsArray = []

    def addLevel(self, array):
        self.levelsArray.append(array)  


    '''def isPresent(self, vertex):
        for l in self.levelsArray:
            if vertex in l:
                return True
        return False
    '''
    def lastLevel(self):
        return self.levelsArray[-1]

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

def buildRLS(m, root, max_w = 0):
    global buildRLS_count, buildRLS_canceled
    buildRLS_count += 1

    limit_width = (max_w != 0)

    levels = RLS()
    visited = [False for j in range(len(m))]
    l = [root]

    while (l):
        if limit_width:
            if len(l) >= max_w:
                buildRLS_canceled += 1
                return None

        levels.addLevel(l)
        for x in l:
            visited[x] = True
        l = []

        for v in levels.lastLevel():
            adj = getNotVisitedAdjacents(m, v, visited)
            
            for a in adj:
                visited[a] = True
                l.append(a)

    return levels

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
    