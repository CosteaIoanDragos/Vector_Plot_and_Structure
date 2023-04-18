import numpy

class MyVector:
    def __init__(self,name_id,colour,typ,values):
        """
        Creates object My Vector
        :param name_id: int str
        :param colour: str
        :param typ: int
        :param values: list
        """
        if type(name_id)==str or type(name_id)==int:
            self.__name_id=name_id
        else :
            raise ValueError("It's not a string or int")
        if colour in ["r","g","b","y"]:
            self.__colour=colour
        else :
            raise ValueError("The colour is not good")
        if  type(typ)==int and typ>=1 :
            self.__typ=typ
        else :
            raise ValueError("It should be greater or equal to 1")
        copyValues =[]
        if type(values)==list:
            self.__values=values
            copyValues=self.__values.copy()
        else:
            raise ValueError("Give me a list")

    def __str__(self):
        """
        create a string reprezentation
        :return: 
        """
        return "vector("+str(self.__name_id)+") of color: "+self.__colour+" of type: "+str(self.__typ) +" with values in "+str(self.__values)
    def get_name_id(self):
        """
        gets the name id
        :param self:
        :return:
        """
        return self.__name_id
    def get_colour(self):
        """
        gets the color
        :param self:
        :return:
        """
        return self.__colour
    def get_type(self):
        """
        gets the type
        :param self:
        :return:
        """

        return self.__typ
    def get_values(self):
        """
        gets the list
        :param self:
        :return:
        """
        copyValues=self.__values.copy()
        return copyValues
    def set_name_id(self,name_id):
        """
        sets the name id
        :param self:
        :param name_id:
        :return:
        """
        if type(name_id) == str or type(name_id) == int:
            self.__name_id = name_id
        else:
            raise ValueError("It's not a string or int")
    def set_colour(self,colour):
        """
        sets the color
        :param self:
        :param colour:
        :return:
        """
        if colour in ["r","g","b","y"]:
            self.__colour=colour
        else :
            raise ValueError("The colour is not good")
    def set_type(self,typ):
        """
        sets the type
        :param self:
        :param typ:
        :return:
        """
        if  type(typ)==int and typ>=1 :
            self.__typ=typ
        else :
            raise ValueError("It should be greater or equal to 1")
    def set_values(self,values):
        """
        sets the values
        :param self:
        :param values:
        :return:
        """

        if type(values) == list:
            self.__values = values
            copyValues = self.__values.copy()
        else:
            raise ValueError("Give me a list")
    def addScalar(self,scalar):
        """adds a scalar to a vector"""
        a=numpy.array(self.__values)
        a=a+scalar
        a=a.tolist()
        self.set_values(a)
    def addVectors(self, other):
        """
        adds a vector to another
        :param self:
        :param other:
        :return:
        """
        if len(self.__values)!=0 and len(other.__values)==len(self.__values):
            res=[self.__values[x]+other.__values[x] for x in range(len(self.__values))]
        else:
            raise ValueError ("One vector is null or they are not equal")
        self.set_values(res)
    def substractVectors(self,other):
        """
        substracts a vector from another
        :param self:
        :param other:
        :return:
        """
        if len(self.__values)!=0 and len(other.__values)==len(self.__values):
            res=[self.__values[x]-other.__values[x] for x in range(len(self.__values))]
        else:
            raise ValueError ("One vector is null or they are not equal")
        self.set_values(res)
    def multiplyVectors(self,other):
        """
        multiplyes two vectors and returns the sum
        :param self:
        :param other:
        :return:
        """
        if len(self.__values)!=0 and len(other.__values)==len(self.__values):
            res = [self.__values[x] * other.__values[x] for x in range(len(self.__values))]
        else:
            raise ValueError("One vector is null or they are not equal")
        return sum(res)
    def sumOfVector(self):
        """
        sums the elements in a vector
        :param self:
        :return:
        """
        if len(self.__values)!=0:
            return sum(self.__values)
        else:
            return ValueError("Vector Null")
    def productOfVector(self):
        """
        multiplyes the elements in a vector

        :param self:
        :return:
        """
        if len(self.__values)!=0:
            return numpy.prod(self.__values)
        else:
            return ValueError("Vector Null")

    def minOfVector(self):
        """
        returns minimum of a vector
        :param self:
        :return:
        """
        if len(self.__values)!=0:
            return min(self.__values)
        else:
            return ValueError("Vector Null")
    def maxOfVector(self):
        """
        returns the max of a vector
        :param self:
        :return:
        """
        if len(self.__values)!=0:
            return max(self.__values)
        else:
            return ValueError("Vector Null")
    def avarageOfVector(self):
        """
        calculates the avaraage of the elements in vector
        :param self:
        :return:
        """
        s=sum(self.__values)
        d=len(self.__values)
        return s/d
if __name__=="__main__":
    f=MyVector("val","r",1,[1])
    g=MyVector("v","r",2,[1,2,3])
    f.set_name_id("1")
    print(f)
    print(g)
    f.addScalar(2)
    print(f)
    f.addVectors(g)
    print (f)
    print(f.multiplyVectors(g))
    print (f.sumOfVector())
    print(f.productOfVector())
    print(f.minOfVector())
    print(f.maxOfVector())
    f.substractVectors(g)
    print(f)
    print(p)