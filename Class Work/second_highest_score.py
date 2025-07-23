#second_highest_score
 
print ('Get the second highest score')


a = 62
b = 98
c = 85
 
if (a > b > c) or (c > b > a):
  second_highest = b

elif (b > a > c) or (c > a > b):
  second_highest = b

else:
  second_highest = c 

print ('The second highest score is:', second_highest)
 