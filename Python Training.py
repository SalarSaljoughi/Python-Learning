{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "54267398",
   "metadata": {},
   "source": [
    "# Python Basics\n",
    "### print function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a37955eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World!\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello World!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "59e98568",
   "metadata": {},
   "source": [
    "### variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fa2fd021",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello there\n",
      "Hasta la vista\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "# strings - Greeting\n",
    "message_string = \"Hello there\"\n",
    "print(message_string)\n",
    "\n",
    "# Strings - Farewell\n",
    "message_string = \"Hasta la vista\"\n",
    "print(message_string)\n",
    "\n",
    "# int & float\n",
    "an_int = 2\n",
    "a_float = 2.1\n",
    "\n",
    "print(an_int + 3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3104cca2",
   "metadata": {},
   "source": [
    "### calculations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9f1cb958",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n",
      "0\n",
      "15\n",
      "3.0\n",
      "27\n",
      "1\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "print(3 + 4) # Addition\n",
    "print(5 - 5) # Subtraction\n",
    "print(3 * 5) # Multiplication\n",
    "print(12 / 4) # Division\n",
    "print(3 ** 3) # Exponentiation\n",
    "print(15 % 2) # Modulus\n",
    "print(15 // 3) # Floor division"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8bb3b9f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15\n"
     ]
    }
   ],
   "source": [
    "a = 5\n",
    "b = 10\n",
    "print(a + b)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4dba5b7c",
   "metadata": {},
   "source": [
    "### concatination"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7b915b9e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hey there!How are you doing?\n",
      "Hey there! How are you doing?\n"
     ]
    }
   ],
   "source": [
    "# process of combining strings called concatination\n",
    "greeting_text = \"Hey there!\"\n",
    "question_text = \"How are you doing?\"\n",
    "full_text = greeting_text + question_text\n",
    "\n",
    "print(full_text)\n",
    "\n",
    "full_text = greeting_text + \" \" + question_text\n",
    "\n",
    "# Prints \"Hey there! How are you doing?\"\n",
    "print(full_text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2e001760",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I am 10 years old today!\n",
      "I am  10  years old today!\n"
     ]
    }
   ],
   "source": [
    "birthday_string = \"I am \"\n",
    "age = 10\n",
    "birthday_string_2 = \" years old today!\"\n",
    "\n",
    "# Concatenating an integer with strings is possible if we turn the integer into a string first\n",
    "full_birthday_string = birthday_string + str(age) + birthday_string_2\n",
    "print(full_birthday_string)\n",
    "\n",
    "# If we just want to print an integer we can pass a variable as an argument to print() regardless of whether it is a string.\n",
    "print(birthday_string, age, birthday_string_2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9a443c62",
   "metadata": {},
   "source": [
    "### updating variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "7de60d04",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "14\n"
     ]
    }
   ],
   "source": [
    "# First we have a variable with a number saved\n",
    "number_of_miles_hiked = 12\n",
    "\n",
    "# Then we need to update that variable Let's say we hike another two miles today\n",
    "number_of_miles_hiked += 2\n",
    "\n",
    "# The new value is the old value Plus the number after the plus-equals\n",
    "print(number_of_miles_hiked)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "d3568318",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What an amazing time to walk through nature! #nofilter #blessed\n"
     ]
    }
   ],
   "source": [
    "hike_caption = \"What an amazing time to walk through nature!\"\n",
    "\n",
    "# Almost forgot the hashtags!\n",
    "hike_caption += \" #nofilter\"\n",
    "hike_caption += \" #blessed\"\n",
    "\n",
    "print(hike_caption)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "74720583",
   "metadata": {},
   "source": [
    "### multiline strings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c0db4c6a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Poets to come! orators, singers, musicians to come!\n",
      "Not to-day is to justify me and answer what I am for,\n",
      "But you, a new brood, native, athletic, continental, greater than\n",
      "  before known,\n",
      "Arouse! for you must justify me.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# By using three quote-marks (\"\"\" or ''') instead of one, we tell the program that the string doesn’t end until the next triple-quote. \n",
    "# This method is useful if the string being defined contains a lot of quotation marks and we want to be sure we don’t close it prematurely.\n",
    "\n",
    "leaves_of_grass = \"\"\"\n",
    "Poets to come! orators, singers, musicians to come!\n",
    "Not to-day is to justify me and answer what I am for,\n",
    "But you, a new brood, native, athletic, continental, greater than\n",
    "  before known,\n",
    "Arouse! for you must justify me.\n",
    "\"\"\"\n",
    "\n",
    "print(leaves_of_grass)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8a0cc2e7",
   "metadata": {},
   "source": [
    "## control flow\n",
    "### if statement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "2d2abc7a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I know it is you, Dave! Go away!\n"
     ]
    }
   ],
   "source": [
    "# Enter a user name here, make sure to make it a string\n",
    "user_name = \"angela_catlady_87\"\n",
    "\n",
    "if user_name == \"Dave\":\n",
    "  print(\"Get off my computer Dave!\")\n",
    "if user_name == \"angela_catlady_87\":\n",
    "  print(\"I know it is you, Dave! Go away!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b8d09f90",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You meet the requirements to graduate!\n"
     ]
    }
   ],
   "source": [
    "# and logical operator\n",
    "credits = 120\n",
    "gpa = 3.4\n",
    "\n",
    "if credits >= 120 and gpa >=2.0:\n",
    "  print(\"You meet the requirements to graduate!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "7d46eaee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You have met at least one of the requirements.\n"
     ]
    }
   ],
   "source": [
    "# or logical operator\n",
    "credits = 118\n",
    "gpa = 2.0\n",
    "\n",
    "if credits >= 120 or gpa >= 2.0:\n",
    "  print(\"You have met at least one of the requirements.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "5b680f00",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your GPA is not high enough to graduate.\n"
     ]
    }
   ],
   "source": [
    "# not logical operator\n",
    "credits = 120\n",
    "gpa = 1.8\n",
    "\n",
    "if not credits >= 120:\n",
    "  print(\"You do not have enough credits to graduate\")\n",
    "elif (not gpa >= 2.0):\n",
    "  print(\"Your GPA is not high enough to graduate.\")\n",
    "else:\n",
    "  print(\"You do not meet either requirement to graduate!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d9002103",
   "metadata": {},
   "source": [
    "## lists"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f1b875b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# lists can contain any data type\n",
    "mixed_list_common = [\"Mia\", 27, False, 0.5]\n",
    "\n",
    "# empty list\n",
    "empty_list = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "aa23f014",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.0, 'bedroom', 10.75, 'bathroom', 9.5]\n",
      "[['hallway', 11.25], ['kitchen', 18.0], ['living room', 20.0], ['bedroom', 10.75], ['bathroom', 9.5]]\n"
     ]
    }
   ],
   "source": [
    "# House Areas\n",
    "hall = 11.25\n",
    "kit = 18.0\n",
    "liv = 20.0\n",
    "bed = 10.75\n",
    "bath = 9.50\n",
    "\n",
    "# creating list of areas\n",
    "areas = [\"hallway\", hall,\n",
    "         \"kitchen\", kit,\n",
    "         \"living room\", liv,\n",
    "         \"bedroom\", bed,\n",
    "         \"bathroom\", bath]\n",
    "\n",
    "print(areas)\n",
    "\n",
    "# creating list of list\n",
    "house = [[\"hallway\", hall],\n",
    "         [\"kitchen\", kit],\n",
    "         [\"living room\", liv],\n",
    "         [\"bedroom\", bed],\n",
    "         [\"bathroom\", bath]]\n",
    "\n",
    "print(house)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6821bb91",
   "metadata": {},
   "source": [
    "### list methods"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "dbf45073",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "# .append()\n",
    "\n",
    "example_list = [1, 2, 3, 4]\n",
    "\n",
    "example_list.append(5)\n",
    "print(example_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "94dd5514",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "# .remove()\n",
    "\n",
    "# if the element we want to remove has duplicates, remove method only removes the first instance.\n",
    "# if we try to remove element that does not exist we get index error or Value error\n",
    "example_list.remove(5)\n",
    "print(example_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "b63c1d94",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['cake', 'cookie', 'bread', 'buscuit', 'tart']\n"
     ]
    }
   ],
   "source": [
    "# append only adds one items at a time, if want to add multiple items we can use + (concatenation)\n",
    "items_sold = [\"cake\", \"cookie\", \"bread\"]\n",
    "\n",
    "# we want to add \"buscuit\" and \"tart\" to the list\n",
    "items_sold_new = items_sold + [\"buscuit\", \"tart\"]\n",
    "print(items_sold_new)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2abf2ceb",
   "metadata": {},
   "source": [
    "### accessing list elements"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "a8505c37",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pam\n"
     ]
    }
   ],
   "source": [
    "# python list start at index zero\n",
    "employees = [\"Michael\", \"Dwight\", \"Jim\", \"Pam\", \"Ryan\", \"Andy\", \"Robert\"]\n",
    "\n",
    "employee_four = employees[3]\n",
    "print(employee_four)\n",
    "\n",
    "# print(employees[8])\n",
    "# we get index error because index 8 does not exist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "1629d455",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cereal\n",
      "cereal\n"
     ]
    }
   ],
   "source": [
    "# negative index\n",
    "shopping_list = [\"eggs\", \"butter\", \"milk\", \"cucumbers\", \"juice\", \"cereal\"]\n",
    "\n",
    "last_element = shopping_list[-1]\n",
    "index5_element = shopping_list[5]\n",
    "\n",
    "print(last_element)\n",
    "print(index5_element)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "14684d30",
   "metadata": {},
   "source": [
    "### modifying elements"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "82755033",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Tomatoes', 'Green Beans', 'Strawberries', 'Grapes']\n"
     ]
    }
   ],
   "source": [
    "# replacing cauliflower with straberries\n",
    "garden = [\"Tomatoes\", \"Green Beans\", \"Cauliflower\", \"Grapes\"]\n",
    "\n",
    "garden[2] = \"Strawberries\"\n",
    "print(garden)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4f5ff9c0",
   "metadata": {},
   "source": [
    "### 2D lists"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "2cfb7ecc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['Noelle', 61], ['Ava', 70], ['Sam', 67], ['Mia', 64]]\n"
     ]
    }
   ],
   "source": [
    "# lists can contain other list as elements, we call these 2D list\n",
    "heights = [[\"Noelle\", 61], [\"Ava\", 70], [\"Sam\", 67], [\"Mia\", 64]]\n",
    "print(heights)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "99cd1d17",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "61\n"
     ]
    }
   ],
   "source": [
    "# accessing 2D list\n",
    "noelles_height = heights[0][1]\n",
    "print(noelles_height)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "eb8a4dde",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['Jenny', 'Meditation'], ['Alexus', 'Photography'], ['Grace', 'Soccer']]\n"
     ]
    }
   ],
   "source": [
    "# modifying 2D list\n",
    "class_name_hobbies = [[\"Jenny\", \"Breakdancing\"], [\"Alexus\", \"Photography\"], [\"Grace\", \"Soccer\"]]\n",
    "\n",
    "# change Jenny's hobby to meditation\n",
    "class_name_hobbies[0][1] = \"Meditation\"\n",
    "print(class_name_hobbies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2745dbd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
