{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO2AJcxHc4DvPAgSv+f9F3K"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "Question 1:\n"
      ],
      "metadata": {
        "id": "-99dYCzLqNlZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "base = 10\n",
        "height = 4\n",
        "area = base*height*0.5\n",
        "print(\"The triangle has an area of \" + str(area) + \" cm\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "28RHP3-XqPw0",
        "outputId": "99ee154d-38ca-4f2a-83a9-c2fc4ddd610f"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The triangle has an area of 20.0 cm\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 2:\n"
      ],
      "metadata": {
        "id": "crA13tmEqQCC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "fenceLength = 15\n",
        "gardenPerimeter = 2*50 + 2*80\n",
        "print(\"You need \" + str(gardenPerimeter//15 + 1) + \" fences to cover the whole garden.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JJW3zIHoqR3V",
        "outputId": "a740b3ca-67fb-4e19-a6dc-4f96c35c0213"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "You need 18 fences to cover the whole garden.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 3:\n"
      ],
      "metadata": {
        "id": "NL66qJ38qSA0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "cents = 835\n",
        "dollars = cents // 100\n",
        "quarters = (cents % 100) // 25\n",
        "dimes = cents % 25 // 10\n",
        "left = cents % 25 % 10\n",
        "print(f\"\"\"Dollars: {dollars}\n",
        "Quarters: {quarters}\n",
        "Dimes: {dimes}\n",
        "Cents: {left}\"\"\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zwollRk5qTOS",
        "outputId": "1daf9129-5e28-499d-de0e-9d857d91890e"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Dollars: 8\n",
            "Quarters: 1\n",
            "Dimes: 1\n",
            "Cents: 0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 4:\n"
      ],
      "metadata": {
        "id": "tEtyqmtBqTWq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"One\\n\\tTwo\\n\\t\\tThree\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "27xDTO90qUtk",
        "outputId": "1915e471-d756-4f04-a450-fc1defca8f4a"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "One\n",
            "\tTwo\n",
            "\t\tThree\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 5:\n"
      ],
      "metadata": {
        "id": "NavEd4_-qU1j"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "name = input(\"What is your name: \")\n",
        "print(name + \" is a common name.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VapAFqPbqWoc",
        "outputId": "2de7359c-7862-4d94-c291-86e3b2d41c8b"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "What is your name: Gerald\n",
            "Gerald is a common name.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 6:\n"
      ],
      "metadata": {
        "id": "aJHCGJ_NqWx7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "filePath = \"c:\\\\Users\\\\Documents\\\\MyFile.txt\"\n",
        "print(filePath)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A-t85tdZqYSS",
        "outputId": "0352ad72-6f17-4698-84fb-f65d602e7691"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "c:\\Users\\Documents\\MyFile.txt\n"
          ]
        }
      ]
    }
  ]
}