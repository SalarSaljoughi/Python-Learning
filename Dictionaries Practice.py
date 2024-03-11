#!/usr/bin/env python
# coding: utf-8

# # Dictionary

# In[1]:


# dictionaries are key: value pairs
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

print(sensors)
print(num_cameras)


# In[2]:


# create empty dictionary
animals_in_zoo = {}


# In[3]:


# add new key_value pair
animals_in_zoo["zebras"] = 8

print(animals_in_zoo)


# In[7]:


# if want to add multiple keys at once we can use .update() method
animals_in_zoo.update({"monkeys": 12, "dinosaurs": 0})

print(animals_in_zoo)


# In[8]:


# overwrite existing value
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)


# # Dict Comprehensions

# In[9]:


# if we have 2 lists that we want to combine into a dictionary

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {key:value for key, value in zip(names, heights)}
print(students)


# In[10]:


# dictionaries can't have duplicate keys. if during list comprehension, first list has duplicate element, it will be overwritten in the process

# if we have 2 lists that we want to combine into a dictionary
cities = ["New York", "London", "Sydney", "New York"]
temps = [ 85, 81, 65, 99]

weather = { key:value for key,value in zip(cities, temps)}

print(weather)


# In[ ]:




