import unittest
import peripheral

class TestPeripheral(unittest.TestCase):

    def setUp(self):
        print 'setUp'
        self.m0 = [
                [0,1,2,0,0,0],
                [2,0,0,5,0,0],
                [1,0,0,0,2,0],
                [0,7,0,0,0,0],
                [0,0,3,0,0,0],
                [0,0,0,0,0,0]
            ]
        self.visited_m0 = [False for i in range(6)]
    
    def tearDown(self):
        print 'tearDown'

    def test_getNotVisitedAdjacents(self):
        print 'test_getNotVisitedAdjacents'
        result = peripheral.getNotVisitedAdjacents(self.m0,2,self.visited_m0)
        self.assertEqual(result, [0,4])
        result = peripheral.getNotVisitedAdjacents(self.m0,5,self.visited_m0)
        self.assertEqual(result, [])
        self.visited_m0[0] = True
        result = peripheral.getNotVisitedAdjacents(self.m0,2,self.visited_m0)
        self.assertEqual(result, [4])

    def test_buildRLS(self):
        print 'test_buildRLS'
        result = peripheral.buildRLS(self.m0,0)
        self.assertEqual(result.levelsArray, [[0],[1,2],[3,4]])
        result = peripheral.buildRLS(self.m0,5)
        self.assertEqual(result.levelsArray, [[5]])

if __name__ == "__main__":
    unittest.main()