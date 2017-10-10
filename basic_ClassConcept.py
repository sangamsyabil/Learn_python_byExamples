# Code written by : Hem Raj Regmi (sangamsyabil@gmail.com) http://hemrajregmi.com
# github repository: https://github.com/sangamsyabil/Learn_python_byExamples
# this program instructs the basic class creation, class instance creation and attribute assertion

class Employee:
    "This is the common base class for all the employees"
    empCount = 0 #Class variable whose value is shared among the instances of a class.

    def __init__(self, name, salary): #A special method, which is called class constructor or initialization method that Python calls when you create a new instance of this class.
        self.name = name
        self.salary = salary
        Employee.empCount +=1

    def displayCount(self):
        print("Total Employee = %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name:", self.name,", Salary: $", self.salary)

#Now creating Instance Objects - You call the class name and pass in whatever arguments its __init__ method accepts.
emp1 = Employee("Mohammad", 300)
emp2 = Employee("Stephinie", 250)
emp3 = Employee("Mannim", 350)

#Now accessing the attributes using the dot operator with object.
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
print("Total Employee = %d" % Employee.empCount)

#Happy Coding!!!