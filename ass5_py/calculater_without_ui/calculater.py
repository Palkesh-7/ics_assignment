#calculater 
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



if __name__ =="__main__":
    q = "d"
    cal = calculater()
    while q!="Q":
        result  = 0
        print("--"*50)
        print("Enter Number with signs (+,-,*,/,%) ")
        eq = input()
        if eq == "Q":
            q = "Q"
            break
        
        eq.replace(" ","")

        if result == 0:
            if eq[1] == "+":
                result = cal.add(int(eq[0]),int(eq[2]))
            elif eq[1] == "-":
                result = cal.sub(int(eq[0]),int(eq[2]))
            
            elif eq[1] == "*":
                result = cal.multi(int(eq[0]),int(eq[2]))

            elif eq[1] == "/":
                result = cal.division(int(eq[0]),int(eq[2]))

            elif eq[1] == "%":
                result = cal.modulus(int(eq[0]),int(eq[2]))

        if result!=0:
            for i in range(3,len(eq),2):
                k = i+1
                if eq[i] == "+":
                    result = cal.add(result,int(eq[k]))
                elif eq[i] == "-":
                    result = cal.sub(result,int(eq[k]))
                
                elif eq[i] == "*":
                    result = cal.multi(result,int(eq[k]))

                elif eq[i] == "/":
                    result = cal.division(result,int(eq[k]))

                elif eq[i] == "%":
                    result = cal.modulus(result,int(eq[k]))

        print("You result : ",result)

        print("Enter C to clear ")

        print("Enter Q for exit : ")

    print("Thank You !")        
        


