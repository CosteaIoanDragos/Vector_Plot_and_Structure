import unittest
from infrastructure.VectorRepository import VectorRepoistory
from domain.MyVector import MyVector

class MyTestCase(unittest.TestCase):
    def setUp(self) :
        self.repo=VectorRepoistory()
        self.vector1 = MyVector("val", "r", 1, [2, 4, 5])
        self.vector2 = MyVector("v", "r", 2, [1, 2, 3])
        self.emptyrepo=VectorRepoistory()
        self.repo.addVector(self.vector1)
        self.repo.addVector(self.vector2)
    def test_create(self):
        self.assertEqual(len(self.repo),2)
        self.assertEqual(str(self.repo.getVectorAtIndex(0)),"vector(val) of color: r of type: 1 with values in [2, 4, 5]")
        self.assertEqual(str(self.repo.getVectorAtIndex(1)),"vector(v) of color: r of type: 2 with values in [1, 2, 3]")
        self.assertEqual(len(self.emptyrepo),0)
        self.assertEqual(str(self.emptyrepo),"")
        #verifies if it add the same vector
        self.assertRaises(ValueError,self.repo.addVector,self.vector1)

    def test_addVector(self):
        self.assertEqual(len(self.emptyrepo), 0)
        self.emptyrepo.addVector(self.vector1)
        self.assertEqual(len(self.emptyrepo),1)
        self.emptyrepo.addVector(self.vector2)
        self.assertEqual(len(self.emptyrepo),2)
        self.assertRaises(ValueError,self.repo.addVector,self.vector1)

    def test_len(self):
        self.assertEqual(len(self.repo),2)
        self.assertEqual(len(self.emptyrepo), 0)
        self.emptyrepo.addVector(self.vector1)
        self.assertEqual(len(self.emptyrepo),1)
    def test_sumOfElementsWithColor(self):
        self.assertEqual(self.repo.sumOfElementWithColor("r"),17)
        self.assertEqual(self.repo.sumOfElementWithColor("y"),0)
        self.assertEqual(self.emptyrepo.sumOfElementWithColor("r"),0)
    def test_delAllVectors(self):
        self.assertEqual(len(self.repo),2)
        self.repo.delAllVectors()
        self.assertEqual(len(self.repo),0)
        self.assertEqual(len(self.emptyrepo), 0)
        self.emptyrepo.delAllVectors()
        self.assertEqual(len(self.emptyrepo),0)
    def test_UpdateColorAtType(self):
        self.assertEqual(self.repo.getVectorAtIndex(0).get_colour(),"r")
        self.repo.updateColorAtType(1,"y")
        self.assertEqual(self.repo.getVectorAtIndex(0).get_colour(),"y")

        self.assertEqual(self.repo.getVectorAtIndex(1).get_colour(),"r")
        self.repo.updateColorAtType(2, "b")
        self.assertEqual(self.repo.getVectorAtIndex(1).get_colour(),"b")
        self.repo.updateColorAtType(2,"r")
        self.assertEqual(self.repo.getVectorAtIndex(1).get_colour(),"r")
    def test_getVectorAtIndex(self):
        self.assertEqual(str(self.repo.getVectorAtIndex(0)),"vector(val) of color: r of type: 1 with values in [2, 4, 5]")
        self.assertEqual(str(self.repo.getVectorAtIndex(1)),"vector(v) of color: r of type: 2 with values in [1, 2, 3]")
#        self.assertEqual(str(self.emptyrepo.getVectorAtIndex(0)),"None")
        self.assertRaises(ValueError,self.repo.getVectorAtIndex,-1)
    def test_updateAtIndex(self):
        self.assertEqual(str(self.repo.getVectorAtIndex(0)),"vector(val) of color: r of type: 1 with values in [2, 4, 5]")
        self.assertEqual(str(self.repo.getVectorAtIndex(1)),"vector(v) of color: r of type: 2 with values in [1, 2, 3]")
        self.repo.updateAtIndex(0,"1","b",3,[0,0,0])
        self.repo.updateAtIndex(0, "1", "b", 3, [0, 0, 0])
        self.assertEqual(str(self.repo.getVectorAtIndex(0)),"vector(1) of color: b of type: 3 with values in [0, 0, 0]")
        self.assertEqual(str(self.repo.getVectorAtIndex(0)),"vector(1) of color: b of type: 3 with values in [0, 0, 0]")
        self.assertRaises(ValueError,self.emptyrepo.updateAtIndex,0,"i","b",3,[0,0,0])
    def test_updateAtNameId(self):
        self.assertEqual(str(self.repo.getVectorAtIndex(0)),"vector(val) of color: r of type: 1 with values in [2, 4, 5]")
        self.assertEqual(str(self.repo.getVectorAtIndex(1)),"vector(v) of color: r of type: 2 with values in [1, 2, 3]")
        self.repo.updateAtNameId("val","b",3,[0,0,0])
        self.repo.updateAtNameId("v","b",3,[0,0,0])
        self.assertEqual(str(self.repo.getVectorAtIndex(0)),"vector(val) of color: b of type: 3 with values in [0, 0, 0]")
        self.assertEqual(str(self.repo.getVectorAtIndex(1)),"vector(v) of color: b of type: 3 with values in [0, 0, 0]")
        self.assertRaises(ValueError,self.emptyrepo.updateAtNameId,"ion","b",3,[0,0,0],)
    def test_delByIndex(self):
        self.assertEqual(str(self.repo.getVectorAtIndex(0)),"vector(val) of color: r of type: 1 with values in [2, 4, 5]")
        self.repo.delByIndex(0)
        self.assertEqual(str(self.repo.getVectorAtIndex(0)),"vector(v) of color: r of type: 2 with values in [1, 2, 3]")
        self.repo.delByIndex(0)
        self.assertEqual(len(self.repo),0)
        self.assertRaises(ValueError,self.emptyrepo.delByIndex,-1)
    def test_delByNameId(self):
        self.assertEqual(str(self.repo.getVectorAtIndex(0)),"vector(val) of color: r of type: 1 with values in [2, 4, 5]")
        self.repo.delByNameId("val")
        self.assertEqual(str(self.repo.getVectorAtIndex(0)),"vector(v) of color: r of type: 2 with values in [1, 2, 3]")
        self.repo.delByNameId("v")
        self.assertEqual(len(self.repo),0)
        self.assertRaises(ValueError,self.emptyrepo.delByNameId,"vld")

if __name__ == '__main__':
    unittest.main()
