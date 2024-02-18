#!/usr/bin/env python
# coding: utf-8

# # Common Letters
# write a function to find common letters in 2 words and return them (avoid duplicates)

# In[1]:


def common_letters(string_one, string_two):
  list = []
  for letter in string_one:
    if (letter in string_two) and not (letter in list):
      list.append(letter)
  return list


# In[2]:


# test function
common_letters("banana", "cream")


# In[3]:


# test function
common_letters("Manhattan", "Manchester")

