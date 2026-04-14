from basic_op import add, subtract, multiply, divide
from adv_op import square, cube, square_root, cube_root

print("Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")
print("6. Cube")
print("7. Square Root")
print("8. Cube Root")

choice = input("Enter choice: ")

if choice in ['1', '2', '3', '4']:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        print(add(a, b))
    elif choice == '2':
        print(subtract(a, b))
    elif choice == '3':
        print(multiply(a, b))
    elif choice == '4':
        print(divide(a, b))

elif choice in ['5', '6', '7', '8']:
    n = float(input("Enter number: "))

    if choice == '5':
        print(square(n))
    elif choice == '6':
        print(cube(n))
    elif choice == '7':
        print(square_root(n))
    elif choice == '8':
        print(cube_root(n))

else:
    print("Invalid input!")