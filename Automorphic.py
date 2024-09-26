print("Check Automorphic between 1 to 100")

n = 1

while n < 100:
    s = n ** 2
    
    if (n < 10 and n == s % 10):
        print(n)

    elif (n == s % 100):
        print(n)
    
    n += 1