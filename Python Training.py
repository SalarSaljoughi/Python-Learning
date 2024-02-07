{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "id": "54267398",
      "cell_type": "markdown",
      "source": "# Python Basics\n### print function",
      "metadata": {}
    },
    {
      "id": "a37955eb",
      "cell_type": "code",
      "source": "print(\"Hello World!\")",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Hello World!\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 1
    },
    {
      "id": "59e98568",
      "cell_type": "markdown",
      "source": "### variables",
      "metadata": {}
    },
    {
      "id": "fa2fd021",
      "cell_type": "code",
      "source": "# strings - Greeting\nmessage_string = \"Hello there\"\nprint(message_string)\n\n# Strings - Farewell\nmessage_string = \"Hasta la vista\"\nprint(message_string)\n\n# int & float\nan_int = 2\na_float = 2.1\n\nprint(an_int + 3)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Hello there\nHasta la vista\n5\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 2
    },
    {
      "id": "3104cca2",
      "cell_type": "markdown",
      "source": "### calculations",
      "metadata": {}
    },
    {
      "id": "9f1cb958",
      "cell_type": "code",
      "source": "print(3 + 4) # Addition\nprint(5 - 5) # Subtraction\nprint(3 * 5) # Multiplication\nprint(12 / 4) # Division\nprint(3 ** 3) # Exponentiation\nprint(15 % 2) # Modulus\nprint(15 // 3) # Floor division",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "7\n0\n15\n3.0\n27\n1\n5\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 3
    },
    {
      "id": "8bb3b9f4",
      "cell_type": "code",
      "source": "a = 5\nb = 10\nprint(a + b)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "15\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 4
    },
    {
      "id": "4dba5b7c",
      "cell_type": "markdown",
      "source": "### concatination",
      "metadata": {}
    },
    {
      "id": "7b915b9e",
      "cell_type": "code",
      "source": "# process of combining strings called concatination\ngreeting_text = \"Hey there!\"\nquestion_text = \"How are you doing?\"\nfull_text = greeting_text + question_text\n\nprint(full_text)\n\nfull_text = greeting_text + \" \" + question_text\n\n# Prints \"Hey there! How are you doing?\"\nprint(full_text)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Hey there!How are you doing?\nHey there! How are you doing?\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 5
    },
    {
      "id": "2e001760",
      "cell_type": "code",
      "source": "birthday_string = \"I am \"\nage = 10\nbirthday_string_2 = \" years old today!\"\n\n# Concatenating an integer with strings is possible if we turn the integer into a string first\nfull_birthday_string = birthday_string + str(age) + birthday_string_2\nprint(full_birthday_string)\n\n# If we just want to print an integer we can pass a variable as an argument to print() regardless of whether it is a string.\nprint(birthday_string, age, birthday_string_2)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "I am 10 years old today!\nI am  10  years old today!\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 6
    },
    {
      "id": "9a443c62",
      "cell_type": "markdown",
      "source": "### updating variables",
      "metadata": {}
    },
    {
      "id": "7de60d04",
      "cell_type": "code",
      "source": "# First we have a variable with a number saved\nnumber_of_miles_hiked = 12\n\n# Then we need to update that variable Let's say we hike another two miles today\nnumber_of_miles_hiked += 2\n\n# The new value is the old value Plus the number after the plus-equals\nprint(number_of_miles_hiked)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "14\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 7
    },
    {
      "id": "d3568318",
      "cell_type": "code",
      "source": "hike_caption = \"What an amazing time to walk through nature!\"\n\n# Almost forgot the hashtags!\nhike_caption += \" #nofilter\"\nhike_caption += \" #blessed\"\n\nprint(hike_caption)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "What an amazing time to walk through nature! #nofilter #blessed\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 8
    },
    {
      "id": "74720583",
      "cell_type": "markdown",
      "source": "### multiline strings",
      "metadata": {}
    },
    {
      "id": "c0db4c6a",
      "cell_type": "code",
      "source": "# By using three quote-marks (\"\"\" or ''') instead of one, we tell the program that the string doesn’t end until the next triple-quote. \n# This method is useful if the string being defined contains a lot of quotation marks and we want to be sure we don’t close it prematurely.\n\nleaves_of_grass = \"\"\"\nPoets to come! orators, singers, musicians to come!\nNot to-day is to justify me and answer what I am for,\nBut you, a new brood, native, athletic, continental, greater than\n  before known,\nArouse! for you must justify me.\n\"\"\"\n\nprint(leaves_of_grass)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "\nPoets to come! orators, singers, musicians to come!\nNot to-day is to justify me and answer what I am for,\nBut you, a new brood, native, athletic, continental, greater than\n  before known,\nArouse! for you must justify me.\n\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 9
    },
    {
      "id": "8a0cc2e7",
      "cell_type": "markdown",
      "source": "## control flow\n### if statement",
      "metadata": {}
    },
    {
      "id": "2d2abc7a",
      "cell_type": "code",
      "source": "# Enter a user name here, make sure to make it a string\nuser_name = \"angela_catlady_87\"\n\nif user_name == \"Dave\":\n  print(\"Get off my computer Dave!\")\nif user_name == \"angela_catlady_87\":\n  print(\"I know it is you, Dave! Go away!\")",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "I know it is you, Dave! Go away!\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 10
    },
    {
      "id": "b8d09f90",
      "cell_type": "code",
      "source": "# and logical operator\ncredits = 120\ngpa = 3.4\n\nif credits >= 120 and gpa >=2.0:\n  print(\"You meet the requirements to graduate!\")",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "You meet the requirements to graduate!\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 11
    },
    {
      "id": "7d46eaee",
      "cell_type": "code",
      "source": "# or logical operator\ncredits = 118\ngpa = 2.0\n\nif credits >= 120 or gpa >= 2.0:\n  print(\"You have met at least one of the requirements.\")",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "You have met at least one of the requirements.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 12
    },
    {
      "id": "5b680f00",
      "cell_type": "code",
      "source": "# not logical operator\ncredits = 120\ngpa = 1.8\n\nif not credits >= 120:\n  print(\"You do not have enough credits to graduate\")\nelif (not gpa >= 2.0):\n  print(\"Your GPA is not high enough to graduate.\")\nelse:\n  print(\"You do not meet either requirement to graduate!\")",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Your GPA is not high enough to graduate.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 13
    },
    {
      "id": "4e3440d4",
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "f1b875b4",
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}