#!/usr/bin/env python
# coding: utf-8

# # Gradebook

# In[ ]:


# last years grade book
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]


# In[ ]:


# this semesters subjects
subject = ["physics", "calculus", "poetry", "history"]
print(subject)


# In[ ]:


# this semesters grades
grades = [98, 97, 85, 88]
print(grades)


# In[ ]:


# creating 2D gradebook
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)


# In[ ]:


# adding new subject and grade
gradebook.append(["computer science", 100])
print(gradebook)


# In[ ]:


# adding another subject and grade
gradebook.append(["visual arts", 93])
print(gradebook)


# In[ ]:


# changing grade on one of the classes
gradebook[-1][-1] = 98
print(gradebook)

# adjusting grade in one of the classes
gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook)


# In[ ]:


# combining this year and last years grade book
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)


# In[ ]:




