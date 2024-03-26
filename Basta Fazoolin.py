#!/usr/bin/env python
# coding: utf-8

# # Basta Fazoolin'
# You’ve started a position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart. The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized.

# #### create and define class

# In[1]:


# # the restaurant decided to expand, create a new class called Franchise
# # the flagship store has address "1232 West End Road" and new installment store address is "12 East Mulberry Street"

# class franchise():
#     def __init__(self, address, menus):
#         self.address = address
#         self.menus = menus
    
#     # give franchise a string representation of the address
#     def __repr__(self):
#         return self.address
    
#     # add new mothod to show customers what they can order
#     def available_menus(self, time):
#         available_menus = []
#         for menu in self.menus:
#             if time >= menu.start_time and time <= menu.end_time:
#                 available_menus.append(menu)
        
#         return available_menus


# #### create and define class

# In[2]:


# We have four different menus: brunch, early-bird, dinner, and kids. create class Menu

class Menu():
    # constructor
    # Give Menu a constructor with the five parameters self, name, items, start_time, and end_time.
    
    def __init__(self, name, items, start_time, end_time):
    # Now, you need to assign the parameters of the constructor to the corresponding class attributes.
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    # give string representation to show the name and when is the menu available
    def __repr__(self):
        return f"{self.name} menu available from {self.start_time} to {self.end_time}"
    
    # create new method that takes purchased items and calculates the bill
    def calculate_bill(self, purchased_items):
        bill = 0
        for items in purchased_items:
            if items in self.items:
                bill += self.items[items]
        return bill


# #### create brunch menu

# In[3]:


# lest create brunch menu which served from 11 AM to 4 PM with following items
# {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
# for time we are going to use 24 hour military time

brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)

# test
print(brunch_menu.name)


# #### create early bird menu

# In[4]:


# early bird menu served from 3 PM to 6 PM with following items
# {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}

early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}

early_bird_menu = Menu("Early_Bird", early_bird_items, 1500, 1800)

# test
print(early_bird_menu.items)


# #### create dinner menu

# In[5]:


# dinner menu served from 5 PM to 11 PM with following items
# {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}

dinner_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}

dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)

# test
print(dinner_menu.start_time)


# #### create kids menu

# In[6]:


# kids menu available from 11 AM to 9 PM with following items
# {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

kids_menu = Menu("Kids", kids_items, 1100, 2100)

# test 
print(kids_menu.end_time)


# #### add string representation 

# In[7]:


# in this step we want to add string representation to our class that shows the menu and when is the menu available.
# see main class

print(brunch_menu)
print(early_bird_menu)
print(dinner_menu)
print(kids_menu)


# #### add new method

# In[8]:


# add new method that calculate the bill with list of purchased items
# see the main class 

# we have brunch order of pancakes, home fries and coffee. 
print(brunch_menu.calculate_bill(["pancakes", "home fries", "coffee"]))

# we have early bird order of salumeria plate and mushroom ravioli
print(early_bird_menu.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))


# #### expanding

# In[17]:


# the restaurant decided to expand, create a new class called Franchise
# the flagship store has address "1232 West End Road" and new installment store address is "12 East Mulberry Street"

class Franchise():
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    
    # give franchise a string representation of the address
    def __repr__(self):
        return self.address
    
    # add new mothod to show customers what they can order
    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menus.append(menu)
        
        return available_menus
        
    
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

print(flagship_store)
print(new_installment)


# #### get address and available menu

# In[18]:


# in franchise class add string representation to show the address
# see the main class for details

# give franchise class a new method called available_menus to show customers what they can order based on when they want to order
# see main class for details

# test
print(flagship_store.available_menus(1200))
print(new_installment.available_menus(1700))


# #### create businesses

# In[19]:


# since we are sucessfull building out branded chain of restaurants, we want to expand and create a restaurant taht sells arepas!
# create new class called business and add constructors name and franchises

class Business():
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


# In[20]:


# lets create our first business calles "Basta Fazoolin' with my Heart" and 2 franchises are flagship store and new isntallment store

basta = Business("Basta Fazoolin' with my Heart", ["flagship_store", "new_installment"])


# #### create new business

# In[23]:


# to create a new business we need a franchise and before franchise we need a menu
# create new business called " Take a' Arepa" which is available from 10am to 8pm with following menu
# {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
# the branch is located at "189 Fitzgerald Avenue" called arepas_place

arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

arepas_menu = Menu("Take a' Arepa", arepa_items, 1000, 20000)

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

arepa = Business("Take a' Arepa", [arepas_place])

# test
print(arepa.franchises[0])
print(arepa.franchises[0].menus[0])


# In[ ]:




