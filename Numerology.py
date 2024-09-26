def numerology():

    d = int(input("Enter ONLY Your Birth Date : "))
    m = int(input("Enter ONLY Your Birth Month : "))
    y = int(input("Enter ONLY Your Birth Year : "))

    s = t1 = t2 = 0

    if d >= 10:
        s += d%10
        s += d//10
    else:
        s += d

    if m >= 10:
        s += m%10
        s += m//10
    else:
        s += m

    while y > 0:
        s += y % 10
        y //= 10

    if s > 9:
        t1 += s%10
        t1 += s//10
    else:
        pass

    if t1 > 9:
        t2 += t1%10
        t2 += t1//10
    else:
        pass

    if t2 == 1:
        print(f"\nYour Numerology Number is {t2} \nNumber 1 indicates pillar shape and reflects independence and strength.")
    elif t2 == 2:
        print(f"Your Numerology Number is {t2} \nNumber 2 plays a supportive role in their life. They are sentimental, lazy, and can easily get depressed.")
    elif t2 == 3:
        print(f"Your Numerology Number is {t2} \nNumber 3 is the most imaginative of all numbers and is reflected in its open and inviting shape, ready to embrace anyone in this world.")
    elif t2 == 4:
        print(f"Your Numerology Number is {t2} \nNumber 4 is square-shaped and down to earth. It is fixed on the ground and acts as a rock of support for all other numbers.")
    elif t2 == 5:
        print(f"Your Numerology Number is {t2} \nNumber 5 is open in front and back. It is the most dynamic of all the numbers.")
    elif t2 == 6:
        print(f"Your Numerology Number is {t2} \nNumber 6 is the most loving and surviving of all numbers, magnetic, youthful, gentle, soft-spoken, romantic, luxury-loving, artistic, and possessors of refined taste.")
    elif t2 == 7:
        print(f"Your Numerology Number is {t2} \nNumber 7 is a thinker and a saint. It is creative, unconventional & moody. It is the most spiritual of all numbers.")
    elif t2 == 8:
        print(f"Your Numerology Number is {t2} \nNumber 8 represents the balance between the spiritual and material world. The symbol of 8 reflects heaven and earth in the two circles stacked on top of each other.")
    elif t2 == 9:
        print(f"Your Numerology Number is {t2} \nNumber 9 completes the circle. Like 6, it is a loving number, but where 6 loves the family, friends and the community, 9 gives its love to the world; it is the humanitarian number. Thus, considered to be a lucky number.")

numerology()