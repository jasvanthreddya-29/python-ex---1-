# n1 = float(input("Enter the first number:"))
# n2 = float(input("Enter the seconed number:"))
# op = input("enter the operation(+,-,/,*):")

# if op == '+': print(f"result:{n1+n2}")
# elif op == '-':print(f"result:{n1-n2}")
# elif op == '*': print(f"result: {n1*n2}")
# elif op == '/':print(f"result:{n1/n2 if n2 !=0 else "error: divison by zero"}")
 

n1 = float(input("Enter the first number:"))
n2 = float(input("Enter the second number:"))
op =input("Enter the operation(+,-,*,/):")
if op == '+':print(f"resutl is:{n1+n2}")
elif op == '-':print(f"result is:{n1-n2}")
elif op == '*':print(f"result is:{n1*n2}")
elif op == '/':print(f"result is:{n1 / n2 if n2 !=0 else "error : division by error"}")


