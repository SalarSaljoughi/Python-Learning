#!/usr/bin/env python
# coding: utf-8

# # Python Challenges - Functions and Loops

# ### Divisible by 10

# In[1]:


# Write your function here
def divisible_by_ten(nums):
  counter = 0
  for i in nums:
    if i % 10 == 0:
      counter += 1
  return counter


# In[2]:


# test function
print(divisible_by_ten([20, 25, 30, 35, 40]))


# ### Greetings
# In this challenge, we will take a list of names and prepend the string 'Hello, ' before each name.

# In[3]:


# Write your function here
def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list


# In[4]:


# test function
print(add_greetings(["Owen", "Max", "Sophie"]))


# ### Delete starting even number
# if list starts with even number, remove them till the first element of the list is off number

# In[5]:


# Write your function here
def delete_starting_evens(my_list):
  while (len(my_list) > 0 and my_list[0] % 2 == 0):
    my_list = my_list[1:]
  return my_list


# In[6]:


# test function
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


# ### odd_indicies
# get a list as input and only return the odd indicies

# In[7]:


#Write your function here
def odd_indices(my_list):
  new_list = []
  for index in range(1, len(my_list), 2):
    new_list.append(my_list[index])
  return new_list


# In[8]:


# test function
print(odd_indices([4, 3, 7, 10, 11, -2]))


# ### Exponents
# function must accept 2 lists as input and will be using nested loops in order to raise a list of numbers to the power of a list of other numbers. 

# In[9]:


# Write your function here
def exponents(bases, powers):
  new_list = []
  for i in bases:
    for j in powers:
      new_list.append(i ** j)
    i += 1
    j += 1
  return new_list  


# In[10]:


# test function
print(exponents([2, 3, 4], [1, 2, 3]))


# ### Larger Sum

# In[11]:


# Write your function here
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for item_1 in lst1:
    sum1 += item_1
  for item_2 in lst2:
    sum2 += item_2
  if sum1 == sum2:
    return lst1
  elif sum1 > sum2:
    return lst1
  else:
    return lst2


# In[12]:


# test function
print(larger_sum([1, 9, 5], [2, 3, 7]))


# ### Over 9000

# In[13]:


# Write your function here
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum


# In[14]:


# test function
print(over_nine_thousand([8000, 900, 120, 5000]))


# ### Max number

# In[15]:


#Write your function here
def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum


# In[16]:


# test function
print(max_num([50, -10, 0, 75, 20]))


# ### same value
# return the index of values that are same in 2 list

# In[17]:


#Write your function here
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst


# In[18]:


# test function
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


# ### reverse list
# checking to see if second list if reverse of the first list

# In[19]:


#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True


# In[20]:


# test function
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))


# In[ ]:




