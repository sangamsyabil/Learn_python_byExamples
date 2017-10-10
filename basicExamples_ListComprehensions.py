# Code written by : Hem Raj Regmi (sangamsyabil@gmail.com) http://hemrajregmi.com
# github repository: https://github.com/sangamsyabil/Learn_python_byExamples
""" List comprehensions are an elegent way to define and create list in python.
    List comprehensions is a complete substitute for the lambda function as well as
    functions map(), filter() and reduce()."""

# convert from celsious to farenheit scale
celsious = [39.2, 33.25, 25.21, 36.25, 33.33]
fahrenheit = [((float(9)/5)*x) for x in celsious]
print("Celsious =", celsious)
print("Farenheit =", fahrenheit)

# create the list of reminder when you divide the first 100 squares by 7
reminders = [x**2%7 for x in range(1, 101)]
print("Reminders =", reminders)

# calculate the cartesian product
A = [1,3,5,7,9]
B = [2,4,6,8,10]
print("Cartesian Product = ", [(a,b) for a in A for b in B])

# create pythagorian triples between one to thirty
print([(x,y,z) for x in range(1,31) for y in range(1,31) for z in range(1,31)])

# Happy coding !!!