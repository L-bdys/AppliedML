import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


num = [1, 2, 3, 4,]
sqr = map(lambda x: x**2, num)
# print(list(sqr))
# Output: [1, 4, 9, 16]

arr = np.array([1, 2, 3, 4,])
sqr_arr = np.square(arr)
# print(sqr_arr)
# Output: [ 1  4  9 16]

ones = np.ones((2, 3))
# print(ones)
# Output:
# [[1. 1. 1.]
#  [1. 1. 1.]]

zeros = np.zeros((2, 3))
# print(zeros)
# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]]

random_arr = np.random.rand(2, 3)
# print(random_arr)
# Output: A 2x3 array with random values between 0 and 1
# Example Output:
# [[0.5488135  0.71518937 0.602763
#  [0.54488318 0.4236548  0.64589411]]

identity = np.eye(3)
# print(identity)
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# Additional examples of NumPy functionalities
arr_sum = np.sum(arr)
# print(arr_sum)
# Output: 10

arr_mean = np.mean(arr)
# print(arr_mean)
# Output: 2.5

arr_reshaped = arr.reshape((2, 2))
# print(arr_reshaped)
# Output:
# [[1 2]
#  [3 4]]

# Additional examples of NumPy functionalities
arr_transposed = arr_reshaped.T
# print(arr_transposed)
# Output:
# [[1 3]
#  [2 4]]

arr_dot = np.dot(arr_reshaped, arr_transposed)
# print(arr_dot)


#--------------------------------------------------------------------------------------

db = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    }
df = pd.DataFrame(db)
# print(df)
# Output:
#       Name  Age         City
# 0    Alice   24     New York
# 1      Bob   27  Los Angeles
# 2  Charlie   22      Chicago
# 3    David   32      Houston

age_mean = df['Age'].mean()
# print(age_mean)
# Output: 26.25

age_filtered = df[df['Age'] > 25]
# print(age_filtered)
# Output:
#     Name  Age         City
# 1    Bob   27  Los Angeles
# 3  David   32      Houston

# Adding a new column
df['Age in 5 Years'] = df['Age'] + 5
# print(df)
# Output:
#       Name  Age         City  Age in 5 Years
# 0    Alice   24     New York               29
# 1      Bob   27  Los Angeles               32
# 2  Charlie   22      Chicago               27
# 3    David   32      Houston               37

# Sorting by Age
df_sorted = df.sort_values(by='Age')
# print(df_sorted)
# Output:
#       Name  Age         City  Age in 5 Years
# 2  Charlie   22      Chicago               27
# 0    Alice   24     New York               29
# 1      Bob   27  Los Angeles               32
# 3    David   32      Houston               37

# print(df.iloc[0])   # Print first row of the DataFrame
# Output:
# Name            Alice
# Age                24
# City        New York
# Age in 5 Years     29

# print(df.loc[0])    # Print row with index 0
# Output:
# Name            Alice
# Age                24
# City        New York
# Age in 5 Years     29

# print(df.iloc[:, 0])   # Print all rows of the first column
# Output:
# 0      Alice
# 1        Bob
# 2    Charlie
# 3      David
# print(df.loc[:, 'Name'])  # Print all rows of the 'Name' column
# Output:
# 0      Alice
# 1        Bob
# 2    Charlie
# 3      David


# ------------------------------------------

# data = np.random.randn(1000)
# sns.histplot(data, bins=30, kde=True)
# plt.title('Histogram with KDE')
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.show()

# data = np.random.rand(100, 2)
# sns.scatterplot(x=data[:, 0], y=data[:, 1])
# plt.title('Scatter Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()

data = np.random.rand(10, 12)
sns.heatmap(data, annot=True, fmt=".2f", cmap='viridis')
plt.title('Heatmap')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
# Output: A 10x12 heatmap with annotated values
