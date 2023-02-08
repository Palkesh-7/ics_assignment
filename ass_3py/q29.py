# 29.	 Write a Python program to create a Caesar encryption 
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher,
# Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. 
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some 
# fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by
# A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private 
# correspondence.



def Caesar_shift(str29,shift):
    for i in str29:
        if (i.islower()):
            print(chr((ord(i)+shift - ord("a"))%26+ord("a")),end="")
        elif (i.isupper()):
            print(chr((ord(i)+shift - ord("A"))%26+ord("A")),end="")
# def encrypt(text,s):
#     result = ""
#     for i in range(len(text)):
#         char = text[i]
#         if (char.isupper()):
#             result += chr((ord(char) + s-65) % 26 + 65)
#         else:
#             result += chr((ord(char) + s - 97) % 26 + 97)
 
#     return result


str29 = input("Enter any string :")
shift = int(input("Enter shift :"))
Caesar_shift(str29,shift)