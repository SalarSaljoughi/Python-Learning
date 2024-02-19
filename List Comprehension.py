#!/usr/bin/env python
# coding: utf-8

# # List comprehension practice

# In[1]:


# create a list consists of the numbers 0-9 (inclusive).
single_digits = list(range(10))
print(single_digits)


# In[2]:


# create empty list called squares and calculate the squares using for loop
squares = []

for digit in single_digits:
  print(digit)
  squares.append(digit ** 2)
print(squares)


# In[3]:


# create new list called cubes and calculate cubes using list comprehension

cubes = [digit ** 3 for digit in single_digits]
print(cubes)


# In[ ]:




