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
      "source": "# Customer List",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#create list of first name\nfirst_names = [\"Ainsley\", \"Ben\", \"Chani\", \"Depak\"]\nprint(fist_names)",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": "# create list of perferred sizes\npreferred_size = [\"Small\", \"Large\", \"Medium\"]\nprint(preferred_size)",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": "# add size for Depak\npreferred_size.append(\"Medium\")\nprint(preferred_size)",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": "# creating 2D List\ncustomer_data = [[\"Ainsley\", \"Small\", True], [\"Ben\", \"Large\", False], [\"Chani\", \"Medium\", True], [\"Depak\", \"Medium\", False]]\nprint(customer_data)",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": "# change Chani shipping method to False\ncustomer_data[2][-1] = False\n\n# remove the shipping method for Ben\n# customer_data[1].remove(customer_data[1][2])\ncustomer_data[1].remove(False)\n\nprint(customer_data)",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": "# adding new customers\ncustomer_data_final = customer_data + [[\"Amit\", \"Large\", True], [\"Karim\", \"X-Large\", False]]\nprint(customer_data_final)",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
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