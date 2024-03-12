#!/usr/bin/env python
# coding: utf-8

# # Scrabble
# 
# we will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.

# In[1]:


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


# In[6]:


# we want to combine 2 list into a dictionary and map leeter to its point value

letter_to_point = {key:value for key,value in zip(letters, points)}

print(letter_to_point)


# In[9]:


# our letters list did not take into account blank tiles, add " " with value zero to dictionary
letter_to_point.update({" ": 0})

print(letter_to_point)


# In[21]:


# we want to define a function to take in the word and return how many points that word is worth

def score_word(word):
    point_total = 0
    for letter in word:
        if letter in letter_to_point:
            point_total += letter_to_point[letter]
        else:
            point_total += 0
            
    return point_total


# In[23]:


# test function
brownie_points = score_word("BROWNIE")
print(brownie_points)


# In[25]:


# create dictionary player_to_words 
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

# create empty dictionary player_to_points
player_to_points = {}


# In[28]:


# calculate each players points
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points


# In[29]:


# test to see if everything is correct
print(player_to_points)


# #### additional tasks 
# If you want extended practice, try to implement some of these ideas with the Python you’ve learned:
# 
# play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played
# 
# update_point_totals() — turn your nested loops into a function that you can call any time a word is played
# 
# make your letter_to_points dictionary able to handle lowercase inputs as well
