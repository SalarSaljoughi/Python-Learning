#!/usr/bin/env python
# coding: utf-8

# # Python Challenge - Functions and Lists

# ### append size
# calculate the size of the list and append it to the list. then return the new list

# In[1]:


#Write your function here
def append_size(my_list):
  my_list.append(len(my_list))
  return my_list


# In[2]:


# test function
print(append_size([23, 42, 108]))


# ### append sum
# add last 2 elements of the list and add it to list and repeat the process 2 more times and return the list at the end

# In[6]:


# Write your function here
def append_sum(my_list):
  for i in range(3):
    my_list.append(my_list[-1] + my_list[-2])
    i += 1
  return my_list


# In[7]:


# test function
print(append_sum([1, 1, 2]))


# ### larger list
# return the last element of list that has more elements, if their are same length return last element of first list

# In[10]:


# Write your function here
def larger_list(my_list1, my_list2):
  if len(my_list1) >= len(my_list2):
    return my_list1[-1]
  else:
    return(my_list2[-1])


# In[11]:


# test function
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))


# ### more than n
# check if item apears more than n times in the list then return True otherwise return False

# In[12]:


# Write your function here
def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  else:
    return False


# In[13]:


# test function
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


# ### combine sort
# combine 2 list and sort it and return the sorted list

# In[14]:


# Write your function here
def combine_sort(my_list1, my_list2):
  new_list = my_list1 + my_list2
  new_list.sort()
  return new_list


# In[15]:


# test function
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))


# ### every 3 number
# create a list of every 3 number from user input number to 100 (100 is inclusive)

# In[18]:


# Write your function here
def every_three_nums(start):
  return list(range(start, 101, 3))


# In[19]:


# test function
print(every_three_nums(91))


# ### remove middle
# Our next function will remove all elements from a list with an index within a certain range.

# In[ ]:


# Write your function here
def remove_middle(my_list, start, end):
  return my_list[:start] + my_list[end+1:]


# In[ ]:


# test function
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


# ### more frequent item
# check which item on the list is more frequent

# In[ ]:


# Write your function here
def more_frequent_item(my_list, item1, item2):
  if my_list.count(item1) > my_list.count(item2):
    return item1
  else:
    return item2


# In[ ]:


# test function
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


# ### double index
# We will provide a list and an index to double. This will create a new list by replacing the value at the index provided with double the original value.

# In[ ]:


# Write your function here
def double_index(my_list, index):
  # Checks to see if index is too big
  if index >= len(my_list):
    return my_list
  else:
    # Gets the original list up to index
    my_new_list = my_list[0:index]
 # Adds double the value at index to the new list 
  my_new_list.append(my_list[index]*2)
  #  Adds the rest of the original list
  my_new_list = my_new_list + my_list[index+1:]
  return my_new_list


# In[ ]:


# test function
print(double_index([3, 8, -10, 12], 2))


# ### middle element
# the function will find middle element of the list. This will be different depending on whether there are an odd or even number of values. 

# In[ ]:


#Write your function here
def middle_element(my_list):
  if len(my_list) % 2 == 0:
    sum = my_list[int(len(my_list)/2)] + my_list[int(len(my_list)/2) - 1]
    return sum / 2
  else:
    return my_list[int(len(my_list)/2)]


# In[ ]:


# test function
print(middle_element([5, 2, -10, -4, 4, 5]))


# In[ ]:




