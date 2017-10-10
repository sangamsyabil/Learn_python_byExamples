# Code written by : Hem Raj Regmi (sangamsyabil@gmail.com) http://hemrajregmi.com
# github repository: https://github.com/sangamsyabil/Learn_python_byExamples
""" Suppose you have created a vector class to represent two dimensional vectors.
    Let's evaluate this by defining the __add__ method on the class"""

class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        print("Vectors (%d, %d)" % (self.a, self.b))

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 9)
v2 = Vector(9, -2)
print(v1 + v2)

#Happy coding!!!