A = int(input())
B = int(input())
C = int(input())
X = int(input())
Y = int(input())
door_dimensions = X * Y
if A * B <= door_dimensions:
    print("The box can be carried")
elif B * C <= door_dimensions:
    print("The box can be carried")
elif A * C <= door_dimensions:
    print("The box can be carried")
else:
    print("The box cannot be carried")
