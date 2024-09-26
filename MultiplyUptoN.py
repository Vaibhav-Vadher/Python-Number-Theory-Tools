n = int(input("Enter any number  : "))
multi = 1


while n >= 1:
    multi *= n
    n -= 1

print(f"Multiplication of all number upto {n} is {multi}.")