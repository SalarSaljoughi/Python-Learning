#!/usr/bin/env python
# coding: utf-8

# # Hacking the Fender
# The Fender, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords including your own. Your mission, should you choose to accept it, is threefold. You must acquire access to The Fender‘s systems, you must update his "passwords.txt" file to scramble the secret data. The last thing you need to do is add the signature of Slash Null, a different hacker whose nefarious deeds could be very conveniently halted by The Fender if they viewed Slash Null as a threat.

# In[1]:


import csv
import json


# In[2]:


# create empty list for compormised passwords
compromised_users = []


# In[3]:


# open the csv file and get list of usernames whom passwords are compermised
with open("passwords.csv") as password_file:
    password_csv = csv.DictReader(password_file)
    for row in password_csv:
        password_row = row
#       print(password_row["Username"])
        compromised_users.append(password_row["Username"])
    
print(compromised_users)


# In[4]:


# we need to open a text file and write these usernames into text file
with open("compromised_users.txt", "w") as compromised_user_file:
    for name in compromised_users:
        compromised_user_file.write(name + "\n")


# In[5]:


# Your boss needs to know that you were successful in retrieving that compromised data. We’ll need to send him an encoded message over the internet. Let’s use JSON to do that.
# we already imported JSON module 
with open("boss_message.json", "w") as boss_message:
    boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
    json.dump(boss_message_dict, boss_message)


# In[19]:


# Enemy of the people, Slash Null, is who we want The Fender to think was behind this attack. He has a signature, whenever he hacks someone he adds this signature to one of the files he touches. Here is the signature:
slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
 
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""

print(slash_null_sig)


# In[21]:


# Now that we’ve safely recovered the compromised users we’ll want to remove the "passwords.csv" file completely.
with open("new_password.csv", "w") as new_password_obj:
    new_password_obj.write(slash_null_sig)


# In[ ]:




