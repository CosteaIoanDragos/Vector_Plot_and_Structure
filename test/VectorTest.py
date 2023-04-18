import unittest
from domain.MyVector import MyVector

class MyTestCase(unittest.TestCase):
    def setUp(self) :
        self.vector1=MyVector("val","r",1,[2,4,5])
        self.vector2=MyVector("v","r",2,[1,2,3])
    def test_create(self):
        self.assertEqual(self.vector1.get_name_id(),"val")
        self.assertEqual(self.vector1.get_colour(),"r")
        self.assertEqual(self.vector1.get_type(),1)
        self.assertEqual(self.vector1.get_values(),[2,4,5])
        self.assertEqual(str(self.vector1),"vector(val) of color: r of type: 1 with values in [2, 4, 5]")
        #test errors
        self.assertRaises(ValueError,MyVector,[2,4],"r",1,[2,4,5])
        self.assertRaises(ValueError,MyVector,"val","z",1,[2,4,5])
        self.assertRaises(ValueError, MyVector, "val","r",0,[2,4,5])
        self.assertRaises(ValueError, MyVector, "val","r",1,"[2,4,5]")
        #test setters
        self.assertRaises(ValueError,self.vector1.set_name_id,[2,4])
        self.assertRaises(ValueError,self.vector1.set_colour,"z")
        self.assertRaises(ValueError,self.vector1.set_type,0)
        self.assertRaises(ValueError,self.vector1.set_values,"[2,4,5]")
        #chack if name id doesnt change
        self.vector1.set_colour("g")
        self.assertEqual(self.vector1.get_colour(),"g")
        self.assertEqual(self.vector1.get_name_id(),"val")
        self.vector1.set_values([1,2,3])
        self.assertEqual(self.vector1.get_name_id(), "val")
        self.assertEqual(self.vector1.get_values(),[1,2,3])
        self.vector1.set_type(3)
        self.assertEqual(self.vector1.get_name_id(), "val")
        self.assertEqual(self.vector1.get_type(),3)
    def test_scalar_op(self):
        self.vector1.addScalar(2)
        self.assertEqual(self.vector1.get_values(),[4,6,7])
        self.vector1.addScalar(0)
        self.assertEqual(self.vector1.get_values(), [4, 6, 7])
        self.vector1.addScalar(10)
        self.assertEqual(self.vector1.get_values(), [14, 16, 17])

    def test_vector_op(self):
        self.vector1.addVectors(self.vector2)
        self.assertEqual(self.vector1.get_values(),[3,6,8])
        self.vector1.substractVectors(self.vector2)
        self.assertEqual(self.vector1.get_values(),[2,4,5])

        self.assertEqual(self.vector1.multiplyVectors(self.vector2),25)
    def test_reduction_op(self):
        self.assertEqual(self.vector1.sumOfVector(),11)
        self.assertEqual(self.vector1.productOfVector(),40)
        self.assertEqual(self.vector1.minOfVector(),2)
        self.assertEqual(self.vector1.maxOfVector(),5)
        self.assertEqual(int(self.vector1.avarageOfVector()),3)

if __name__ == '__main__':
    unittest.main()
