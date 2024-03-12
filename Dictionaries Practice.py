#!/usr/bin/env python
# coding: utf-8

# # Dictionary
# ### creating and updating dicts

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


# ### Dict Comprehensions

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


# ### get a key

# In[12]:


building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

print(building_heights["Burj Khalifa"])
print(building_heights["Ping An"])


# In[13]:


# if we want to access a  key that does not exist in a dictionary we get an error to avoid we can use if statement
key_to_check = "Landmark 81"

if key_to_check in building_heights:
  print(building_heights["Landmark 81"])


# ### .get( ) method

# In[14]:


# Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. If the key you are trying to .get() does not exist, it will return None by default.

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

#this line will return 632:
print(building_heights.get("Shanghai Tower"))

#this line will return None:
print(building_heights.get("My House"))

# You can also specify a value to return if the key doesn’t exist. For example, we might want to return a building height of 0 if our desired building is not in the dictionary
print(building_heights.get('Shanghai Tower', 0))
print(building_heights.get('Mt Olympus', 0))
print(building_heights.get('Kilimanjaro', 'No Value'))


# ### delete a key

# In[4]:


# to delete a key, we can use .pop() method
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

print(raffle.pop(320291, "No Prize"))
print(raffle)


# In[6]:


print(raffle.pop(320291, "No Prize"))
print(raffle.pop(100000, "No Prize"))
print(raffle.pop(872921, "No Prize"))

print(raffle)


# ### get all keys

# In[7]:


# we can access list of all keys using .list() method
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

print(list(test_scores))


# In[8]:


# also there is .keys() method which returns a dict_keys object that we can itterate. you can not add or remove elements from dict_keys object

for student in test_scores.keys():
    print(student)


# ### get all values

# In[9]:


# we can use .valus() method to create dict_values object that we can itterate.

for score in test_scores.values():
    print(score)


# ### get all values

# In[10]:


# we can get both keys and values using .item() method which returns dict_list object. each element of the dict_list is a tuple (key, value)

biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
 print(company + " has a value of " + str(value) + " billion dollars. ")

