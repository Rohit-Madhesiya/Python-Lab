import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generating random data
np.random.seed(0)
X = np.random.rand(100, 2)

# Fitting the KMeans model
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
y_kmeans = kmeans.predict(X)

# Plotting the clustered data
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], s=200, alpha=0.5)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generating random data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Fitting the model
model = LinearRegression()
model.fit(X, y)

# Making predictions
X_new = np.array([[0], [2]])
y_pred = model.predict(X_new)

# Plotting the data and the regression line
plt.scatter(X, y)
plt.plot(X_new, y_pred, 'r-')
plt.show()





import csv

def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["empno", "name", "salary"])
        for row in data:
            writer.writerow(row)

def search_emp_info(filename, empno):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['empno'] == empno:
                print(f"Employee found - Name: {row['name']}, Salary: {row['salary']}")
                return
    print("Employee not found")

data = [
    ["1", "John Doe", "50000"],
    ["2", "Jane Smith", "60000"],
    ["3", "Tom Brown", "55000"]
]

write_to_csv('employee.csv', data)
search_emp_info('employee.csv', '2')
search_emp_info('employee.csv', '4')




import matplotlib.pyplot as plt

# Bar chart
x = ['A', 'B', 'C', 'D', 'E']
y = [10, 20, 30, 40, 50]
plt.bar(x, y)
plt.title('Bar Chart')
plt.show()

# Histogram
import numpy as np
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.title('Histogram')
plt.show()

# Pie chart
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()





# Experiment-10 (2)
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














# mmmut/
#   __init__.py
#   all_department/
#       __init__.py
#       itca.py
#       itrc.py
#       ece.py
#       ee.py
#       ce.py
#       me.py


# itca.py
def admin():
  print("Admin function in ITCA department")


# itrc.py
def cabin():
  print("Cabin function in ITRC department")


import os

filename = 'example.txt'

if os.access(filename, os.R_OK):
  print('Read permission')
else:
  print('No read permission')

if os.access(filename, os.W_OK):
  print('Write permission')
else:
  print('No write permission')

if os.access(filename, os.X_OK):
  print('Execute permission')
else:
  print('No execute permission')

import calendar

year = 2022
month = 9

print(calendar.month(year, month))


class WelcomeMessage:

  def display_message(self):
    print("Welcome to MMMUT")


welcome = WelcomeMessage()
welcome.display_message()


def transpose_matrix(matrix):
  return [[matrix[j][i] for j in range(len(matrix))]
          for i in range(len(matrix[0]))]


def get_matrix_transpose():
  row = int(input("Enter the number of rows: "))
  col = int(input("Enter the number of columns: "))
  matrix = [[
      int(input(f"Enter element at position [{i}][{j}]: ")) for j in range(col)
  ] for i in range(row)]
  transpose = [[matrix[j][i] for j in range(row)] for i in range(col)]
  return transpose


def find_remainder(arr, n):
  result = 1
  for num in arr:
    result = (result * num) % n
  return result


import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius**2)
print("The area of the circle is:", area)






# my_list = [1, 2, 3, 4, 5]

# # inserting an element
# my_list.insert(2, 10)

# # removing an element
# my_list.remove(3)

# # appending an element
# my_list.append(6)

# # length of the list
# print(len(my_list))

# # removing and returning the last element
# my_list.pop()

# # clearing the list
# my_list.clear()

# # Arithmetic operators
# num1 = 10
# num2 = 5
# print("Arithmetic Operators:")
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 % num2)
# print(num1 ** num2)

# # Assignment operators
# x = 5
# x += 3
# print("Assignment Operators:", x)

# # Logical operators
# a = True
# b = False
# print("Logical Operators:")
# print(a and b)
# print(a or b)
# print(not a)

# # Identity operators
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x
# print("Identity Operators:")
# print(x is z)
# print(x is y)
# print(x == y)

# # Membership operators
# fruits = ["apple", "banana"]
# print("Membership Operators:")
# print("banana" in fruits)
# print("orange" not in fruits)
