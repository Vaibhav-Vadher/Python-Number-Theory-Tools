n = int(input("Enter any number : "))
f = 0
d = 1

while d <= n:
    if n % d == 0:
        f += 1
    d += 1

if f == 2:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not prime number")