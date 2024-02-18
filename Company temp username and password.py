#!/usr/bin/env python
# coding: utf-8

# # Company temp username and password
# we want to create functions to generate temp username and password for employees

# ### username
# we want function to generate user name, that uses first 3 letters of first name and 4 first letters of last name
# if name is shorter than 3 use the fullname and if the last name is shorter than 4 letters use full lastname

# In[1]:


def username_generator(first_name, last_name):
  user_name = ""
  if (len(first_name) < 3) and (len(last_name) < 4):
    user_name = first_name + last_name
  elif (len(first_name) < 3):
    user_name = first_name + last_name[:4]
  elif len(last_name) < 4:
    user_name = first_name[:3] + last_name
  else:
    user_name = first_name[:3] + last_name[:4]
  
  return user_name


# In[3]:


# test function
first_name = "Abe"
last_name = "Simpson"

username_generator(first_name, last_name)


# ### password
# generate password that uses username and shift all of the letters by one to the right, so the last letter of the username ends up as the first letter and so forth

# In[14]:


def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password
    print(password)


# In[15]:


password_generator("AbeSimp")

