#!/usr/bin/env python
# coding: utf-8

# ### Poem
# imagine we have a list with bunch of extra white spaces and extra lines. we need to clean our list and print the poem

# In[2]:


love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
print(love_maybe_lines)


# In[3]:


# clean the extra whitespaces

love_maybe_lines_stripped = []

for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())
print(love_maybe_lines_stripped)


# In[4]:


# joing the strings to shows each item as a new line

love_maybe_full = "\n".join(love_maybe_lines_stripped)
print(love_maybe_full)


# In[ ]:




