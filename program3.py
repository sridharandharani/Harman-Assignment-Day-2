# wtp to print all the prime numbers in between 2 and 500 (number divisible by 1 nd itself)
for num in range(2,500):
    if (num > 2):
        for i in range(2,num):
            if(num % i) == 0:
                break
        else:
                print(num)
