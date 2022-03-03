# wtp to check wheather a string is palindrome or not (both string and reverse string is same)
string = input("Enter a string:")
i = 0
for i in range(len(string)):
    if string[i] != string[-1+i]:
        print("The given string is not a palindrome")
        break
    else:
        print("The given string is a palindrome")
        break