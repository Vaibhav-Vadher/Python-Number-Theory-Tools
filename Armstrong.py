print("Check Armstrong")

n = int(input("Enter any number : "))

temp = n
sum = 0

while temp > 0:
    r = temp % 10
    sum += r ** 3
    temp //= 10

if n == sum:
    print("It is Armstrong")
else:
    print("It is NOT Armstrong")