from infrastructure.VectorRepository import VectorRepoistory
from domain.MyVector import MyVector
from application.controller import VectorController
from ui.console import run
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
if __name__=="__main__":
    f=MyVector("val","r",1,[2,4,5])
    g=MyVector("v","r",2,[1,2,3])
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