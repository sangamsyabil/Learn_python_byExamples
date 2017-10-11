# Code written by : Hem Raj Regmi (sangamsyabil@gmail.com) http://hemrajregmi.com
# github repository: https://github.com/sangamsyabil/Learn_python_byExamples
''' This is an example of using lambda expression and sorting the both list and tuples. '''


planets = [
    ("Mercury", 2440, 5.43, 0.395),
    ("Venus", 6052, 5.24, 0.732),
    ("Earth", 6378, 5.52, 1.000),
    ("Mars", 3396, 3.93, 1.530),
    ("Jupitar", 71492, 1.33, 5.210),
    ("Saturn", 60268, 0.69, 9.551),
    ("Uranus", 25559, 1.27, 19.213),
    ("Neptune", 24764, 1.64, 30.070)
]
''' format: (name, radious(KM), density(g/cm3), distance from sun(AUs)'''

#lets sort the planets by size - largest the first
size = lambda planet:planet[1] #Using lambda expression to make the sorting function
planets.sort(key=size, reverse=True) #Sorting by descending order. By default it will be ascending (reverse=False)
print(planets)

# list.sort() method changes the list
# to make the list unchanged and to sort the tuples we can use sorted() method
distance = lambda dist:dist[-1]
print(sorted(planets, key=distance, reverse=False))

#Now sorting a tuples
data = (7,4,2,8,2,6,9,2,4,5,8,60,11,25)
print(sorted(data)) #the original data is un-altered. But the sorted(data) becomes List

#Happy coding!!!
