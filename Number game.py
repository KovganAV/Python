import random
import turtle
s = 0
p = 0
while True:
    if s == 0:
        a = input("Enter: 1 - light, 2 - medium, 3 - heavy:")
        try:
            int(a)
        except ValueError:
            print("Error")
            continue
        if s == 0:
            if int(a) == 1:
                k = 13
                s = 1
                checkK = k
            elif int(a) == 2:
                k = 9
                s = 1
                checkK = k
            elif int(a) == 3:
                k = 6
                s = 1
                checkK = k
            else:
                print("Error")
                continue
    ran = input("Enter the number hidden number in the range from 1 to 10:")
    l = random.randrange(1, 10, 1)
    try:
        int(ran)
    except ValueError:
        print("Error")
        continue
    while checkK != 0:
        if l == int(ran):
            print("You guessed")
            checkK = k
            p += 1
            break
        elif l > int(ran):
            print(f"More")
            checkK += -1
            ran = input("Enter the number hidden number in the range from 1 to 10:")
        elif l < int(ran):
            print(f"Less")
            checkK += -1
            ran = input("Enter the number hidden number in the range from 1 to 10:")
    else:
        print("You lost")
        print(p)
        break