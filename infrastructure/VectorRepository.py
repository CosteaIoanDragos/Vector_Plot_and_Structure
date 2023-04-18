from domain.MyVector import MyVector
from matplotlib import pyplot as plt
class VectorRepoistory:
    def __init__(self):
        """
        crate a list of vectors
        """
        self.__data=[]
    def __str__(self):
        """
        creates a string representation of the list of vectors
        :return:
        """
        s = ""
        for elem in self.__data:
            s += str(elem) + "\n"
        return s
    def __len__(self):
        """
        calcuates the number of vectors in the repository
        :return:
        """
        return len(self.__data)
    def addVector(self,st):
        """
        adds a vector to the repository
        :param st:
        :return:
        """
        ok=1
        for elem in self.__data:
            if st.get_name_id()== elem.get_name_id():
                ok=0
        if ok==1:
            self.__data.append(st)
        else:
            raise ValueError("The id has been used")

    def sumOfElementWithColor(self,colour):
        """
        sums up the elements with the same color
        :param colour:
        :return:
        """
        suma = 0
        for elem in self.__data:
            if colour==elem.get_colour():
                v=elem.get_values()
                suma=suma+sum(v)
        return suma
    def delAllVectors(self):
        """
        delets all vectors from repository
        :return:
        """
        for i in range(len(self.__data)-1,-1,-1):
            del self.__data[i]

    def updateColorAtType(self,type,color):
        """
        updates the color of an element ,by type
        :param type:
        :param color:
        :return:
        """
        for elem in self.__data:
            if type==elem.get_type():
                elem.set_colour(color)
    def get_Vectors(self):
        return self.__data
    def getVectorAtIndex(self,index):
        """
        It returns a vector at at index
        if the index is not valid returns None
        :param index: int
        :return: vector or none
        """
        if index>=len(self.__data) or index<0:
            raise ValueError
        for i in range(len(self.__data)):
            if i==index:
                return self.__data[i]
    def updateAtIndex(self,index,name_id,colour,typ,values):
        """
        uptates a vector at an index
        :param index:
        :param name_id:
        :param colour:
        :param typ:
        :param values:
        :return:
        """
        if index>=len(self.__data) or index<0:
            raise ValueError
        i=0
        for elem in self.__data:
            if i==index:
                elem.set_colour(colour)
                elem.set_type(typ)
                elem.set_name_id(name_id)
                elem.set_values(values)
            i=i+1
    def updateAtNameId(self,name_id,colour,typ,values):
        """
        updates an element at a given name id
        :param name_id:
        :param colour:
        :param typ:
        :param values:
        :return:
        """
        ok=0
        for elem in self.__data:
            if elem.get_name_id()==name_id:
                ok=1
        if ok==0:
            raise ValueError
        for elem in self.__data:
            if elem.get_name_id()==name_id:
                elem.set_colour(colour)
                elem.set_values(values)
                elem.set_type(typ)
    def delByIndex(self,index):
        """
        deletes an element in the repository by index
        :param index:
        :return:
        """
        if index >= len(self.__data) or index < 0:
            raise ValueError

        for i in range(len(self.__data)-1,-1,-1):
            if i==index:
                del self.__data[i]
    def delByNameId(self,name_id):
        """
        deletes an element in the repository by name id
        :param name_id:
        :return:
        """
        ok=0
        for elem in self.__data:
            if elem.get_name_id()==name_id:
                ok=1
        if ok==0:
            raise ValueError
        for elem in self.__data:
            if elem.get_name_id()==name_id:
                self.__data.remove(elem)

    def plot(self):
        """
        plots the elements in a graph
        :return:
        """
        for v in self.__data:
            shape = "d"
            if v.get_type() == 1:
                shape = "o"
            elif v.get_type() == 2:
                shape = "s"
            elif v.get_type() == 3:
                shape = "v"
            plt.scatter(range(len(v.get_values())), v.get_values(), color=v.get_colour(), marker=shape)

        plt.show()

    ## extra features from my vector (put here for implementation,i think they are unnecessary)
    def add_scalar(self,ind,scalar):
        i=0
        for elem in self.__data:
            if i==ind:
                elem.addScalar(scalar)
            i=i+1
    def addVectors(self,ind1,ind2):
        i=0
        for elem in self.__data:
            if i==ind1:
                elem.addVectors(self.__data[ind2])
            i=i+1
    def subVectors(self,ind1,ind2):
        i = 0
        for elem in self.__data:
            if i == ind1:
                elem.substractVectors(self.__data[ind2])
            i=i+1
    def mulVectors(self,ind1,ind2):
        i = 0
        for elem in self.__data:
            if i == ind1:
                return(elem.multiplyVectors(self.__data[ind2]))
            i = i + 1
    def sumOfElem(self,ind1):
        i=0
        for elem in self.__data:
            if i==ind1:
                return elem.sumOfVector()
            i=i+1
    def productOfVectors(self,ind1):
        i = 0
        for elem in self.__data:
            if i == ind1:
                return elem.productOfVector()
            i = i + 1


if __name__ == "__main__":
    f = MyVector("val", "r", 1, [2, 4, 5])
    g = MyVector("v", "r", 2, [1, 2, 3])
    st=VectorRepoistory()
    st.addVector(f)
    st.addVector(g)
    print(st)
    print(st.mulVectors(0,1))
    print(st)
    st.subVectors(0,1)
    print(st)