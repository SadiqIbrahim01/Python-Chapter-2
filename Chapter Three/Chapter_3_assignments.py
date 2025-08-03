# Chapter_3_assignments 

3.1) 

3.2) Nothing except both variables have a single value assigned to them

3.3) >>>>>>>>>>
     <<<<<<<<<<
     >>>>>>>>>>
     <<<<<<<<<<
     >>>>>>>>>>
     <<<<<<<<<<
     >>>>>>>>>>
     <<<<<<<<<<
     >>>>>>>>>>
     <<<<<<<<<<

3.4) for row in range(2):
	for column in range(7):
		print('@', end='')
	print()

3.5) # Turing test
print("What is your problem?")
input()

print("Have you had this problem before (yes or no)?")
response = input()

if response == "yes":
    print("Well, you have it again.")
else:
    print("Well, you have it now.")

This will not convince the user as it ignores an the first question 



3.6) #Table of Squares and Cube

print(f"{'Number'} {'Square'} {'Cube'}")

for number in range(6):
    square = number ** 2
    cube = number ** 3
    print(f"{number:>6} {square:>6} {cube:>6}")


3.8) # Arithmetic Largest and Smallest
for i in range(4):
    num = int(input(f"Enter integer #{i + 1}: "))

3.9)

3.10)

3.11) # miles per gallon 
total_miles = 0
total_gallons = 0

while True:
    miles = float(input("Enter miles driven (-1 to quit): "))
    if miles == -1:
        break

    gallons = float(input("Enter gallons used: "))
    mpg = miles / gallons
    print(f"Miles per gallon for this tankful: {mpg:.2f}")

    total_miles += miles
    total_gallons += gallon

3.12) # palindrome_checker
number = int(input("Enter a five-digit integer: "))
if 10000 <= number <= 99999:
    digit1 = number // 10000         
    digit2 = (number // 1000) % 10   
    digit3 = (number // 100) % 10    
    digit4 = (number // 10) % 10    
    digit5 = number % 10           
    
    # Check if first and last digits match
    if digit1 == digit5 and digit2 == digit4:
        print(f"{number} is a palindrome")
    else:
        print(f"{number} is not a palindrome")

3.13) # factorials
number = int(input("Enter a nonnegative integer: "))
if number >= 0:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is {factorial}")
else:
    print("Please enter a nonnegative integer")

3.16) #two largest values
largest = float('-inf')
second_largest = float('-inf')
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print(f"The largest number is: {largest}")
print(f"The second-largest number is: {second_largest}")

3.17) # triangles
#first triangle
for i in range(10):
    spaces = " " * i
    asterisks = "*" * (10 - i)
    print(spaces + asterisks)

#second triangle
for i in range(1, 11):
    asterisks = "*" * i
    spaces = " " * (10 - i)
    print(asterisks + spaces)

#third triangle
for i in range(1, 11):
    asterisks = "*" * i
    spaces = " " * ((10 - i) // 2)
    print(spaces + asterisks + spaces)

#fourth triangle
for i in range(10):
    asterisks = "*" * (10 - i)
    spaces = " " * (i // 2)
    print(spaces + asterisks + spaces)

3.21) # Calculate change
price = int(input("Enter purchase price in cents (1-100): "))

if 1 <= price <= 100:
    change = 100 - price
 
    quarters = change // 25
    change = change % 25
    dimes = change // 10
    change = change % 10
    nickels = change // 5
    pennies = change % 5

    print(f"Change for ${price/100:.2f} from $1.00:")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")
else:
    print("Please enter a valid price between 1 and 100 cents")



