# Messages to print
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

M = 0.0  # Varialbe to store the total

# Asks for an equation
while True:
    print(msg_0)
    calc = input()

    # Spilt into parts x, oper, y
    eq = calc.split()
    x = eq[0]
    oper = eq[1]
    y = eq[2]
    nums = [x,y]

    # Check if str x or y is "M"
    # Check x or y NaN
    try:
        if x == 'M':
            x = M
        else:
            float(x)
    except ValueError:
        print(msg_1)
        continue
    else:
        x = float(x)

    try:
        if y == 'M':
            y = M
        else:
            float(y)
    except ValueError:
        print(msg_1)
        continue
    else:
        y = float(y)

    if oper not in ['+', '-', '*', '/']:
        print(msg_2)
        continue
    else:
        if oper == '+':
            M = (x + y)
            print(M)
        elif oper == '-':
            M = (x - y)
            print(M)
        elif oper == '*':
            M = (x * y)
            print(M)
        elif oper == '/':
            if y != 0:
                M = (x / y)
                print(M)
            else:
                print(msg_3)
                continue

    store = input(msg_4)
    if store == 'n':
        M = 0
    elif store == 'y':
        M = M

    cont = input(msg_5)
    if cont == 'n':
        break
    elif cont == 'y':
        continue


    break

