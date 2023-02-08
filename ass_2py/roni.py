def Batch_of_hundread(start,end):
    if start>0:
        for i in range(start, end+1):
            print("\t",i,end=" ")
            if i % 100 == 0:
                print("\n",end=" \n")
    else:
        print("\n You enter WRONG input. Please enter valid input ")



if __name__=="__main__":
    start= int(input("\nEnter a starting number : "))
    end=int(input("\nEnter the ending number : "))
                        
                    
Batch_of_hundread(start,end)