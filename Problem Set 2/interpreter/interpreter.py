expression = input(str("Expression: "))

x, y, z = expression.split(" ") # x = num, y = +/*-, z = num
x = float(x)
z = float(z)

if y == "+":
    print(x+z)
elif y == "/":
    print(x/z)
elif y == "*":
    print(x*z)
elif y == "-":
    print(x-z)
