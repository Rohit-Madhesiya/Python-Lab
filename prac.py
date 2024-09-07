# def is_rightangled_triangle(a, b, c):
#   sides = [a, b, c]
#   sides.sort()
#   if sides[0]**2 + sides[1]**2 == sides[2]**2:
#     return True
#   else:
#     return False

# a, b, c = int(input()), int(input()), int(input())
# print(is_rightangled_triangle(a, b, c))

# def celsius_to_fahrenheit(celsius):
#   return (celsius * 9 / 5) + 32

# def fahrenheit_to_celsius(fahrenheit):
#   return (fahrenheit - 32) * 5 / 9

# a = float(input("Enter the temperature in celsius: "))
# print("The temperature in fahrenheit is: ", celsius_to_fahrenheit(a))
# b = float(input("Enter the temperature in fahrenheit: "))
# print(f"The temperature in celsius is: {fahrenheit_to_celsius(b)}")

# result = [str(x) for x in range(1500, 2701) if x % 7 == 0 and x % 5 == 0]
# print(','.join(result))

# def check_perfect_square(num):
#   sqrt_val = int(num**0.5)
#   return sqrt_val * sqrt_val == num

# def is_fibonacci_multiple(num):
#   return check_perfect_square(5 * num * num +
#                               4) or check_perfect_square(5 * num * num - 4)

# num = int(input("Enter a number: "))
# print(is_fibonacci_multiple(num))

# def transpose_matrix(matrix):
#   return [[matrix[j][i] for j in range(len(matrix))]
#           for i in range(len(matrix[0]))]

# row = int(input("Enter the number of rows: "))
# col = int(input("Enter the number of columns: "))
# matrix = [[
#     int(input(f"Enter element at position [{i}][{j}]: ")) for j in range(col)
# ] for i in range(row)]

# t_matrix = transpose_matrix(matrix)
# for mat in t_matrix:
#   print(mat)

# def find_remainder(arr, n):
#   result = 1
#   for num in arr:
#     result = (result * num) % n
#   return result

# arr = [1, 2, 3, 4, 5]
# result = find_remainder(arr, 5)
# print("Remainder is:", result)

# import math

# radius = float(input("Enter the radius of the circle: "))
# area = math.pi * (radius**2)
# print("The area of the circle is:", area)

# import os

# filename = 'example.txt'

# if os.access(filename, os.R_OK):
#   print('Read permission')
# else:
#   print('No read permission')

# if os.access(filename, os.W_OK):
#   print('Write permission')
# else:
#   print('No write permission')

# if os.access(filename, os.X_OK):
#   print('Execute permission')
# else:
#   print('No execute permission')

# import calendar

# year = 2024
# month = 1

# print(calendar.month(year, month))

# class WelcomeMessage:

#   def display_message(self):
#     print("Welcome to MMMUT")

# welcome = WelcomeMessage()
# welcome.display_message()

# class StringInfo:

#   def __init__(self, input_string):
#     self.input_string = input_string

#   def count_uppercase(self):
#     return sum(1 for char in self.input_string if char.isupper())

#   def count_lowercase(self):
#     return sum(1 for char in self.input_string if char.islower())

#   def count_vowels(self):
#     vowels = 'aeiouAEIOU'
#     return sum(1 for char in self.input_string if char in vowels)

#   def count_consonants(self):
#     consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
#     return sum(1 for char in self.input_string if char in consonants)

#   def count_spaces(self):
#     return sum(1 for char in self.input_string if char.isspace())

# input_string = input("Enter a string: ")
# string_info = StringInfo(input_string)
# print(f"Uppercase: {string_info.count_uppercase()}")
# print(f"Lowercase: {string_info.count_lowercase()}")
# print(f"Vowels: {string_info.count_vowels()}")
# print(f"Consonants: {string_info.count_consonants()}")
# print(f"Spaces: {string_info.count_spaces()}")


# filename = input("Enter the file name: ")
# with open(filename, 'r') as file:
#   content = file.read()
#   char_count = {}
#   for char in content:
#     if char in char_count:
#       char_count[char] += 1
#     else:
#       char_count[char] = 1
#   print(char_count)

# filename = input("Enter the file name: ")
# key_value_pair = input("Enter the key value pair (key=value): ")
# count = 0

# with open(filename, 'r') as file:
#   for line in file:
#     if key_value_pair in line:
#       count += 1
# print(
#     f"Number of occurrences of key value pair '{key_value_pair}' in the file: {count}"
# )

# import pandas as pd

# data = pd.read_csv('medal.csv')
# print(data.head())
# print(data.tail())

# import pandas as pd

# data = {'external_value': [100, 200, 300], 'dataframe_value': ['A', 'B', 'C']}
# df = pd.DataFrame(data)

# external_values = [100, 200, 300]
# mapped_values = [
#     df.loc[df['external_value'] == val, 'dataframe_value'].values[0]
#     for val in external_values
# ]

# print(mapped_values)

# import matplotlib.pyplot as plt

# marks = [75, 80, 65, 90, 70]
# subjects = ['Math', 'Science', 'English', 'History', 'Geography']

# plt.pie(marks, labels=subjects, autopct='%1.1f%%')
# plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('medal.csv')
top_countries = data.nlargest(5, 'gold_medal')
plt.pie(top_countries['gold_medal'],
        labels=top_countries['country'],
        autopct='%1.1f%%')
plt.title(
    'Gold Medal Achievements of Five Most Successful Countries in 2016 Summer Olympics'
)
plt.show()