#calculater 
import requests
import math
import pandas as pd
import datetime

def create_log_file(log_str):
    time = datetime.datetime.now()
    log = "Time {0} ---> {1}".format(time,log_str)
    with open("log_file.txt",'a+') as f:
        f.write(log + "\n")

class calculater:

    def add(self,number1,number2):
        return (number1+number2)
    def sub(self,number1,number2):
        return (number1 - number2)
    def multi(self,number1,number2):
        return (number1 * number2)
    def division(self,number1,number2):
        return (number1 / number1)
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


class area:
    def triangle():
        print("Enter 1 calculate area with base and height : ")
        print("Enter 2 calculate area with all three side : ")
        ch = int(input("Enter you choice : "))
        if ch == 1:
            b = float(input("Enter base of triangel :"))
            h = float(input("Enter Height of triangle :"))
            result = ((1/2)*(b*h))
            log_str = "Base of Triangle {} ,Height of Triangle {} = area = {}".format(b,h,result)
            create_log_file(log_str)
            return result
        elif ch == 2:
            a = float(input("Enter side a : "))
            b = float(input("Enter side b : "))
            c = float(input("Enter c side : "))
            s = (a+b+c)/2
            result = (math.sqrt(s*(s-a)*(s-b)*(s-c)))
            log_str = "side a of Triangle {} ,side b of Triangle {},side c of Triangle {} and area is {}".format(a,b,c,result)
            create_log_file(log_str)
            return result
    def rectangle():
        a = float(input("Enter side a : "))
        b = float(input("Enter side b : "))
        result = a*b
        log_str = "side a of rectangle {} ,side b of rectangle {} and area is {}".format(a,b,result)
        create_log_file(log_str)
        return result

    def square():
        a = float(input("Enter side a : "))
        result = a*a
        log_str = "side a of square {} and area is {}".format(a,result)
        create_log_file(log_str)
        return result

    def trapezoid():
        a = float(input("Enter parallel side a : "))
        b = float(input("Enter parallel side b : "))
        h  = float(input("Enter Vertical Height h : "))
        result = (1/2)*(a+b)*h

        log_str = "parallel side a of trapezoid {} ,parallel side b of trapezoid {},Vertical Height h of trapezoid {} and area is {}".format(a,b,h,result)

        create_log_file(log_str)
        return result

    def ellips():
        a = float(input("Enter half minar axis : "))
        b = float(input("Enter half major axis : "))
        result = (math.pi*a*b)
        log_str = "half minar axis ellips{} ,half major axis ellips {} and area is {}".format(a,b,result)
        create_log_file(log_str)
        return result

    def circle():
        r = float(input("Enter Radius of Circle : "))
        result = (math.pi*r*r)
        log_str = "Radius of circle {} and area of circle {} ".format(r,result)
        create_log_file(log_str)
        return result

    
def input_function(operation,result):
    

    if (operation >= 1 and operation <= 6):
        if result == 0:
            number1 = float(input("Enter Your Number :"))
            number2 = float(input("Enter Your Number :"))
            return number1,number2
        else :
            number1  = result
            number2 = float(input("Enter Your Number :"))
            return number1,number2

    elif (operation>=7 and operation<=12):
        number1 = float(input("Enter your Number :"))
        number2 = None
        return number1,number2

def choice():
    choice_list = ["Addition","Subtraction","Multiplication","Division","Finding remainder","floor division ","Square","Square root","Cube","Cube root","Nth Degree of number", "Nth root of number"]
    for i in range(0,6):
        print("Enter ",i+1,"for", choice_list[i],"\t \t \t Enter",i+6+1,"for", choice_list[(i+6)])
    print("Enter 0 for Exit :")
    operation = int(input("Enter Operation : "))
    return operation

def simple_calculator():
    
    operation = choice()

    result = 0

    while True:
        if operation == 0:
            break
        if operation == 1:
        
            number1,number2 = input_function(operation,result)
            result = cal.add(number1,number2)
            print(result)
            log_str = "{} {} {} = {}".format(number1,'+',number2,result)
            create_log_file(log_str)
            operation = choice()
            

        elif operation == 2:
            number1,number2 = input_function(operation,result)
            result = cal.sub(number1,number2)
            print(result)
            log_str = "{} {} {} = {}".format(number1,'-',number2,result)
            create_log_file(log_str)
            operation = choice()
                
        elif operation == 3:
            number1,number2 = input_function(operation,result)
            result = cal.multi(number1,number2)
            print(result)
            log_str = "{} {} {} = {}".format(number1,'*',number2,result)
            create_log_file(log_str)
            operation = choice()
                
        elif operation == 4:
            number1,number2 = input_function(operation,result)
            result = cal.division(number1,number2)
            print(result)
            log_str = "{} {} {} = {}".format(number1,'/',number2,result)
            create_log_file(log_str)
            operation = choice()

        elif operation == 5:
            number1,number2 = input_function(operation,result)
            result = cal.modulus(number1,number2)
            print(result)
            log_str = "{} {} {} = {}".format(number1,'%',number2,result)
            create_log_file(log_str)
            operation = choice()

        elif operation == 6:
            number1,number2 = input_function(operation,result)
            result = cal.floor_division(number1,number2)
            print(result)
            log_str = "{} {} {} = {}".format(number1,'//',number2,result)
            create_log_file(log_str)
            operation = choice()
        
        # -----------------------------------------------------
        elif operation == 7:
            number1,number2 = input_function(operation,result)
            result = cal.square(number1)
            print(result)
            log_str = "{} {} {} = {}".format(number1,"",'Square',result)
            create_log_file(log_str)
            operation = choice()

        elif operation == 8:
            number1,number2 = input_function(operation,result)
            result = cal.square_root(number1)
            print(result)
            log_str = "{} {} {} = {}".format(number1,'','Square root',result)
            create_log_file(log_str)
            operation = choice()

        elif operation == 9:
            number1,number2 = input_function(operation,result)
            result = cal.cube(number1)
            print(result)
            log_str = "{} {} {} = {}".format(number1,'','Cube',result)
            create_log_file(log_str)
            operation = choice()

        elif operation == 10:
            number1,number2 = input_function(operation,result)
            result = cal.cube_root(number1)
            print(result)
            log_str = "{} {} {} = {}".format(number1,'','Cube root',result)
            create_log_file(log_str)
            operation = choice()

        elif operation == 11:
            number1,number2 = input_function(operation,result)
            result = cal.Nth_Degree_of_number(number1)
            print(result)
            log_str = "{} {} {} = {}".format(number1,'','Nth Degree of number',result)
            create_log_file(log_str)
            operation = choice()

        elif operation == 12:
            number1,number2 = input_function(operation,result)
            result = cal.Nth_root_of_number(number1)
            print(result)
            log_str = "{} {} {} = {}".format(number1,'','Nth root of number',result)
            create_log_file(log_str)
            operation = choice()


def currency_conversion():
    while True:
        print("Enter 1 to convert currency : ")
        print("Enter 0 to exit : ")
        choice_cc = int(input("Enter your choice : "))
        if choice_cc == 1:
            # list_of_rates = list(requests.get("https://api.frankfurter.app/latest"))

            # print(list_of_rates)

            from_currency = str(
                input("Enter in the currency you'd like to convert from: ")).upper()

            to_currency = str(
                input("Enter in the currency you'd like to convert to: ")).upper()

            amount = float(input("Enter in the amount of money: "))

            response = requests.get(
                f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

            print(
                f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")
            result = response.json()['rates'][to_currency]
            log_str = "{} {} to {} {} ".format(amount,from_currency,result,to_currency)
            create_log_file(log_str)
        elif choice_cc == 0:
            break


def area_choice():
    area_choice_list = ["Triangle","Rectangle","Square","Trapezoid","Ellips","Circle"]
    for i in range(0,3):
        print("Enter ",i+1,"for", area_choice_list[i],"\t \t \tEnter",i+3+1,"for", area_choice_list[(i+3)])

    operation = int(input("Enter Operation : "))
    return operation


def area_calculator():
    operation = area_choice()
    while True:
        if operation == 0:
            break
        if operation == 1:
            result = area.triangle()
            operation = area_choice()
            
        elif operation == 2:
            result = area.rectangle()
            print(result)
            print("Enter 0 for exit :")
            operation = area_choice()
        elif operation == 3:
            result = area.square()
            print(result)
            print("Enter 0 for exit :")
            operation = area_choice()
        elif operation == 4:
            result = area.trapezoid()
            print(result)
            print("Enter 0 for exit :")
            operation = area_choice()
        elif operation == 5:
            result = area.ellips()
            print(result)
            print("Enter 0 for exit :")
            operation = area_choice()
        elif operation == 6:
            result = area.circle()
            print(result)
            print("Enter 0 for exit :")
            operation = area_choice()

def creat_dataframe(number_of_member,group_member_name_list):
    dataframes = []
    for i in range(number_of_member):
        df = pd.DataFrame(columns=group_member_name_list)
        dataframes.append(df)
    return dataframes

def creat_group(group):
    group_name = input("Enter group name : ")
    number_of_member = int(input("Enter Number of Members : "))
    group_member_name_list  = []
    for i in range(number_of_member):
        group_member_name_list.append(input("Enter Member name : "))
    
    df1 = pd.DataFrame(columns=group_member_name_list)
    group[group_name] = df1
 

def entry(group,selcted_goup):
    amount = float(input("Enter your expenditure amount : "))
    count = 1
    print("Group Name : ",selcted_goup)

    paid_by_name = input("Enter Name of person who paid the bill : ")

    df = group[selcted_goup]

    member_list = list(df.columns)

    for i in member_list:
        print("Enter ",count," for ",i)
        count+=1

    print("Enter Your choice seprated by Space :")
    split_member_index = list(map(int, input().split()))
    split_amount = amount/(len(split_member_index))
    data ={}
    for i in member_list:
        data[i] = [0]

    for j in split_member_index:
        data[member_list[j-1]] = split_amount

    data["paid_by"] = [paid_by_name]
    df.loc[len(df.index)] = data
    group[selcted_goup] = df
    return group


def splite_Bills():
    while True:
        print("Enter 1 to the Show Group : ")
        print("Enter 2 to Create Group : ")
        print("Enter 0 to exit : ")
        group =  {}
        choice_b =  int(input("Enter Your choice : "))

        if choice_b == 0:
            break
        elif choice_b == 1:
            for i in group.keys():
                print(i)
            selcted_goup = input("Enter your Selected group name : ")
            group = entry(group,selcted_goup)
        elif choice_b == 2:
            creat_group(group)
            


def percentage_calculator():
    while True:
        print("Enter 1 to calculate area : ") 
        print("Enter 0 to Exit : ")

        choice_pp = int(input("Enter your choice : "))

        if choice_pp == 1: 
            total_marks = int(input("Enter your total marks : "))
            obtain_marks = int(input("Enter TO Obtain marks  :"))
            result =(obtain_marks/total_marks)*100
            print("Your Percentage : ",result,"%")
            log_str =  "Total marks = {}, Obtain marks {} Your Percentage {}".format(total_marks,obtain_marks,result)
            
        elif choice_pp == 0:
            break

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

        print("Enter '0' to exit ")

        print("-"*50)

        print("Enter your choice : ")

        user_choice = int(input("-->"))

        if user_choice == 0:
            break
        elif user_choice == 1:
            simple_calculator()
        elif user_choice == 2:
            currency_conversion()
        elif user_choice == 3:
            area_calculator()
        elif user_choice == 4:
            splite_Bills()
        elif user_choice == 5:
            percentage_calculator()

        print("Enter C to clear ")

        print("Enter Q for exit : ")

    print("Thank You !")        
        


