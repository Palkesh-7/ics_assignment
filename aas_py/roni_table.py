def multiplication_table():
    for i in range(1,11):
        if (i<10):
            print(" ",end="")
            print(i,"| ",end="")
        print("\n ",i,"|", end=" ")
        for j in range(1,11):
            print(i*j,end=" ")




if __name__=="__main__":
    multiplication_table()