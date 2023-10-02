username=input('Please enter your name')
age = input('Please enter your age')
print(username,'is',age,'years old')

length=int(input('Enter the length of the rectangle')) #int para que lea el numero y no string
width= int(input('Enter the width of the rectangle'))
print('Perimeter:' + str(length*2) + str(width*2))
print('Area:' + str(length*width))