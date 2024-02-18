#!/usr/bin/env python
# coding: utf-8

# # Carly's Clippers

# In[1]:


# we are data analyst at Carly's hair salon and we need to do some analysis
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]


# In[2]:


# calculating average haircut price
total_price = 0
for price in prices:
  total_price += price
print(total_price)

average_price = total_price / len(prices)
print(average_price)

print("Average Haircut Price: " + str(average_price))


# In[4]:


# That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.
# create new_prices list using list comprehension

new_prices = [num - 5 for num in prices]
print(new_prices)


# In[8]:


# calculate hair salon revenue for last week
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print(total_revenue)

print("Total Revenue: " + str(total_revenue))


# In[9]:


# average daily revenue
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)


# In[14]:


# Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)


# In[ ]:




