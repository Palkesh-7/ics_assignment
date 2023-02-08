# # area_choice_list = ["Triangle","Rectangle","Square","Trapezoid","Ellips","Circle"]
# # for i in range(0,3):
# #     print("Enter ",i+1,"for", area_choice_list[i],"\t \t \tEnter",i+3+1,"for", area_choice_list[(i+3)])

# # # operation = int(input("Enter Operation : "))
# # # print(operation)

# group_name = input("Enter group name : ")
# number_of_member = int(input("Enter Number of Members : "))
# group =  {}
# group_member_name_list  = []
# for i in range(number_of_member):
#     group_member_name_list.append(input("Enter Member name : "))


# if group_name not in group.keys():
#     group[group_name] = group_member_name_list
# elif group_name in group.keys():
#     group[group_name] = (group[group_name]).append(name)

# print(group)

def entry(group,group_name):
    amount = float(input("Enter your expenditure amount : "))
    count = 1
    print("Group Name : ",group_name)
    list_member = group[group_name]
    paid_by = input("Enter Name of person who paid the bill : ")
    for i in list_member:
        print("Enter ",count," for ",i)
        count+=1


    print("Enter Your choice seprated by Space :")
    split_member_index = list(map(int, input().split()))
    
    return paid_by,split_member_index


group = {"ics":["palkesh","malviya"]}
group_name = "ics"
entry(group,group_name)
