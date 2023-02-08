print("     ",end="")
count = 1
for x in range(1,11):
    if x<10:
        print("     ",x,end="")
    else:
        print("  ",x,end="")

print()
print("     ",end="")
print("-"*52)
for i in range(1,11):
    if count<10:
        print(count,"  |",end="")
    else:
        print(count," |",end ="")
    for j in range(2,11):
        if (i*j<10):
            print("   ",i*j,end ="")
        elif(i*j>=10):
            print("  ",i*j,end="")
        elif(i*j>=100):
            print("",i*j,end="")
    count+=1
    print()