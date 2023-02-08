for i in range(1,11):
    print("\t",i,end="")
print("\n +-------------------------------------------------------------------------------------")
for i in range(1,11):
    if (i<10):
        print(" ",end="")
    print(i,"| ",end="")
    j=1
while(j<=10):
    print("\t",j*i,end="")
    j+=1
    print("\n")
                
                
                
# if __name__=="__main__":
#     multiplication_table()