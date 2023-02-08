print("Enter number seprated by comma")
in39 = list(map(int,(input().split(","))))

for i in range(len(in39)):
    if i < len(in39)-1:
        print(in39[i],end=", ")
    else:
        print(in39[i],end="")