#!/usr/bin/env python
# coding: utf-8

# # Customer List

# In[ ]:


#create list of first name
first_names = ["Ainsley", "Ben", "Chani", "Depak"]
print(fist_names)


# In[ ]:


# create list of perferred sizes
preferred_size = ["Small", "Large", "Medium"]
print(preferred_size)


# In[ ]:


# add size for Depak
preferred_size.append("Medium")
print(preferred_size)


# In[ ]:


# creating 2D List
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)


# In[ ]:


# change Chani shipping method to False
customer_data[2][-1] = False

# remove the shipping method for Ben
# customer_data[1].remove(customer_data[1][2])
customer_data[1].remove(False)

print(customer_data)


# In[ ]:


# adding new customers
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)


# In[ ]:




