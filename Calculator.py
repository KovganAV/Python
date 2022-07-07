while True:
    s = input("Sign (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("First number"))
        y = float(input("Second number"))
        if s == '+':
           print(x + y)
        elif s == '-':
            print(x - y)
        elif s == '*':
            print(x * y)
        elif s == '/':
            if y != 0:
                print(x / y)
            else:
                print('Divide by zero?')
    else:
        print("No")