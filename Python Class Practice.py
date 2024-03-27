#!/usr/bin/env python
# coding: utf-8

# # Python Class Practice

# ### creating class

# In[1]:


class Facade:
    pass


# ### instantiation

# In[2]:


class Facade:
    pass

facade_1 = Facade()


# ### OOP

# In[3]:


class Facade:
    pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)


# ### class variables

# In[4]:


class Grade:
    minimum_passing = 65


# ### class methods

# In[5]:


class Rules:
    def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."


# ### class methods with arguments
# It’s March 14th (known in some places as Pi day) at Jan van High, and you’re feeling awfully festive. You decide to create a program that calculates the area of a circle.

# In[6]:


class Circle:
    pi = 3.14
  
    def area(self, radius):
        return Circle.pi * radius ** 2


# In[7]:


# create instance of circle
circle = Circle()

pizza_area = circle.area(12/2)
print(pizza_area)

teaching_table_area = circle.area(36/2)
print(teaching_table_area)

round_room_area = circle.area(11460/2)
print(round_room_area)


# ## Coonstructors

# In[8]:


# There are several methods that we can define in a Python class that have special behavior. These methods are sometimes called “magic,” because they behave differently from regular methods. 
# Another popular term is dunder methods, so-named because they have two underscores (double-underscore abbreviated to “dunder”) on either side of them.
# Methods that are used to prepare an object being instantiated are called constructors.


# ### __init__

# In[9]:


# __init__  This method is used to initialize a newly created object. It is called every time the class is instantiated.
class Shouter:
    def __init__(self):
        print("HELLO?!")

shout1 = Shouter()

shout2 = Shouter()

# Above, we created a class called Shouter and every time we create an instance of Shouter the program prints out a shout.


# ### adding the parameters

# In[10]:


class Circle:
    pi = 3.14
  
    # Add constructor here:
    def __init__(self, diameter):
        print(f"New circle with diameter: {diameter}")


teaching_table = Circle(36)


# ### instance variable

# In[11]:


# The data held by an object is referred to as an instance variable. Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to.

class Store:
    pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"


# ### attribute functions

# In[12]:


# instance variables and class variables are both accessed similarly in Python.
# they are both considered attributes of an object. 
# If we attempt to access an attribute that is neither a class variable nor an instance variable of the object Python will throw an AttributeError.

# if we are not sure if an object has an attribute or not we can use hasattr() and if it returns True object has a given attribute and False otherwise.
# If we want to get the actual value of the attribute, getattr() is a Python function that will return the value of a given object and attribute.
# we can also supply a third argument that will be the default if the object does not have the given attribute.
    # hasattr(object, “attribute”)
    # getattr(obkect, "attribute", default)
    
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
    if hasattr(element, "count") == True:
        print(str(type(element)) + " has the count attribute!")
    else:
        print(str(type(element)) + " does not have the count attribute :(")


# ### self

# In[13]:


# we can use class instead of dictionary
class Circle:
    pi = 3.14
    def __init__(self, diameter):
        print(f"Creating circle with diameter {diameter}")
        # we usually have the diameter so we need to calculate the radius for calculations
        self.radius = diameter / 2
    
    # define a method to calculate the circumference
    def circumference(self):
        return 2 * self.pi * self.radius


# In[14]:


# medium pizza
medium_pizza = Circle(12)
print(Circle.circumference(medium_pizza))
# teaching_table
teaching_table = Circle(36)
print(Circle.circumference(teaching_table))
# Round room auditorum
round_room = Circle(11460)
print(Circle.circumference(round_room))


# ### objects

# In[15]:


print(dir(5))

def this_function_is_an_object(name):
    print(f"Helle my name is {name}")

print(dir(this_function_is_an_object))


# ### string representation
# init is default string representation gives us some information, like where the class is defined and our computer’s memory address where this object is stored, but is usually not useful information to have when we are trying to debug our code. to represent the string we use __repr__()

# In[16]:


class Circle:
    pi = 3.14
  
    def __init__(self, diameter):
        self.radius = diameter / 2
  
    def area(self):
        return self.pi * self.radius ** 2
  
    def circumference(self):
        return self.pi * 2 * self.radius

    def __repr__(self):
        return f"Circle with radius {self.radius}"

  
medium_pizza = Circle(12)
print(medium_pizza)

teaching_table = Circle(36)
print(teaching_table)

round_room = Circle(11460)
print(round_room)


# ## Review and Practice

# In[17]:


# create a class called student and create cunstructor with 2 parameters and add as attribute

# first version
# class Student():
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
        
# adjusted version
class Student():
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.score = []
        
    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grade.append(grade)
    


# In[18]:


# Create three instances of the Student class:

    # Roger van der Weyden, year 10
    # Sandro Botticelli, year 12
    # Pieter Bruegel the Elder, year 8

roger = Student("Roger van der Weyden", 10)

sandro = Student("Sandro Botticelli", 12)

pieter = Student("Pieter Bruegel the Elder", 8)


# In[19]:


# define a new class for scores and set the min score to 65

class Grade():
    minimum_passing = 65
    def __init__(self, score):
        self.score = score


# In[20]:


# update the class Student to have new attribute score and set it to empty list
# Add an .add_grade() method to Student that takes a parameter, grade.
    # .add_grade() should verify that grade is of type Grade and if so, add it to the Student‘s .grades.
    # If grade isn’t an instance of Grade then .add_grade() should do nothing.

class Student():
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.score = []
        
    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)


# In[23]:


# Create a new Grade with a score of 100 and add it to pieter‘s .grades attribute using .add_grade().
pieter.add_grade(100)
print(pieter)


# In[ ]:





# In[ ]:





# In[ ]:




