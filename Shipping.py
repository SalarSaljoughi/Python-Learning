#!/usr/bin/env python
# coding: utf-8

# # Shipping Company
# checking which option is cheaper

# In[ ]:


weight = 8


# In[ ]:


# ground shipping
if weight <= 2:
  cost_ground = 20 + (weight * 1.5)
elif 2 < weight <= 6:
  cost_ground = 20 + (weight * 3)
elif 6 < weight <= 10:
  cost_ground = 20 + (weight * 4)
else:
  cost_ground = 20 + (weight * 4.75)  

print("Ground Shipping $", cost_ground)


# In[ ]:


# Premium ground shipping
cost_ground_premium = 125.00

print("Ground Shipping Premimium $", cost_ground_premium)


# In[ ]:


# drone shipping
if weight <= 2:
 cost_drone = weight * 4.5
elif 2 < weight <= 6:
 cost_drone = weight * 9
elif 6 < weight <= 10:
 cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

print("Drone Shipping: $", cost_drone)


# In[ ]:




