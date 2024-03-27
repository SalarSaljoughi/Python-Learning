#!/usr/bin/env python
# coding: utf-8

# # Python Basics
# ### print function

# In[1]:


print("Hello World!")


# ### variables

# In[2]:


# strings - Greeting
message_string = "Hello there"
print(message_string)

# Strings - Farewell
message_string = "Hasta la vista"
print(message_string)

# int & float
an_int = 2
a_float = 2.1

print(an_int + 3)


# ### calculations

# In[3]:


print(3 + 4) # Addition
print(5 - 5) # Subtraction
print(3 * 5) # Multiplication
print(12 / 4) # Division
print(3 ** 3) # Exponentiation
print(15 % 2) # Modulus
print(15 // 3) # Floor division


# In[4]:


a = 5
b = 10
print(a + b)


# ### concatination

# In[5]:


# process of combining strings called concatination
greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text

print(full_text)

full_text = greeting_text + " " + question_text

# Prints "Hey there! How are you doing?"
print(full_text)


# In[6]:


birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"

# Concatenating an integer with strings is possible if we turn the integer into a string first
full_birthday_string = birthday_string + str(age) + birthday_string_2
print(full_birthday_string)

# If we just want to print an integer we can pass a variable as an argument to print() regardless of whether it is a string.
print(birthday_string, age, birthday_string_2)


# ### updating variables

# In[7]:


# First we have a variable with a number saved
number_of_miles_hiked = 12

# Then we need to update that variable Let's say we hike another two miles today
number_of_miles_hiked += 2

# The new value is the old value Plus the number after the plus-equals
print(number_of_miles_hiked)


# In[8]:


hike_caption = "What an amazing time to walk through nature!"

# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"

print(hike_caption)


# ### multiline strings

# In[9]:


# By using three quote-marks (""" or ''') instead of one, we tell the program that the string doesn’t end until the next triple-quote. 
# This method is useful if the string being defined contains a lot of quotation marks and we want to be sure we don’t close it prematurely.

leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
"""

print(leaves_of_grass)


# ## control flow
# ### if statement

# In[10]:


# Enter a user name here, make sure to make it a string
user_name = "angela_catlady_87"

if user_name == "Dave":
  print("Get off my computer Dave!")
if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")


# In[11]:


# and logical operator
credits = 120
gpa = 3.4

if credits >= 120 and gpa >=2.0:
  print("You meet the requirements to graduate!")


# In[12]:


# or logical operator
credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")


# In[13]:


# not logical operator
credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate")
elif (not gpa >= 2.0):
  print("Your GPA is not high enough to graduate.")
else:
  print("You do not meet either requirement to graduate!")


# ## Loops
# ### for loops

# In[14]:


# With for loops, on each iteration, we will be able to perform an action on each element of the collection.
# If we ever forget to indent, we’ll get an IndentationError or unexpected behavior.


ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

for ingredient in ingredients:
  print(ingredient)


# In[15]:


# elegent way to write for loops
for ingredient in ingredients: print(ingredient)


# In[16]:


# if we want to repeat for certain amount of time we use for loop using range function
# for <temporary variable> in <list of length n>:
#   action

for temp in range(6):
    print("Learning Loops!")
    
for temp in range(6):
  print("Loop is on iteration number " + str(temp + 1))


# ### while loops

# In[17]:


# while loops are form of indefinite iteration. A while loop performs a set of instructions as long as a given condition is true.
count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1


# In[18]:


# elegent way of writing while loop
count = 0
while count <= 3: print(count); count += 1


# In[19]:


countdown = 10
while countdown >= 0:
  print(countdown)
  countdown -= 1
print("we have liftoff!")


# In[20]:


# while loops with list - first we need to fine the list length and compare
length = len(ingredients)
index = 0

while index < length:
  print(ingredients[index])
  index += 1


# ### infinite loops

# In[21]:


# A loop that never terminates is called an infinite loop. 
# my_favorite_numbers = [4, 8, 15, 16, 42]

# for number in my_favorite_numbers:
#   my_favorite_numbers.append(1)

# if we encounter infinite loop, we can terminate with control + c


# ### loop conotrol: Break

# In[22]:


items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
for item in items_on_sale:
    if item == "knit dress":
        print("Found it")
# this loop will continue even after it prints the statement, if we have many elements this is waste of time and memory    


# In[23]:


# better way to write above loop
items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

print("Checking the sale list!")

for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break

print("End of search!")


# ### loop control: Continue

# In[24]:


# continue will be used to skip current iteration of the loop
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

for i in big_number_list:
  if i <= 0:
    continue
  print(i)


# ### nested loops

# In[25]:


project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
for team in project_teams:
  print(team)


# In[26]:


# Loop through each sublist
for team in project_teams:
  # Loop elements in each sublist
  for student in team:
    print(student)


# ## Strings

# In[27]:


favorite_fruit = "blueberry"


# In[28]:


print(favorite_fruit)

# select first index
print(favorite_fruit[0])


# ### sliceing strings

# In[29]:


# string[first_index:last_index]
print(favorite_fruit[4:6])

print(favorite_fruit[:4])

print(favorite_fruit[4:])


# ### concatinating strings

# In[30]:


fruit_prefix = "blue"
fruit_suffix = "berries"
favorite_fruit = fruit_prefix + fruit_suffix

print(favorite_fruit)


# In[31]:


fruit_sentence = "My favorite fruit is" + favorite_fruit

print(fruit_sentence)
# Output: My favorite fruit isblueberries

fruit_sentence = "My favorite fruit is " + favorite_fruit

print(fruit_sentence)


# ### length of string

# In[32]:


# len() used to get the length of the function

favorite_fruit = "blueberry"

length = len(favorite_fruit)

print(length)


# In[33]:


# if we want to get last character of a long string
last_char = favorite_fruit[len(favorite_fruit)-1]

print(last_char)


# ### negative indices

# In[34]:


# we can use negative indecies to access elements
favorite_fruit = 'blueberry'
print(favorite_fruit[-1])

print(favorite_fruit[-2])

print(favorite_fruit[-3:])


# ### immutable

# In[35]:


# strings are immutable, means we can not change a string once it is created.

first_name = "Bob"
last_name = "Daily"

# correct name must be Rob Daily
# first_name[0] = R
# this results in error

# the correct way to fix this
fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)


# ### escape character

# In[36]:


# \ is escape character

favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""
print(favorite_fruit_conversation)


# ### iterating through strings

# In[37]:


def print_each_letter(word):
  for letter in word:
    print(letter)

favorite_color = "blue"
print_each_letter(favorite_color)


# ### strings and conditionals

# In[38]:


# count how many b are in a string
favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "b":
    counter += 1
print(counter)


# In[39]:


# instead of above code we can use in keyword which returns True or Flase
print("e" in "blueberry")

print("a" in "blueberry")


# In[40]:


# in keyword works with letters and also with words
print("blue" in "blueberry")

print("blue" in "strawberry")


# In[41]:


print("e" in "blueberry" and "e" in "carrot")

print("e" in "blueberry" and not "e" in "carrot")


# ### string methods

# In[42]:


# string methods only create new strings and won't change the original string
# .lower() returns the string with all lowercase characters.
# .upper() returns the string with all uppercase characters.
# .title() returns the string in title case, which means the first letter of each word is capitalized.

favorite_song = 'SmOoTH'
favorite_song_lowercase = favorite_song.lower()
fovarite_song_uppercase = favorite_song.upper()
favorite_song_title = favorite_song.title()
print(favorite_song_lowercase)
print(fovarite_song_uppercase)
print(favorite_song_title)


# In[43]:


# .split()
# .split() is performed on a string, takes one argument, and returns a list of substrings found between the given argument (which in the case of .split() is known as the delimiter). The following syntax should be used:

man_its_a_hot_one = "Like seven inches from the midday sun"
print(man_its_a_hot_one.split())

greatest_guitarist = "santana"
print(greatest_guitarist.split('n'))
print(greatest_guitarist.split('a'))


# In[44]:


authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
print(author_names)

# just keep last names
author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
  
print(author_last_names)


# In[45]:


smooth_chorus = \
"""And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""

chorus_lines = smooth_chorus.split('\n')

print(chorus_lines)


# In[46]:


# .join()
# .join() is essentially the opposite of .split(), it joins a list of strings together with a given delimiter.

my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
print(' '.join(my_munequita))
print(''.join(my_munequita))


# In[47]:


reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = " ".join(reapers_line_one_words)
print(reapers_line_one)


# In[48]:


santana_songs = ['Oye Como Va', 'Smooth', 'Black Magic Woman', 'Samba Pa Ti', 'Maria Maria']
santana_songs_csv = ','.join(santana_songs)
print(santana_songs_csv)


# In[49]:


smooth_fifth_verse_lines = ['Well I\'m from the barrio', 'You hear my rhythm on your radio', 'You feel the turning of the world so soft and slow', 'Turning you \'round and \'round']

smooth_fifth_verse = '\n'.join(smooth_fifth_verse_lines)

print(smooth_fifth_verse)


# In[50]:


# .strip()
# to remove extra whitespaces, unnecessary linebreaks and rouge tabs.

featuring = "           rob thomas                 "
print(featuring.strip())

featuring_1 = "!!!rob thomas      !!!!!"
print(featuring_1.strip('!')) # this one still has the spaces


# In[51]:


user_name = ":::::::: Eloise :::::::::::"

user_name_fixed = user_name.strip(":").strip()
print(user_name_fixed)


# In[52]:


# .replace()
# Replace takes two arguments and replaces all instances of the first argument in a string with the second argument. 
# string_name.replace(substring_being_replaced, new_substring)

with_spaces = "You got the kind of loving that can be so smooth"
with_underscores = with_spaces.replace(' ', '_')
print(with_underscores)


# In[53]:


# .find()
# find() takes a string as an argument and searching the string it was run on for that string. It then returns the first index value where that string is located.

print('smooth'.find('t'))
print("smooth".find('oo'))


# In[54]:


# .format()
# .format() takes variables as an argument and includes them in the string that it is run on. You include {} marks as placeholders for where those variables will be imported.

def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)

print(favorite_song_statement("Smooth", "Santana"))


# In[55]:


# .format() can be made even more legible for other people reading your code by including keywords. 

def favorite_song_statement(song, artist):
  return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)

# even now if keywords are not in order, the code still works
def favorite_song_statement(song, artist):
  # this will have the same output as the above example
  return "My favorite song is {song} by {artist}.".format(artist=artist, song=song)


# In[56]:


# new version of .format() is f string
def favorite_song_statement(song, artist):
  return f"My favorite song is {song} by {artist}."

print(favorite_song_statement("Smooth", "Santana"))


# ## tuples

# In[57]:


# you can store different data types and they are ordered but immutable (can not be changed)
my_info = ("Salar", 30, "programmer")
print(my_info[0])
print(my_info[1])


# ### tuple unpacking

# In[58]:


name, age, occupation = my_info
print(name)
print(occupation)


# In[59]:


# if we want to create one element tuple
one_element_tuple = (4,)
one_element_tuple


# ## lists

# In[60]:


# lists can contain any data type
mixed_list_common = ["Mia", 27, False, 0.5]

# empty list
empty_list = []


# In[61]:


# House Areas
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# creating list of areas
areas = ["hallway", hall,
         "kitchen", kit,
         "living room", liv,
         "bedroom", bed,
         "bathroom", bath]

print(areas)

# creating list of list
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

print(house)


# ### list methods

# In[62]:


# .append()

example_list = [1, 2, 3, 4]

example_list.append(5)
print(example_list)


# In[63]:


# .remove()

# if the element we want to remove has duplicates, remove method only removes the first instance.
# if we try to remove element that does not exist we get index error or Value error
example_list.remove(5)
print(example_list)


# In[64]:


# append only adds one items at a time, if want to add multiple items we can use + (concatenation)
items_sold = ["cake", "cookie", "bread"]

# we want to add "buscuit" and "tart" to the list
items_sold_new = items_sold + ["buscuit", "tart"]
print(items_sold_new)


# In[65]:


# .insert() method

store_line = ["Karla", "Maxium", "Martim", "Isabella"]

store_line.insert(2, "Vikor")
print(store_line) 


# In[66]:


# .pop() removing by index
# Passing in an index that does not exist or calling .pop() on an empty list will both result in an IndexError.

cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]

removed_element = cs_topics.pop()
print(cs_topics)
print(removed_element)

cs_topics.pop(2)
print(cs_topics)


# In[67]:


# range function / list function

# this below creats range object
my_range = range(10)
print(type(my_range))

# to turn this object to list, we use list funtion
print(list(my_range))

# if we enter one number to range function, the range starts at zero, if we want to start on number other that zero, we need to enter 2 numbers
my_list = range(2, 9)
print(list(my_list))

# if we enter 3 numbers in range function, we can create list that skips numbers
my_range2 = range(2, 9, 2)
print(list(my_range2))

my_range3 = range(1, 100, 10)
print(list(my_range3))


# In[68]:


# len() function

my_list = [1, 2, 3, 4, 5]

print(len(my_list))


# In[69]:


# .count() method to count occurances of an item on the list
letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
num_i = letters.count("i")
print(num_i)


# In[70]:


# .sort() method for sorting list
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]

names.sort()
print(names)

names.sort(reverse=True)
print(names)


# In[71]:


# sorted() function
# difference between .sort() method and sorted function is the method modifies the list but the function generates new list
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]

sorted_names = sorted(names)
print(sorted_names)
print(names)


# ### accessing list elements

# In[72]:


# python list start at index zero
employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

employee_four = employees[3]
print(employee_four)

# print(employees[8])
# we get index error because index 8 does not exist


# In[73]:


# negative index
shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = shopping_list[-1]
index5_element = shopping_list[5]

print(last_element)
print(index5_element)


# In[74]:


# list slicing list[start: end] - end is the index we want + 1

letters = ["a", "b", "c", "d", "e", "f", "g"]
# we want letter b to f
sliced_list = letters[1:6]
print(sliced_list)


# In[75]:


# slicing for first n elements list[:n]
fruits = ["apple", "cherry", "pineapple", "orange", "mango"]
print(fruits[:3])

# accessing last n element list[-n:]
print(fruits[-2:])


# ### modifying elements

# In[76]:


# replacing cauliflower with straberries
garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]

garden[2] = "Strawberries"
print(garden)


# ### 2D lists

# In[77]:


# lists can contain other list as elements, we call these 2D list
heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]
print(heights)


# In[78]:


# accessing 2D list
noelles_height = heights[0][1]
print(noelles_height)


# In[79]:


# modifying 2D list
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]

# change Jenny's hobby to meditation
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies)


# In[80]:


# .count() with 2D list
number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]
num_pairs = number_collection.count([100, 200])
print(num_pairs)


# ### list unpacking

# In[81]:


numbers = [1, 2, 3]
first, second, third = numbers # first = 1, second = 2, third = 3
print(first)
print(second)
print(third)


# In[82]:


numbers = [1, 2, 3, 4, 5, 6]
first_1, second_2, *others = numbers
print(first_1)
print(second_2)
print(others)


# ### combining lists: zip function

# In[83]:


# allows to combine list
names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]

# we want to create a nested list that combines each name with a height
names_and_heights = zip(names, heights)
print(names_and_heights)
converted_list = list(names_and_heights)
print(converted_list)

# when using zip function, the inner elements does not use [] because they are converted to tuples.


# ### list comprehension

# In[84]:


# list comprehension syntax
# new_list = [<expression> for <element> in <collection>]
numbers = [2, -1, 79, 33, -45]
doubled = []

for number in numbers:
  doubled.append(number * 2)

print(doubled)


# In[85]:


# same output via list comprehension
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)


# In[86]:


# list comprehension with conditionals
# if we want to double only negative numbers in numbers list

numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []

for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)

print(only_negative_doubled) 


# In[87]:


# same output via list comprehension
numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)


# In[88]:


# list comprehension with if else statement
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
print(doubled)


# ## functions

# In[89]:


# python has built in functions and user defined functions

# some builtin functions are:
# print
# srt()
# len()
# help()
# min() and max()
# round()
# return


# In[90]:


# round function 
tshirt_price = 9.75

rounded_price = round(tshirt_price, 1)
print(rounded_price)


# ### defining function

# In[91]:


# to define a function
def trip_welcome():
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")
    
# to call a function
trip_welcome()


# In[92]:


# defining function with one parameter
def trip_welcome(destination):
  print("Welcome to Tripcademy!") 
  print("Looks like you're going to " + destination + " today.")
    
trip_welcome("Denver")


# In[93]:


# defining function with multiple parameters
def trip_welcome(origin, destination):
  print("Welcome to Tripcademy")
  print("Looks like you are traveling from " + origin)
  print("And you are heading to " + destination)

trip_welcome("Prospect Park", "Atlantic Terminal")


# In[94]:


# function with keyword arguments
def calculate_taxi_price(miles_to_travel, rate, discount):
  print(miles_to_travel * rate - discount )

calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)


# In[95]:


# funtion with default values
def calculate_taxi_price(miles_to_travel, rate, discount = 10):
  print(miles_to_travel * rate - discount )


# Using the default value of 10 for discount.
calculate_taxi_price(10, 0.5)

# Overwriting the default value of 10 with 20
calculate_taxi_price(10, 0.5, 20)


# ### return

# In[96]:


# return - Functions can also return a value to the program so that this value can be modified or used later.
def calculate_exchange_usd(us_dollars, exchange_rate):
  return us_dollars * exchange_rate

new_zealand_exchange = calculate_exchange_usd(100, 1.4)

print("100 dollars in US currency would give you " + str(new_zealand_exchange) + " New Zealand dollars")


# In[97]:


# multiple returns - We can return several values by separating them with a comma.
weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']

def threeday_weather_report(weather):
  first_day = " Tomorrow the weather will be " + weather[0]
  second_day = " The following day it will be " + weather[1]
  third_day = " Two days from now it will be " + weather[2]
  return first_day, second_day, third_day

monday, tuesday, wednesday = threeday_weather_report(weather_data)

print(monday)
print(tuesday)
print(wednesday)


# In[98]:


def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)


# In[99]:


time = "3pm"
mood = "good"

def report():
  print("The current time is " + time)
  print("The mood is " + mood)

print("Beginning of report")

report()


# ## modules
# ### datetime module

# In[100]:


# datetime module allows to work with date and time

from datetime import datetime

current_time = datetime.now()
print(current_time)

# create a date time, year, month, day, hour, minute, second, milisecond, timezone
birthday = datetime(1993, 3, 25, 12, 30, 15)
print(birthday)
print(birthday.year)
print(birthday.month)
print(birthday.weekday) # week day is number between 0 and 6 which monday is 0 and 6 represent sunday


# In[101]:


print(datetime(2018, 1, 1) - datetime(2017, 1, 1))
print(datetime.now() - datetime(2018, 1, 1))
print(datetime.now() - birthday)


# In[102]:


# strptime
# if we don't have clean datetime object, we can parse it and change it to correct format
user_date = "jan 15, 2018"
user_date_2 = "Jul 07, 2016"
parsed_date = datetime.strptime(user_date, '%b %d, %Y')
parsed_date_2 = datetime.strptime(user_date_2, '%b %d, %Y')
print(parsed_date.month)
print(parsed_date.year)
print(parsed_date_2.month)


# In[103]:


# srtftime
# we are going to datetime object and format it as string

date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)


# ### random module

# In[104]:


# random module allows to generate random numbers or select items at random
# we’ll be using more than one piece of the module’s functionality, so we need to import the whole module

# random.choice() which takes a list as an argument and returns a number from the list

# radnom.randint() which takes two numbers as arguments and generates a random number between the two numbers you passed in

# Import random below:
import random

# Create random_list below:
random_list = []
random_list = [random.randint(1,100) for i in range(101)]
# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)


# ### decimal module

# In[105]:


# decimal arithmatic using python builtin floating points
cost_of_gum = 0.10
cost_of_gumdrop = 0.35

cost_of_transaction = cost_of_gum + cost_of_gumdrop
print(cost_of_transaction)


# In[106]:


# same operation using decimal module

from decimal import Decimal
cost_of_gum = Decimal('0.10')
cost_of_gumdrop = Decimal('0.35')

cost_of_transaction = cost_of_gum + cost_of_gumdrop
print(cost_of_transaction)


# ### files

# In[107]:


# files in python act as module
# imagine we have a file called library.py that has function. if we want to access that function in other file, we can import the file
# import library
# and call the function we need


# ## Dictionaries
# ### creating and updating dicts

# In[108]:


animals_in_zoo.update({"monkeys": 12})
animals_in_zoo["dinosaurs"] = 0


# In[ ]:


# keys and values can be any data type
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}
print(students_in_classes)


# In[ ]:


# adding new key value pair to dictionaries
locations = {}
locations["Paris"] = 100
locations.update({"London": 75})
locations.update({"New York": 83, "Vancouver": 110})

print(locations)


# In[ ]:


# overwrite existing value
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)


# ### Dict Comprehensions

# In[ ]:


# if we have 2 lists that we want to combine into a dictionary

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {key:value for key, value in zip(names, heights)}
print(students)


# In[ ]:


# dictionaries can't have duplicate keys. if during list comprehension, first list has duplicate element, it will be overwritten in the process

# if we have 2 lists that we want to combine into a dictionary
cities = ["New York", "London", "Sydney", "New York"]
temps = [ 85, 81, 65, 99]

weather = {key:value for key,value in zip(cities, temps)}

print(weather)


# ### using dictionaries

# In[ ]:


building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

print(building_heights["Burj Khalifa"])
print(building_heights["Ping An"])


# In[ ]:


# if we want to access a  key that does not exist in a dictionary we get an error to avoid we can use if statement
key_to_check = "Landmark 81"

if key_to_check in building_heights:
  print(building_heights["Landmark 81"])


# ### .get( ) method

# In[ ]:


# Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. If the key you are trying to .get() does not exist, it will return None by default.

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

#this line will return 632:
print(building_heights.get("Shanghai Tower"))

#this line will return None:
print(building_heights.get("My House"))

# You can also specify a value to return if the key doesn’t exist. For example, we might want to return a building height of 0 if our desired building is not in the dictionary
print(building_heights.get('Shanghai Tower', 0))
print(building_heights.get('Mt Olympus', 0))
print(building_heights.get('Kilimanjaro', 'No Value'))


# ### .pop( ) method: deleting a key 

# In[ ]:


# to delete a key, we can use .pop() method
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

print(raffle.pop(320291, "No Prize"))
print(raffle)


# In[ ]:


print(raffle.pop(320291, "No Prize"))
print(raffle.pop(100000, "No Prize"))
print(raffle.pop(872921, "No Prize"))

print(raffle)


# ### get all keys

# In[ ]:


# we can access list of all keys using .list() method
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

print(list(test_scores))


# In[ ]:


# also there is .keys() method which returns a dict_keys object that we can itterate. you can not add or remove elements from dict_keys object

for student in test_scores.keys():
    print(student)


# ### get all values

# In[ ]:


# we can use .valus() method to create dict_values object that we can itterate.

for score in test_scores.values():
    print(score)


# ### get all values

# In[ ]:


# we can get both keys and values using .item() method which returns dict_list object. each element of the dict_list is a tuple (key, value)

biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
 print(company + " has a value of " + str(value) + " billion dollars. ")


# ### in keyword with dictionaries

# In[ ]:


# we can use in keyword to check if something exist as key in a dictionary

inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}

print(12 in inventory)
# this checks if 12 is a key in inventory dictionary and returns False


# ## file handling in python
# ### reading files

# In[ ]:


with open('real_cool_document.txt') as cool_doc:
    cool_contents = cool_doc.read()
print(cool_contents)


# In[ ]:


# we can save the whole file to one string using read() or if we want to read file line by line we can use readline() 


# ### writing files

# In[ ]:


# we pass the argument 'w' to open() in order to indicate to open the file in write-mode. The default argument is 'r' and passing 'r' to open() opens the file in read-mode

with open("bad_bands.txt", "w") as bad_bands_doc:
    bad_bands_doc.write("Z bazi!")


# ### appending to a file

# In[ ]:


# Instead of opening the file using the argument 'w' for write-mode, we open it with 'a' for append-mode.
with open('generated_file.txt', 'a') as gen_file:
    gen_file.write("\n... and it still is")


# ### handling csv file

# In[ ]:


# since csv fiels are plain text we can open similarly to txt files
with open("Users.csv") as Users:
    users = Users.read()
    
print(users)

# in this example the whole thing parsed as single string


# ### turn csv file to dictionary

# In[ ]:


import csv

list_of_email_addresses = []
with open('users.csv', newline='') as users_csv:
    user_reader = csv.DictReader(users_csv)
    for row in user_reader:
        list_of_email_addresses.append(row['Email'])
        
print(list_of_email_addresses)


# In[ ]:


# files with different delimiter
import csv

with open('addresses.txt', newline='') as addresses_csv:
    address_reader = csv.DictReader(addresses_csv, delimiter=';')
    for row in address_reader:
        print(row['Address'])


# ### writing csv file

# In[ ]:


big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}] 

import csv

with open('output.csv', 'w') as output_csv:
    fields = ['name', 'userid', 'is_admin']
    output_writer = csv.DictWriter(output_csv, fieldnames=fields)

    output_writer.writeheader()
    for item in big_list:
        output_writer.writerow(item)


# # Class

# In[1]:


# a class is a template for a data type. it describes the kinds of information that class will hold and how programmer will interact with that data
# to define a class, we should capitalizee the name and use class keyword
class CoolClass:
    pass


# In[3]:


# a class doesn't do anything by itself, we must create an instance of the class, in order to breathe life into the schematic.
# Instantiating a class looks a lot like calling a function. We would be able to create an instance of our defined CoolClass as follows:
# below, we created an object by adding parentheses to the name of the class. We then assigned that new instance to the variable cool_instance for safe-keeping so we can access our instance of CoolClass at a later time.cool_instance = CoolClass()
cool_instance = CoolClass()


# ### OOP

# In[7]:


# A class instance is also called an object. The pattern of defining classes and creating objects to represent the responsibilities of a program is known as Object Oriented Programming or OOP.
# Instantiation takes a class and turns it into an object, the type() function does the opposite of that. When called with an object, it returns the class that the object is an instance of.
# In Python __main__ means “this current file that we’re running” and so one could read the output from type() to mean “the class CoolClass that was defined here, in the script you’re currently running.”
print(type(cool_instance))


# ### class variables

# In[9]:


# When we want the same data to be available to every instance of a class we use a class variable. A class variable is a variable that’s the same for every instance of the class.
# ou can define a class variable by including it in the indented part of your class definition, and you can access all of an object’s class variables with object.variable syntax.
class Musician:
    title = "Rockstar"

drummer = Musician()
print(drummer.title)
print(type(drummer))


# ### class methods

# In[11]:


# methods are functions that are defined as part of a class
class Dog:
    dog_time_dilation = 7

    def time_explanation(self):
        print(f"Dogs experience {self.dog_time_dilation} years for every 1 human year.")

pipi_pitbull = Dog()
pipi_pitbull.time_explanation()

# in this example we create dog class with a time_explanation() method that takes one argument self which refers to the object calling the function.
# we created a dog name pipi_pitbull and called the .time_explanation() method on our new object for Pipi.
# notice we didn't pass any arguments when we called .time_explanation, but we were able to refer to self in the function body. When you call a method it automatically passes the object calling the method as the first argument.


# ### methods with arguments

# In[13]:


# methods can take more arguments than just self
class DistanceConverter:
    kms_in_a_mile = 1.609
    def how_many_kms(self, miles):
        return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)

# Above we defined a DistanceConverter class, instantiated it, and used it to convert 5 miles into kilometers. Notice again that even though .how_many_kms() takes two arguments in its definition, we only pass miles, because self is implicitly passed (and refers to the object converter).


# ## Coonstructors

# In[14]:


# There are several methods that we can define in a Python class that have special behavior. These methods are sometimes called “magic,” because they behave differently from regular methods. 
# Another popular term is dunder methods, so-named because they have two underscores (double-underscore abbreviated to “dunder”) on either side of them.
# Methods that are used to prepare an object being instantiated are called constructors.


# ### init

# In[16]:


# __init__  This method is used to initialize a newly created object. It is called every time the class is instantiated.
class Shouter:
    def __init__(self):
        print("HELLO?!")

shout1 = Shouter()

shout2 = Shouter()

# Above, we created a class called Shouter and every time we create an instance of Shouter the program prints out a shout.


# In[1]:


# adding parameters:
class Shouter:
    def __init__(self, phrase):
        #make sure phrase is a string
        if type(phrase) == str:
            
            # then shout it out loud
            print(phrase.upper())
            
shout_1 = Shouter("shout")

shout_2 = Shouter("let it all out")


# ### Instance variable

# In[3]:


# The data held by an object is referred to as an instance variable. Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to.

class FakeDict:
    pass

fake_dict1 = FakeDict()
fake_dict2 = FakeDict()

fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"

# Let's join the two strings together!
working_string = f"{fake_dict1.fake_key} {fake_dict2.fake_key}"
print(working_string)


# ### Attribute Functions

# In[4]:


# instance variables and class variables are both accessed similarly in Python.
# they are both considered attributes of an object. 
# If we attempt to access an attribute that is neither a class variable nor an instance variable of the object Python will throw an AttributeError.

class NoCustomAttributes:
    pass

attributeless = NoCustomAttributes()

try:
    attributeless.fake_attribute
except AttributeError:
    print("This text gets printed!")


# In[7]:


# if we are not sure if an object has an attribute or not we can use hasattr() and if it returns True object has a given attribute and False otherwise.
# If we want to get the actual value of the attribute, getattr() is a Python function that will return the value of a given object and attribute.
# we can also supply a third argument that will be the default if the object does not have the given attribute.
    # hasattr(object, “attribute”)
    # getattr(obkect, "attribute", default)

print(hasattr(attributeless, "fake_attribute"))

print(getattr(attributeless, "other_fake_attribute", 800))


# ### self

# In[11]:


# we can use class instead of dictionary

class SearchEngineEntry:
    def __init__(self, url):
        self.url = url

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.url)

print(wikipedia.url)


# In[10]:


# Since the self keyword refers to the object and not the class being called, we can define a .secure() method on the SearchEngineEntry class that returns the secure link to an entry.

class SearchEngineEntry:
    secure_prefix = "https://"
    def __init__(self, url):
        self.url = url

    def secure(self):
        return f"{self.secure_prefix}{self.url}"

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.secure())

print(wikipedia.secure())


# ### object

# In[1]:


# we can cal dir() method to get list of all attributes
class FakeDict:
    pass

fake_dict = FakeDict()
fake_dict.attribute = "Cool"

print(dir(fake_dict))


# ### string represntation

# In[3]:


class Employee():
    def __init__(self, name):
        self.name = name

argus = Employee("Argus Filch")
print(argus)

# This default string representation gives us some information, like where the class is defined and our computer’s memory address where this object is stored, but is usually not useful information to have when we are trying to debug our code.


# In[4]:


# __repr__ This is a method we can use to tell Python what we want the string representation of the class to be. __repr__() can only have one parameter, self, and must return a string.

class Employee():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

argus = Employee("Argus Filch")
print(argus)


# In[ ]:




