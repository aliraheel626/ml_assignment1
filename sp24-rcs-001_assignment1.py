# 1.1 Create a list: nums = [3, 5, 7, 8, 12], make another list named ‘cubes’ and append the cubes of the given list ‘nums’
# in this list and print it.
import pandas as pd
import numpy as np
nums = [3, 5, 7, 8, 12]
cubes = [x**3 for x in nums]
nums.extend(cubes)
print(nums)

# 1.2. Create an empty dictionary: dict = {}, add the following data to the dictionary: ‘parrot’: 2, ‘goat’: 4, ‘spider’: 8, ‘crab’:
# 10 as key value pairs.
dict = {}
sum_of_legs = 0
dict.update({'parrot': 2})
dict.update({'goat': 4})
dict.update({'spider': 8})
dict.update({'crab': 10})


# 1.3. Use the ‘items’ method to loop over the dictionary (dict) and print the animals and their corresponding legs. Sum
# the legs of each animal, and print the total at the end.
for key, val in dict.items():
    print(f'animal {key} has {val} legs')
    sum_of_legs += val
print(f'total legs: {sum_of_legs}')


# 1.4. Create a tuple: A = (3, 9, 4, [5, 6]), change the value in the list from ‘5’ to ‘8’.
A = (3, 9, 4, [5, 6])
A[3][0] = 8
print(f'new tuple A: {A}')

# 1.5. Delete the tuple A.
del A

# 1.6. Create another tuple: B = (‘a’, ‘p’, ‘p’, ‘l’, ‘e’), print the number of occurrences of ‘p’ in the tuple.
B = ('a', 'p', 'p', 'l', 'e')
print(f'p in B occurs {B.count('p')} times')


# 1.7. Print the index of ‘l’ in the tuple.
print(f'index of l in B is {B.index('l')}')


# 2.1 Convert matrix A into numpy array
A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print("Matrix A:")
print(A)

# 2.2 Use slicing to pull out the subarray consisting of the first 2 rows and columns 1 and 2.
b = A[:2, 1:3]
print("\nSubarray b (first 2 rows, columns 1 and 2):")
print(b)

# 2.3 Create an empty matrix ‘C’ with the same shape as ‘A’.
C = np.empty_like(A)
print("\nEmpty matrix C with the same shape as A:")
print(C)

# 2.4 Add the vector z to each column of the matrix ‘A’ with an explicit loop and store it in ‘C’.
z = np.array([1, 0, 1])
for i in range(A.shape[1]):  # iterate over columns
    C[:, i] = A[:, i] + z
print("\nMatrix C after adding vector z to each column of A:")
print(C)

# 2.5 Add and print the matrices X and Y.
X = np.array([[1, 2],
              [3, 4]])
Y = np.array([[5, 6],
              [7, 8]])
print("\nMatrix X + Matrix Y:")
print(X + Y)

# 2.6 Multiply and print the matrices X and Y (element-wise multiplication).
print("\nElement-wise multiplication of X and Y:")
print(X * Y)

# 2.7 Compute and print the element-wise square root of matrix Y.
print("\nElement-wise square root of matrix Y:")
print(np.sqrt(Y))

# 2.8 Compute and print the dot product of the matrix X and vector v.
v = np.array([9, 10])
print("\nDot product of matrix X and vector v:")
print(np.dot(X, v))

# 2.9 Compute and print the sum of each column of X.
print("\nSum of each column of matrix X:")
print(np.sum(X, axis=0))

# 3.1 Create a function ‘Compute’ that takes two arguments, distance and time, and calculates velocity


def Compute(distance, time):
    # Velocity is distance divided by time
    if time != 0:  # Prevent division by zero
        velocity = distance / time
        return velocity
    else:
        return "Time cannot be zero."


distance = 100  # in meters
time = 10  # in seconds
velocity = Compute(distance, time)
print(f"Velocity: {velocity} meters/second")

# 3.2 Create a list named ‘even_num’ that contains all even numbers up to 12
even_num = [2, 4, 6, 8, 10, 12]

# Create a function ‘mult’ that takes the list ‘even_num’ and calculates the product of all entries


def mult(num_list):
    product = 1
    for num in num_list:
        product *= num
    return product


product_of_evens = mult(even_num)
print(f"Product of all even numbers in the list: {product_of_evens}")


# Creating the dataframe 'pd' with 5 rows and 4 columns
data = {
    'C1': [1, 2, 3, 5, 5],
    'C2': [6, 7, 5, 4, 8],
    'C3': [7, 9, 8, 6, 5],
    'C4': [7, 5, 2, 8, 8]
}
df = pd.DataFrame(data)

# 4.1 Print only the first two rows of the dataframe
print("First two rows:")
print(df.head(2))

# 4.2 Print the second column
print("\nSecond column (C2):")
print(df['C2'])

# 4.3 Change the name of the third column from ‘C3’ to ‘B3’
df.rename(columns={'C3': 'B3'}, inplace=True)
print("\nDataFrame with renamed third column (C3 to B3):")
print(df)

# 4.4 Add a new column to the dataframe and name it ‘Sum’
df['Sum'] = 0  # Initializing the new 'Sum' column
print("\nDataFrame after adding 'Sum' column:")
print(df)

# 4.5 Sum the entries of each row and add the result in the column ‘Sum’
df['Sum'] = df.sum(axis=1)  # Summing each row across all columns
print("\nDataFrame with sum of each row in 'Sum' column:")
print(df)

# 4.6 Read CSV file named ‘hello_sample.csv’ into a Pandas dataframe
# Assuming the file is present in the working directory, adjust the path accordingly.
csv_df = pd.read_csv('hello_sample.csv')

# 4.7 Print complete dataframe
print("\nComplete CSV DataFrame:")
print(csv_df)

# 4.8 Print only bottom 2 records of the dataframe
print("\nBottom 2 records of CSV DataFrame:")
print(csv_df.tail(2))

# 4.9 Print information about the dataframe
print("\nInformation about CSV DataFrame:")
csv_df.info()

# 4.10 Print shape (rows x columns) of the dataframe
print("\nShape of CSV DataFrame (rows x columns):")
print(csv_df.shape)

# 4.11 Sort the data of the dataframe using column ‘Weight’
sorted_df = csv_df.sort_values(by='Weight')
print("\nCSV DataFrame sorted by 'Weight':")
print(sorted_df)

# 4.12 Use isnull() and dropna() methods of the Pandas dataframe and see if they produce any changes
print("\nChecking for null values in CSV DataFrame:")
print(csv_df.isnull())

# Drop rows with missing values
csv_cleaned = csv_df.dropna()
print("\nDataFrame after applying dropna():")
print(csv_cleaned)
