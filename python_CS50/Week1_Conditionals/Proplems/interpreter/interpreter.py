expression = input("Expression: ")
x, y, z = expression.split(" ")
#expession = ((float(x)),y,float(z))
result = eval(f"{x}{y}{z}")
print ("{:.1f}".format(result))