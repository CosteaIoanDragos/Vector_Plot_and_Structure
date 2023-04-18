from domain.MyVector import MyVector
from infrastructure.VectorRepository import VectorRepoistory
class VectorController:

    def __init__(self,vector_repo:VectorRepoistory=VectorRepoistory()):
        self.__vector_repo=vector_repo
    def __len__(self):
        return len(self.__vector_repo)
    def __str__(self):
        return str(self.__vector_repo)
    def add_vector(self,vec):
        self.__vector_repo.addVector(vec)
    def sum_ElementWithColor(self,colour):
        return self.__vector_repo.sumOfElementWithColor(colour)
    def del_AllVectors(self):
        self.__vector_repo.delAllVectors()
    def update_colorAtType(self,typ,col):
        self.__vector_repo.updateColorAtType(typ,col)
    def get_vectorAtIndex(self,ind):
        return self.__vector_repo.getVectorAtIndex(ind)
    def update_atIndex(self,ind,name_id,colour,typ,values):
        self.__vector_repo.updateAtIndex(ind,name_id,colour,typ,values)
    def uptdate_atNameId(self,name_id,colour,typ,values):
        self.__vector_repo.updateAtNameId(name_id,colour,typ,values)
    def del_byIndex(self,ind):
        self.__vector_repo.delByIndex(ind)
    def del_nameId(self,name_id):
        self.__vector_repo.delByNameId(name_id)
    def plot_all(self):
        self.__vector_repo.plot()
    def add_scalar(self,ind,scalar):
        self.__vector_repo.add_scalar(ind,scalar)
    def add_vectors(self,ind1,ind2):
        self.__vector_repo.addVectors(ind1,ind2)
    def sub_vectors(self,ind1,ind2):
        self.__vector_repo.subVectors(ind1,ind2)
    def mul_vectors(self,ind1,ind2):
        return(self.__vector_repo.mulVectors(ind1,ind2))

    def sumOfElem(self, ind1):
        return self.__vector_repo.sumOfElem(ind1)

    def productOfVectors(self, ind1):
        return self.__vector_repo.productOfVectors(ind1)