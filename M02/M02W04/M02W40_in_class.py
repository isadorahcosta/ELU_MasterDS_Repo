# -*- coding: utf-8 -*-
"""
@author: Ceccato Rudy
Created on Thu Dec 30 14:37:54 2021 

M2- W4 Assignment

Due Sunday by 02/01/2022 at 10:00 

Step 1: Write a class of “Person”, which is the parent class of Lecturer and Student. 
        The Student and Lectures classes inherit from the Person class. 
        In this class, the instance attributes should be number of legs, 
        which should be initialised 2 and a boolean variable - 
        is_alive, that should be initialised as True. 

Step 2: Write a class 'Student' which stores information about a student. 
        The class must have the following instance attributes 
        controlled by the user: 
        Name, Grade, Number.

Step 3: Write a class which stores information about a “Lecturer”. 
        The class must have the following instance attributes, 
        also controlled by the user: 
        Name, Number

In Step 2 and Step 3, both object should inherit the instance attributes 
from the Person object.

Hint: super().<name of the method you want to call from parent class>()

Submit your Python file or Jupyter notebook. 
"""
####NOTE: using multilevel inheritance - Granparent  -> Parent -> Children structure
####as it seemed more efficient in this context
class Person():
    def __init__(self,  num_of_legs=2, is_alive=True):
        self.num_of_legs = num_of_legs
        self.is_alive = is_alive

class Student(Person):
    def __init__(self, first_name, last_name,  id_number, grade=7, num_of_legs=2, is_alive=True):
        super().__init__(num_of_legs, is_alive)
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number 
        self.grade = grade
        
####using multilevel inheritance
class Lecturer(Student):
    def __init__(self, first_name, last_name, id_number, grade=None, num_of_legs=2, is_alive=True):
        Person.__init__(self, num_of_legs, is_alive)
        Student.__init__(self, first_name, last_name, id_number, grade)



###TESTING####
####Person class####
person00 = Person()
print('\n''########',"Testing PERSON class data: ########")
print(person00.num_of_legs, "&", person00.is_alive)
person00.num_of_legs = 1
person00.is_alive = False
print(person00.num_of_legs, "&", person00.is_alive)

####Student class####
student00 = Student("John", "Smith", 123456, 7)
##testing inheritance
print('\n''########',"Testing STUDENT class inherited data: ########")
print("Accessing 'leg#' from within Student:", student00.num_of_legs)
print("Accessing 'alive?' from within Student:", student00.is_alive)
student00.num_of_legs = 1
student00.is_alive = False
print("Modified 'leg#' from within Student:", student00.num_of_legs)
print("Modified 'alive?' from within Student:", student00.is_alive)

##testing class own data
print('\n',"Testing STUDENT class own data:" )
print("Accessing 'first name' from within Student:", student00.first_name)
print("Accessing 'last name' from within Student:", student00.last_name)
print("Accessing 'grade' from within Student:", student00.grade)
print("Accessing 'id#' from within Student:", student00.id_number)
##modifying class own data
student00.first_name="Jenny"
student00.last_name = "Smith Rosendal"
student00.grade = 8
student00.id_number = 7654321
print('\n',"Modifying STUDENT class own data:")
print("Modified 'first name' from within Student:", student00.first_name)
print("Modified 'last name' from within Student:", student00.last_name)
print("Modified 'grade' from within Student:", student00.grade)
print("Modified 'id#' from within Student:", student00.id_number)

# ####Lecturer class####
lecturer00 = Lecturer("Keanu", "Reeves", 10100101)
##testing inheritance
print('\n''########',"Testing LECTURER class inherited data: ########")
print("Accessing 'leg#' from within Lecturer:", lecturer00.num_of_legs)
print("Accessing 'alive?' from within Lecturer:", lecturer00.is_alive)
lecturer00.num_of_legs = 1
lecturer00.is_alive = False
print("Modified 'leg#' from within Lecturer:", lecturer00.num_of_legs)
print("Modified 'alive?' from within Lecturer:", lecturer00.is_alive)

##testing class own data
print('\n',"Testing LECTURER class own data:")
print("Accessing 'first name' from within Lecturer:", lecturer00.first_name)
print("Accessing 'last name' from within Lecturer:", lecturer00.last_name)
print("Accessing 'id#' from within Lecturer:", lecturer00.id_number)
##modifying class own data
lecturer00.first_name="Trinity"
lecturer00.last_name = "Holy"

lecturer00.id_number = 1010000101
print('\n',"Modifying LECTURER class own data:")
print("Modified 'first name' from within Lecturer:", lecturer00.first_name)
print("Modified 'last name' from within Lecturer:", lecturer00.last_name)
print("Modified 'id#' from within Lecturer:", lecturer00.id_number)

