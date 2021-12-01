import numpy as np
import pandas as pd

# Challenge 1: Find how many measurements are larger than the previous measurement?

# STEP 1 - Load puzzle data
data = pd.read_csv('AoC_Day1_PuzzleInput.txt', header = None)

# View data
print(data.describe())
print(data.head())


# STEP 2 - Convert dataframe values to List object
input_data = data.loc[:,0].tolist()

# Count number of elements in list
print(f"There are {len(input_data)} sonar measurements recorded.\n")
print("The measurements recorded are as follows:\n\n",input_data)


# STEP 3: Calculate the difference between list numbers

'''Using np.diff() calculates the differences between the current and previous number in the list. 
* If the current number is less than the previous number, the difference is recorded as a negative value & so indicates a decrease.
* If the current number is greater than the previous number, the difference is recorded as a positive value & so indicates an increase.
'''
differences = np.diff(input_data)

# Print first 100 values of difference to demonstrate.
print(differences[0:100])


# STEP 4: Separate negative and positive values
'''
A For Loop was created to:
1. Separate all the positive numbers (indicating an increase) into 1 list **AND**
2. Separate all the negative numbers (indicating a decrease) into another list.

Overall, this gives us the solution through use of the `len()` function to calculate the number of elements in the increases list.
'''
# Use a loop to separate negative & positive Values
increases = []
decreases = []

for values in differences:
    if values > 0:
        increases.append(values)
    else:
        decreases.append(values)
        
# Adding up the number of elements in each list to give the solution.        
print(len(increases))
print(len(decreases))
print(len(decreases) + len(increases))


# OPTIONAL: Simplifying For Loop into a list comprehension
number_of_increases = [x for x in differences if x > 0]
number_of_decreases = [x for x in differences if x < 0]
print(f"Where there is no measurement before the first measurement:\n\nThere were a total of {len(number_of_increases)} measurements that were larger than the previous number.")
print(f"There were a total of {len(number_of_decreases)} measurements that were smaller than the previous number.")


# ADDITIONAL - Uncomment the following code for interest

# # List showing the values & number of increases
# print(increases)

# # List showing the values & number of decreases
# print(decreases)

print("Challenge 1 Complete! - Thankyou, Happy Advent of Code 2021 :D")
