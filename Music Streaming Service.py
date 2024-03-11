#!/usr/bin/env python
# coding: utf-8

# # Music Streaming Service

# In[2]:


# we have 2 lists, representing songs in user's library and the amount of time each song has been played
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]


# In[3]:


# Using a dict comprehension, create a dictionary called plays that goes through zip(songs, playcounts) and creates a song:playcount pair for each song in songs and each playcount in playcounts.
plays = {key: value for key, value in zip(songs, playcounts)}

print(plays)


# In[6]:


# After printing plays, add a new entry to it. The entry should be for the song "Purple Haze" and the playcount is 1.
plays["Purple Haze"] = 1

print(plays)


# In[8]:


# This user has caught Aretha Franklin fever and listened to “Respect” 5 more times. Update the value for "Respect" to be 94 in the plays dictionary.
plays["Respect"] = 94

print(plays)


# In[10]:


# Create a dictionary called library that has two key: value pairs:
    # key "The Best Songs" with a value of plays, the dictionary you created
    # key "Sunday Feelings" with a value of an empty dictionary
    
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)


# In[ ]:




