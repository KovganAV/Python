import random
s = random.randint(1, 5)
l = random.randint(1, 2)
print("number of attempts")
print(l)
g = 0
print('enter password')
d = int(input())
while True:
    if l == 1:
       if s == d:
             print('You have successfully entered your password')
       if s != d:
           print("Hazzer?")

    if l == 2:
       if s == d:
              print('You have successfully entered ')
       if  s != d:
              print("Hazzer?")




