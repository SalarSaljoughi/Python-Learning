#!/usr/bin/env python
# coding: utf-8

# # Len's Slice
# ### new pizza place in the neighborhood

# In[1]:


# to keep track of the kind of pizza you sell, create a list of toppings:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]


# In[2]:


# To keep track of how much each kind of pizza slice costs, create a list called prices
prices = [2, 6, 1, 3, 2, 7, 2]


# In[3]:


# Your boss wants you to do some research on $2 slices.

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)


# In[4]:


# Find the length of the toppings list
num_pizzas = len(toppings)
print(num_pizzas)


# In[5]:


# print a message
print("we sell " + str(num_pizzas) + " different kinds of pizza!")


# In[6]:


# create 2D list of prices and toppings
pizza_and_prices = [[2, "pepperoni"], [6, "pineapples"], [1, "cheese"], [3, "sausage"], [2, "ollives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)


# In[7]:


# sort the list in ascending order
pizza_and_prices.sort()
print(pizza_and_prices)


# In[8]:


# cheapest pizza
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)


# In[9]:


# most expensive pizza
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)


# In[10]:


# remove last index
pizza_and_prices.pop()
print(pizza_and_prices)


# In[11]:


# add new topping 
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)


# In[12]:


# three cheapest pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)


# In[ ]:




