#!/usr/bin/env python
# coding: utf-8

# # Physics Class

# In[1]:


# write a function that takes temperature in Fahrenheit as input and converts it to Celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp


# In[2]:


# testing our function if temperature is 100 Fahrenheit
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)


# In[3]:


# write a function that takes temperature in Celsius and converts it to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp


# In[4]:


# test function with 0 Celsius
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)


# In[5]:


# define a function to calculate force
def get_force(mass, acceleration):
    force = mass * acceleration
    return force


# In[6]:


train_mass = 22680
train_acceleration = 10


# In[10]:


# test function with given data
train_force = get_force(train_mass, train_acceleration)
print(train_force)


# In[11]:


print("The GE train supplies " + str(train_force) + " Newtoons of force.")


# In[12]:


# define a function to calculate energy
def get_energy(mass, c = 3*10**8):
    energy = mass * (c ** 2)
    return energy


# In[13]:


bomb_mass = 1


# In[30]:


# test function with bomb mass
bomb_energy = get_energy(bomb_mass)
print(bomb_energy)


# In[31]:


print("A 1kg bomb supplies " + str(bomb_energy) + " Jules.")


# In[32]:


# define a function to calculate the work
def get_work(mass, acceleration, distance):
    f = get_force(mass, acceleration)
    work = f * distance
    return work


# In[33]:


train_distance = 100


# In[34]:


train_work = get_work(train_mass, train_acceleration, train_distance)
print(train_work)


# In[35]:


print("the GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters" )

