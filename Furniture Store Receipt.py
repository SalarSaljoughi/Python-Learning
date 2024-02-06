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
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "source": "# Furniture Store Receipt",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Creating a recipt for furniture store\n\n# adding first item and its price to inventory\nlovely_loveseat_description = \"\"\"Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.\"\"\"\nlovely_loveseat_price = 254.00",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 1
    },
    {
      "cell_type": "code",
      "source": "# adding second item and its price to inventory\nstylish_settee_description = \"\"\"Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.\"\"\"\nstylish_settee_price = 180.50",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 2
    },
    {
      "cell_type": "code",
      "source": "\n# adding third item and its price to inventory\nluxurious_lamp_description = \"\"\"Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.\"\"\"\nluxurious_lamp_price = 52.15",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 3
    },
    {
      "cell_type": "code",
      "source": "# additing sales tax\nsales_tax = 0.088",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 4
    },
    {
      "cell_type": "code",
      "source": "# creating variables for customer\ncutomer_one_total = 0\ncustomer_one_itemization = \"\"",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 5
    },
    {
      "cell_type": "code",
      "source": "\n# calculating itemized list and total for first customer\ncustomer_one_total = cutomer_one_total + lovely_loveseat_price\ncustomer_one_itemization = customer_one_itemization + lovely_loveseat_description\n\nprint(customer_one_total)\nprint(customer_one_itemization)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "254.0\nLovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 6
    },
    {
      "cell_type": "code",
      "source": "# adding new item to cart\ncustomer_one_total += luxurious_lamp_price\ncustomer_one_itemization = customer_one_itemization + \"\\n\" + luxurious_lamp_description\n\nprint(customer_one_total)\nprint(customer_one_itemization)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "306.15\nLovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.\nLuxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 7
    },
    {
      "cell_type": "code",
      "source": "# calculating total for first customer\ncustomer_one_tax = customer_one_total * sales_tax\ncustomer_one_total += customer_one_tax\n\nprint(customer_one_total)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "333.09119999999996\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 8
    },
    {
      "cell_type": "code",
      "source": "# printing receipt with itemized list and total for first customer\nprint(\"Customer One Items: \")\nprint(customer_one_itemization + \"\\n\")\nprint(\"Customer One Total: \")\nprint(customer_one_total)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Customer One Items: \nLovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.\nLuxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.\n\nCustomer One Total: \n333.09119999999996\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 9
    },
    {
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