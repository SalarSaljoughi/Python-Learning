#!/usr/bin/env python
# coding: utf-8

# # Python Challenges - Functions

# ### tenth power
# calculate the tenth power of input

# In[1]:


# Write your tenth_power function here:
def tenth_power(num):
  return num ** 10


# In[2]:


# test function
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024


# ### square root
# calculate the square root of the input

# In[3]:


# Write your square_root function here:
def square_root(num):
  return num ** 0.5


# In[4]:


# test function
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10


# ### win percentage
# calculate the percentage of games won

# In[5]:


# Write your win_percentage function here:
def win_percentage(wins, losses):
  return (wins / (wins + losses)) * 100 


# In[6]:


# test function
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100


# ### average
# calculate the average of 2 functions

# In[7]:


# Write your average function here:
def average(num1, num2):
  return (num1 + num2) / 2


# In[8]:


# test function
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0


# ### remainder
# calculate the remainder of twice the first number divided by half of second number

# In[9]:


# Write your remainder function here:
def remainder(num1, num2):
  return (2 * num1) % (num2 / 2)


# In[10]:


# test functions
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0


# ### first three multiples

# In[11]:


# Write your first_three_multiples function here
def first_three_multiples(num):
  print(1 * num)
  print(2 * num)
  print(3 * num)
  return 3 * num


# In[12]:


# test fucntion
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0


# ### tip

# In[13]:


# Write your tip function here:
def tip(total, percentage):
  return (total * percentage) / 100


# In[14]:


# test
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0


# ### Bond, James Bond
# recreating famous movie with our own text

# In[15]:


# Write your introduction function here:
def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name


# In[16]:


# test function
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou


# ### dog years

# In[17]:


# Write your dog_years function here:
def dog_years(name, age):
  dog_years = age * 7
  return name + "," + " you are " + str(dog_years) + " years old in dog years"


# In[18]:


# test functions
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"


# ### all operations

# In[19]:


# Write your lots_of_math function here:
def lots_of_math(a, b, c, d):
  first = a + b
  second = c - d
  third = first * second
  fourth = third % a
  print(first)
  print(second)
  print(third)
  return fourth


# In[20]:


# test function
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0

