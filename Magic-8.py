#!/usr/bin/env python
# coding: utf-8

# # Magic 8 Ball

# In[1]:


import random


# In[2]:


# creating variable
name = "Salar"
question = "Will I win the lottery?"
answer = ""


# In[3]:


# generating random number
random_number = random.randint(1, 9)
# making sure the random number works
print(random_number)


# In[4]:


# magic 8 ball logic
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now" 
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outloo not so good" 
elif random_number == 9:
  answer = "It is decidedly so"
else:
  answer = "Error"


# In[5]:


# printing the answers
print(name + " asks: " + question )
print("Magic 8-Ball's answer: " + answer)


# In[ ]:




