#wtp to check wheather a number is palindrome or not (both number and reverse number is same)
num = int(input("Enter the number:"))
temp = num
reverse = 0
while num != 0:
    rem = num % 10
    reverse = reverse * 10 + rem
    num //= 10
print(str(reverse))
if temp == reverse :
    print("The given number is palindrome")
else:
    print("The given number is not a palindrome")
