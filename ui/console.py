from application.controller import VectorController
from domain.MyVector import MyVector

def print_menu():
    print("\nType '1' to list all commands\nType '0' to finish the program")
    print("0 - exit")
    print("1 - help")
    print("2 - List of Vectors")
    print("3 - Add Vector")
    print("4 - Vector Operations")
    print("5 - Get Vector at an index")
    print("6 - Update a vector at a given index")
    print("7 - Update a vector at a name_id")
    print("8 - Delete a vector by index")
    print("9 - Delete a vector by name_id")
    print("10 - Plot All Vectors")
    print("11 - Sum of elements with color")
    print("12 - Delete all vectors")
    print("13 - Update color at type")
def Vector_op():
    print("0 -back")
    print("-1 - Exit Program")
    print("1 - Add Scalar to vector")
    print("2 - Add two vectors")
    print("3 - Substract two vectors")
    print("4 - Multiplication")
    print("5 - Sum of elem in a vector")
    print("6- Average of elements in a vector")
    print ("7-Product of elements in vector")
    print ("8 - Minimum of vector")
    print ("9 - Maximum of vector")
def run (controller: VectorController):
    print_menu()
    f = MyVector("val", "r", 1, [2, 4, 5])
    g=MyVector("v","r",2,[1,2,3])
    controller.add_vector(f)
    controller.add_vector(g)
    command=input(">>> ")
    while command !="0":
        if command == "1":
            print_menu()
        elif command =="2":
            if len(controller)==0:
                print("No Vector")
                print_menu()
            print(controller)
        elif command =="3":
            print("\n Add new Vector")

            try:
                name_id = input("Name_id = ")
                colour = input("Color (r,b,g,y) = ")
                typ=int(input ("Type = "))
                numar=int(input("Number of values:"))
                values = []
                for e in range(0,numar):
                    ele=int(input("enter Value: "))
                    values.append(ele)
                f=MyVector(name_id,colour,typ,values)
                controller.add_vector(f)
            except ValueError as ex:
                print(f"Enter the right numbers.\n{ex}")
                print_menu()
        elif command =="4":
            Vector_op()
            command1=input(">>> ")
            while command1 != "0":
                if command1 == "1":
                    print(controller)
                    vec=int(input("Choose vector by index: "))
                    scalar=int(input("scalar: "))
                    controller.add_scalar(vec,scalar)
                    break
                elif command1=="2":
                    print(controller)
                    vec = int(input("Choose vector(to be added) by index: "))
                    vec2=int(input("choose the second vector: "))
                    controller.add_vectors(vec,vec2)
                    break
                elif command1=="3":
                    print(controller)
                    vec = int(input("Choose vector(to be substracted) by index: "))
                    vec2 = int(input("choose the second vector: "))
                    controller.sub_vectors(vec, vec2)
                    break
                elif command1=="4":
                    print(controller)
                    vec = int(input("Choose vector(to be multiplied) by index: "))
                    vec2 = int(input("choose the second vector: "))
                    print(controller.mul_vectors(vec, vec2))
                    break
                elif command1=="5":
                    print(controller)
                    vec=int(input("choose vector by index"))
                    print(controller.get_vectorAtIndex(vec).sumOfVector())
                elif command1=="7":
                    print(controller)
                    vec=int(input("choose vector by index"))
                    print(controller.get_vectorAtIndex(vec).productOfVector())
                elif command1=="6":
                    print(controller)
                    vec = int(input("choose vector by index"))
                    print(controller.get_vectorAtIndex(vec).avarageOfVector())

                elif command1=="8":
                    print(controller)
                    vec=int(input("choose vector by index"))
                    print(controller.get_vectorAtIndex(vec).minOfVector())
                elif command1=="9":
                    print(controller)
                    vec=int(input("choose vector by index"))
                    print(controller.get_vectorAtIndex(vec).maxOfVector())
                else:
                    command1=0
                command1 = input(">>> ")

        elif command =="5":
            ind=int(input("Index= "))
            try:
                print(controller.get_vectorAtIndex(ind))
            except ValueError as ex:
                print(f"Enter the right index.\n{ex}")
                print_menu()
        elif command =="6":
            try:
                ind=int(input("Index: "))
                name_id = input("Name_id = ")
                colour = input("Color (r,b,g,y) = ")
                typ = int(input("Type = "))
                numar = int(input("Number of values:"))
                values = []
                for e in range(0, numar):
                    ele = input("enter Value: ")
                    values.append(ele)
                controller.update_atIndex(ind,name_id,colour,typ,values)
            except ValueError as ex:
                print(f"Enter the right index.\n{ex}")
                print_menu()
        elif command =="7":
            try:
                name_id = input("Name_id = ")
                colour = input("Color (r,b,g,y) = ")
                typ = int(input("Type = "))
                numar = int(input("Number of values:"))
                values=[]
                for e in range(0, numar):
                    ele = input("enter Value: ")
                    values.append(ele)
                controller.uptdate_atNameId(name_id,colour,typ,values)
            except ValueError as ex:
                print(f"Enter the right index.\n{ex}")
                print_menu()
        elif command == "8":
            ind=int(input("Index: "))
            controller.del_byIndex(ind)
        elif command =="9":
            name_id=input("Name id: ")
            controller.del_nameId(name_id)
        elif command =="10":
            controller.plot_all()
        elif command =="11":
            colour=input("Colour: ")
            print(controller.sum_ElementWithColor(colour))
        elif command =="12":
            controller.del_AllVectors()
            print("vectors have been deleted")
        elif command == "13":
            typ=int(input("Type: "))
            colour=input("Colour")
            controller.update_colorAtType(typ,colour)


        else:
            print("Command not defined")
        command=input(">>> ")
if __name__=="__main__":
    controller=VectorController()
    run(controller)