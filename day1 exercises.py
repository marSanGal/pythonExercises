# username=input('Please enter your name')
# age = input('Please enter your age')
# print(username,'is',age,'years old')



# length=int(input('Enter the length of the rectangle')) #int para que lea el numero y no string
# width= int(input('Enter the width of the rectangle'))
# print('Perimeter:' + str(length*2) + str(width*2))
# print('Area:' + str(length*width))



# age = 16

# if age >= 18:
#     print("You are in category A")
# if age >= 16:
#     print("You are in category B")
# if age < 16:
#     print("You are in category C")



# num1 = int(input("Please enter the first number: "))
# num2 = int(input("Please enter the second number: "))

# print("Add: +\nSubstract: -\nmultiply: *\nDivide: /\nSquare: S")
# op = input("Please enter the operation to perform: ")

# if op == "+":
#     res= num1 + num2
#     print(res)
# elif op == "-":
#     res= num1 - num2
#     print(res)
# elif op == "*":
#     res= num1 * num2
#     print(res)
# elif op == "/":
#     res= num1 / num2
#     print(res)
# elif op == "S":
#     res= num1 ** num2
#     print(res)
# else:
#     print("Not a valid operation, please try again")



mark = int(input("Please enter the mark: "))

if mark > 100 or mark < 1:
    print("Invalid mark, please try again")
else:
    if mark > 70:
        print("Distinction")
    elif mark > 60:
        print("Merit")
    elif mark >= 50:
        print("pass")
    else:
        print("Fail!")