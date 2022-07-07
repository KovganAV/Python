import random
print('Write the dimension of your list:')
dimensionofthelist = int(input())
print('Write from where and to where to randomize:')
num = int(input())
num1 = int(input())
list = [] * dimensionofthelist
if num >num1:
    for randomrandint in range(dimensionofthelist):
        list.append(random.randint(num1, num))
    print('Your list:', list)
    print('list sum:', sum(list))
if num<=num1:
    for randomrandint in range(dimensionofthelist):
        list.append(random.randint(num, num1))
    print('Your list:', list)
    print('Sum:', sum(list))
