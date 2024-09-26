print("Check Palindrome")
n = int(input("Enter numbers or word : "))

temp = n
rev = 0

while temp > 0:
    i = temp % 10
    rev = (rev * 10 ) + i
    temp //= 10

if n == rev:
    print("It is Palindrome")
else:
    print("Not a Palindrome")       