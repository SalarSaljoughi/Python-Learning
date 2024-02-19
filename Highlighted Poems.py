#!/usr/bin/env python
# coding: utf-8

# # Highlighted Poems
# imagine we have a giant strings that has poets, titles and dates

# In[1]:


highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print(highlighted_poems)


# In[2]:


# first we need to seprate them

print(highlighted_poems)
highlighted_poems_list = highlighted_poems.split(",")
print(highlighted_poems_list)


# In[3]:


# as you can see there are a lot of whitespaces, lets remove them

highlighted_poems_stripped = []
for items in highlighted_poems_list:
  highlighted_poems_stripped.append(items.strip())
print(highlighted_poems_stripped)


# In[4]:


# now to access to each poet and details we need to seprate them by :

highlighted_poems_details = []
for details in highlighted_poems_stripped:
  highlighted_poems_details.append(details.split(":"))
print(highlighted_poems_details)


# In[5]:


# now we need to seprate the poets, titles and dates into their own list

titles = []
poets = []
dates = []

for items in highlighted_poems_details:
  titles.append(items[0])
  poets.append(items[1])
  dates.append(items[2])

print(titles)
print(poets)
print(dates)


# In[8]:


# finally we want to print this using .format
# The poem TITLE was published by POET in DATE.

for i in range(len(poets)):
    print(f"The poem {titles[i]} was published by {poets[i]} in {dates[i]}")


# In[ ]:




