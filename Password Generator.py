#!/usr/bin/env python
# coding: utf-8

# # password generator
# create a function that generates temporary password with last 3 digits of first name and last name

# In[5]:


# define the function
def password_generator(fist_name, last_name):
  temp_pass = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return temp_pass


# In[6]:


# random name
first_name = "Reiko"
last_name = "Matsuki"


# In[7]:


# test function
temp_password = password_generator(first_name, last_name)
print(temp_password)


# In[ ]:




