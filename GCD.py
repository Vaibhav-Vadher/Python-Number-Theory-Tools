n1 = a = int(input("Enter number 1 : "))
n2 = b = int(input("Enter number 2 : "))

while n2 != 0:
    temp = n2
    n2 = n1 % n2
    n1 = temp

print(f"HCF of {a} & {b} is {n1}")
