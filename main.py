# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Import libraries necessary for this project
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Import supplementary visualizations code visuals.py


# Pretty display for notebooks


# Load the Boston housing dataset
data = pd.read_csv('D:\ Predicting-Boston-Housing-Prices\housing.csv')
prices = data['MEDV']
features = data.drop('MEDV', axis=1)

# Success
print("Boston housing dataset has {} data points with {} variables each.".format(*data.shape))
print(data[:10])
print(features)
print(prices)
import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(1, 1, 1)
ax.hist(data['RM'], bins = 15)
plt.title("Average number of rooms Distribution ")
plt.xlabel("RM")
plt.ylabel("frequency")
plt.show()

fig=plt.figure()
ax=fig.add_subplot(1, 1, 1)
ax.hist(data['LSTAT'], bins = 15)
plt.title("Homeowners distribution with low class")
plt.xlabel("LSTAT")
plt.ylabel("frequency")
plt.show()

fig=plt.figure()
ax=fig.add_subplot(1, 1, 1)
ax.hist(data['PTRATIO'], bins = 15)
plt.title("Students to Teachers ratio distribution")
plt.xlabel("PTRATIO")
plt.ylabel("frequency")
plt.show()

# TODO: Minimum price of the data
minimum_price = np.min(prices)

# TODO: Maximum price of the data
maximum_price = np.max(prices)

# TODO: Mean price of the data
mean_price = np.mean(prices)

# TODO: Median price of the data
median_price = np.median(prices)

# TODO: Standard deviation of prices of the data
std_price = np.std(prices)

# Show the calculated statistics
print("Statistics for Boston housing dataset:\n")
print("Minimum price: ${}".format(minimum_price))
print("Maximum price: ${}".format(maximum_price))
print("Mean price: ${}".format(mean_price))
print("Median price ${}".format(median_price))
print("Standard deviation of prices: ${}".format(std_price))


#                         RM VS PRICES
fig=plt.figure()
ax=fig.add_subplot(1, 1, 1)
ax.scatter(data['RM'], data['MEDV'])
#Lables & Title
plt.title("Average selling Prices and Average number of rooms")
plt.xlabel("RM")
plt.ylabel("Prices")
plt.show()

#                       LSTAT VS PRICES
fig=plt.figure()
ax=fig.add_subplot(1, 1, 1)
ax.scatter(data['LSTAT'], data['MEDV'])
plt.title("Average selling Prices VS % of low class Homeowners")
plt.xlabel("LSTAT")
plt.ylabel("Prices")
plt.show()

#                       PTRATIO VS PRICES
fig=plt.figure()
ax=fig.add_subplot(1, 1, 1)
ax.scatter(data['PTRATIO'], data['MEDV'])
plt.title("Average selling Prices and Ratio of Students to Teachers")
plt.xlabel("PTRATIO")
plt.ylabel("Prices")
plt.show()