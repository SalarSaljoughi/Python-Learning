#!/usr/bin/env python
# coding: utf-8

# # travel 
# ### travel expenses

# In[1]:


# define the function
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = (hotel_rate * trip_time) - 10
  trip_total = car_rental_total + hotel_total + plane_ticket_price

  return trip_total


# In[2]:


# call function
print(calculate_expenses(200, 100, 100, 5))


# ### trip planner

# In[3]:


# Write your code below:
def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination )


# In[5]:


# call function with positional arguments
trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")


# In[6]:


# call functiono with keyword arguments
trip_planner(first_destination = "Iceland", final_destination = "Germany", second_destination = "India")


# In[7]:


# call function with default arguments
trip_planner("Brooklyn", "Queens")


# ### budget

# In[8]:


current_budget = 3500.75


# In[9]:


# dwfine function to print the remaining budget
def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)


# In[10]:


# Write a function to account for expense
def deduct_expense(budget, expense):
  return budget - expense


# In[11]:


# for example we buy a shirt - calculate the new budget
shirt_expense = 9

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)


# ### weather report

# In[12]:


weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']

def threeday_weather_report(weather):
  first_day = " Tomorrow the weather will be " + weather[0]
  second_day = " The following day it will be " + weather[1]
  third_day = " Two days from now it will be " + weather[2]
  return first_day, second_day, third_day


# In[13]:


monday, tuesday, wednesday = threeday_weather_report(weather_data)

print(monday)
print(tuesday)
print(wednesday)


# ## trip planner V1.0

# In[14]:


# welcome message
def trip_planner_welcome(name): 
  print("Welcome to tripplanner v1.0 " + name)

trip_planner_welcome("Salar")


# In[26]:


# calculate the estimated travel time with rounding based on a decimal
def estimated_time_rounded(estimated_time):
    rounded_time = round(estimated_time, 0)
    return rounded_time
    
estimate = estimated_time_rounded(50.55)
print(estimate)


# In[29]:


# generate messages for user's planned trip
def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
    print("Your trip starts off in " + origin)
    print("And you are traveling to " + destination)
    print("You will be traveling by " + mode_of_transport) 
    print("It will take approximately " + str(estimated_time) + " hours")
    
destination_setup("Denver", "NY", estimate)


# In[ ]:




