# Code written by : Hem Raj Regmi (sangamsyabil@gmail.com) http://hemrajregmi.com
# github repository: https://github.com/sangamsyabil/Learn_python_byExamples
''' Instead of starting from a scratch, you can create a class by deriving it from
a pre-existing class by listing the parent class in parenthesis after the new class name.'''

class Parent: #define parent class
    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print("Calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent Attribute :", Parent.parentAttr)

class Child(Parent): #define child class
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print("Calling child method")

c = Child() #instance of child
c.childMethod() #child calls its method
c.parentMethod() #calls parent's method
c.setAttr(200) #again call parent's method
c.getAttr() #again call parent's method

#Happy Coding!!!
