#!/usr/bin/env python
# coding: utf-8

# # username generator
# write a function to generate user name with first 3 letters of first name and first 3 letters of last name

# In[1]:


def account_generator(first_name, last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name


# In[2]:


# random first and last name
first_name = "Julie"
last_name = "Blevins"


# In[3]:


# test function
new_account = account_generator(first_name, last_name)
print(new_account)


# In[ ]:




