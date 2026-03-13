a = float(input("coefficent of a:"))
b = float(input("coefficent of b:"))
c = float(input("coefficent of c:"))

determinant = (b**2)-(4*a*c)
if determinant >=0:
    print("the roots are real.")
else:
    print("the roots are not real")
