#!/usr/bin/env python
# coding: utf-8

# # Python Challenges - Functions and if statements

# ### Over budget

# In[1]:


# Monthly budget
budget = 2000


# In[2]:


# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500


# In[3]:


# Calculate the total amount of expenses
total = food_bill + electricity_bill + internet_bill + rent


# In[4]:


# Check if the total is greater than the budget and store the result in over_budget
if total > budget:
  over_budget = True
else:
  over_budget = False


# In[5]:


print("Total: " + str(total))
print("Is it over budget? " + str(over_budget))


# ### large power

# In[25]:


# Write your large_power function here:
def large_power(base, exponent):
    number = base ** exponent
    if number > 5000:
        return True
    else:
        return False


# In[26]:


# testing the functions
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False


# ### Twice as large

# In[27]:


# Write your twice_as_large function here:
def twice_as_large(num1, num2):
  if num1 > 2 * num2:
    return True
  else:
    return False


# In[28]:


# test function
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True


# ### Divisible by 10

# In[29]:


# Write your divisible_by_ten() function here:
def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False


# In[30]:


# test the function
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False


# ### In Range

# In[31]:


# Write your in_range function here:
def in_range(num, lower, upper):
  if num >= lower and num <= upper:
    return True
  else:
    return False


# In[32]:


# test function
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False


# ### Same Name

# In[33]:


# Write your same_name function here:
def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
    return False


# In[34]:


# test function
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False


# ### Always False

# In[35]:


# Write your always_false function here:
def always_false(num):
  if num > 10 and num < 10:
    return True
  else:
    return False


# In[36]:


# test function
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False


# ### Movie Rating

# In[39]:


# Write your movie_review function here:
def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif 5 < rating < 9:
    return "This one was fun."
  else: 
    return "Outstanding!" 


# In[38]:


# test function
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."


# In[ ]:




