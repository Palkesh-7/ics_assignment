# 32.	Write a Python program to add prefix text to all of the lines in a string.  


str32 = '''Pranamasana (Prayer pose)
Hastauttanasana (Raised arms pose)
Hastapadasana (Standing forward bend)
Ashwa Sanchalanasana (Equestrian pose)
Dandasana (Stick pose)
Ashtanga Namaskara (Salute with eight parts)
Bhujangasana (Cobra pose)
Adho Mukha Svanasana (Downward facing dog pose)
Ashwa Sanchalanasana (Equestrian pose)
Hastapadasana (Standing forward bend)
Hastauttanasana (Raised arms pose)
Tadasana (Mountain Pose)'''


str32_list = str32.split("\n")
k = 1
for i in str32_list:
    print(k,". ",i)
    k+=1