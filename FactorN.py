n = int(input("Enter any number  : "))
i = 1

while n >= i:
    if n % i == 0:
        print(f"Factor of number {n} is {i}.")
    i += 1