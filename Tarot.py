#!/usr/bin/env python
# coding: utf-8

# # Tarot

# In[1]:


tarot = { 1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor", 5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice", 12: "The Hanged Man", 13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star", 18:	"The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}


# In[2]:


# we are going to do a three card spread of your past, present, future
# create empty dictionary called spread

spread = {}


# In[3]:


# the first card we draw is card 13, pop the value and assign it as value to key "past" in spread dictionary
spread["past"] = tarot.pop(13, 0)

print(spread)


# In[4]:


# the second card you draw is card 22. pop the value and assign it as value to key "present" in spread dictionary
spread["present"] = tarot.pop(22, 0)

print(spread)


# In[5]:


# the third card you draw is card 10. pop the value and assign it as value to key "future" in spread dictionary
spread["future"] = tarot.pop(10, 0)

print(spread)


# In[6]:


# itterate through the items in spread dictionary and print the statement

for time, card in spread.items():
    print(f"your {time} is the {card} card.")

