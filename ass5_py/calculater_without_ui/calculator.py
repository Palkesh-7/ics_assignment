#calculater 

import math

class calculater:

    def add(self,number1,number2):
        return (number1+number2)
    def sub(self,number1,number2):
        return (number1 - number2)
    def multi(self,number1,number2):
        return (number1 * number2)
    def division(self,number1,number2):
        return (number1 / number2)
    def modulus(self,number1,number2):
        return (number1 % number2)
    def floor_division(self,number1,number2):
        return (number1//number2)
    
    
    def square(self,number1):
        return number1*number1


    def square_root(self,number1):
        return math.sqrt(number1)
    
    def cube(self,number1):
        return (number1*number1*number1)
    def cube_root(self,number1):
        return ((number1)**(1/3))

    def Nth_Degree_of_number(self,number1):
        degree = int(input("Enter degree : "))
        return (number1**degree)

    def Nth_root_of_number(self,number1):
        root = int(input("Enter root"))
        return (number1**(1/root))



        
def input_function(result):
    choice_list = ["Addition","Subtraction","Multiplication","Division","Finding remainder","floor division ","Square","Square root","Cube","Cube root","Nth Degree of number", "Nth root of number"]
    for i in range(len(choice_list)):
        print("Enter ",i+1,"for", choice_list[i])

    operation = int(input("Enter Operation : "))

    if (operation >= 1 and operation <= 6):
        if result == 0:
            number1 = float(input("Enter Your Number :"))
            number2 = float(input("Enter Your Number :"))
            return number1,number2,operation
        else :
            number2  = result
            number1 = float(input("Enter Your Number :"))
            return number1,number2,operation

    elif (operation>=7 and operation<=12):
        number1 = float(input("Enter your Number :"))
        number2 = None
        return number1,number2,operation

def simple_calculator():
    choice_list = ["Addition","Subtraction","Multiplication","Division","Finding remainder","floor division ","Square","Square root","Cube","Cube root","Nth Degree of number", "Nth root of number"]
    for i in range(len(choice_list)):
        print("Enter ",i+1,"for", choice_list[i])

    operation = int(input("Enter Operation : "))

    result = 0

    while True:
        if operation == 0:
            break
        if operation == 1:
            number1,number2,operation = input_function(result)
            result = cal.add(number1,number2)
            print(result)

        elif operation == 2:
            number1,number2,operation = input_function(result)
            result = cal.sub(number1,number2)
            print(result)
                
        elif operation == 3:
            number1,number2,operation = input_function(result)
            result = cal.multi(number1,number2)
            print(result)
                
        elif operation == 4:
            number1,number2,operation = input_function(result)
            result = cal.division(number1,number2)
            print(result)

        elif operation == 5:
            number1,number2,operation = input_function(result)
            result = cal.modulus(number1,number2)
            print(result)

        elif operation == 6:
            number1,number2,operation = input_function(result)
            result = cal.floor_division(number1,number2)
            print(result)
        
        # -----------------------------------------------------
        elif operation == 7:
            number1,number2,operation = input_function(result)
            result = cal.square(number1)
            print(result)

        elif operation == 8:
            number1,number2,operation = input_function(result)
            result = cal.square_root(number1)
            print(result)

        elif operation == 9:
            number1,number2,operation = input_function(result)
            result = cal.cube(number1)
            print(result)

        elif operation == 10:
            number1,number2,operation = input_function(result)
            result = cal.cube_root(number1)
            print(result)

        elif operation == 11:
            number1,number2,operation = input_function(result)
            result = cal.Nth_Degree_of_number(number1)
            print(result)

        elif operation == 12:
            number1,number2,operation = input_function(result)
            result = cal.Nth_root_of_number(number1)
            print(result)




if __name__ =="__main__":


    cal = calculater()
    while True:
        result  = 0

        print("--"*50)
        title = "Advance Calculator"
        title= title.center(50)
        print(title)
        print("1> Enter 1 Simple calculator :")
        print("2> Enter 2 currency conversion :")
        print("3> Enter 3 Area calculator :")
        print("4> Enter 4 Splite Bills :")
        print("5> Enter 5 Percentage calculator :")

        print()

        print("Enter 'q' to exit ")

        print("-"*50)

        print("Enter your choice : ")

        user_choice = int(input("-->"))

        if user_choice == 0:
            break
        elif user_choice == 1:
            simple_calculator()
        elif user_choice == 2:
            pass
        elif user_choice == 3:
            pass

        print("You result : ",result)

        print("Enter C to clear ")

        print("Enter Q for exit : ")

    print("Thank You !")        
        


