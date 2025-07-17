# Three integers

print ('You should input three integers')

number_one = int (input('Enter first integer: '))

number_two = int (input('Enter second integer: '))

number_three = int (input('Enter third integer: '))

sum = number_one + number_two + number_three

print ('Sum of integers is ', sum)

average = sum / 3

print ('Average of integers is ', round(average, 2))

product = number_one * number_two * number_three

print ('Product is ', product)


print ('Largest is ', max(number_one, number_two, number_three))

print ('Smallest is ', min(number_one, number_two, number_three))
