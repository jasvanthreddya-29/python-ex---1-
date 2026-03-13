# n1 = int(input("enter the first number:"))
# n2 = int(input("enter the second number:"))
# n3 = int(input("enter the third number:"))

# if n1<n2:
#     print(f"n1 is minimum",n1>n2)
# elif n2<n3:
#     print(f"n2 is minimum",n2>n3)
# elif n3<n1:
#     print(f"n3 is minimum",n3>n1)
    
    
    
    
n1 = int(input("Enter first integer: "))
n2 = int(input("Enter second integer: "))
n3 = int(input("Enter third integer: "))

min_val = n1
if n2 < min_val:
    min_val = n2
if n3 < min_val:
    min_val = n3
print("Minimum value is:", min_val)