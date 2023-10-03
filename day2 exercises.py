#Calculate interest rate 

num =int(input("Enter a sarting value: "))
counter=0
target = int(input("Enter a target value: "))
interest = int(input("Enter an interest amount: "))

while num <= target:
    num += num / 100 * interest
    counter += 1
print(counter)

