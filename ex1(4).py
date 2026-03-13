length = float(input("Enter the length:"))
breadth = float(input("Enter the breadth:"))
if length > 0 and breadth > 0 :
    area = length * breadth 
    perimeter = 2*(length + breadth)
    print("area:",area)
    print("perimeter",perimeter)
else:
    print("error:length and breadth must be positive numbers. ")
