import pandas as pd
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


if __name__ =="__main__":
    while True:
        result  = 0
        print("1> Enter 1 Splite Bills :")
        print("2> Enter 0 for Exit :")
        print("Enter your choice : ")

        user_choice = int(input("-->"))

        if user_choice == 0:
            break
        elif user_choice == 1:
            splite_Bills()