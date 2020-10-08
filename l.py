# Exercise 1:
# grades = [20, 10, 90, 85, 40, 75, 65, 64, 12, 74, 71, 98, 50]
# Task:
# Filter the grades to only display everyone above (and including) 70%



grades_in_pec= [20,10,90,85,40,75,65,64,12,74,71,98,50]

good_grades = list(filter(lambda x: x>=70,grades_in_pec))

print(good_grades)



# Exercise 2:
# dog_ages = [12, 8, 4, 1, 2, 6, 4, 4, 5]
# Task:
# Convert the ages into "dog years" (x7)

dog_ages =[12,8,4,1,2,6,4,4,5]

dog_years=list(map(lambda y: y*7,dog_ages))
print(dog_years)



# Exercise 3:
# transactions = [51.0, 49.99, 80.99, 67.99, 120.52, 23.49]
# Task:
# Convert the transactions to a single total

from functools import reduce

transactions = [51.0,49.99,80.99,67.99,120.52,23.49]

total= reduce(lambda a,d: a+d, transactions)

print(total)

