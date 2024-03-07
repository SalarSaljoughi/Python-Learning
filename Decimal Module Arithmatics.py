#!/usr/bin/env python
# coding: utf-8

# # Decimal number calculations
# arithmatic calculations using decimal module

# In[2]:


# Import Decimal below:
from decimal import Decimal


# In[4]:


# arithmatic calculations using python's builtin function
two_decimal_points = 0.2 + 0.69
print(two_decimal_points)


# In[5]:


four_decimal_points = 0.53 * 0.65
print(four_decimal_points)


# In[6]:


# arithmatic operation using decimal module
two_decimal_points_a = Decimal('0.10') + Decimal('0.69')
print(two_decimal_points_a)


# In[7]:


four_decimal_points_a = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points_a)


# In[ ]:




