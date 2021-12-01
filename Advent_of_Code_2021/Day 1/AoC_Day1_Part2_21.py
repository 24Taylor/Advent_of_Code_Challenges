import numpy as np
import pandas as pd

# Challenge 1 Part 2: Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

# STEP 1 - Load puzzle data & Convert dataframe values to List object
data = pd.read_csv('AoC_Day1_PuzzleInput.txt', header = None)
input_data = data.loc[:,0].tolist()

# STEP 2 - Copy input data & display first 10 results
part2 = input_data.copy()
print(part2[:10])

# STEP 3 - Creating a 'Sliding Window' and required parameters
'''
Using np.convolve enables a custom 'sliding window' to be created 
which adds up all elements in the window and returns an array with all consecutive results.
'''
part2 = np.convolve(part2,np.ones(3,dtype=int),'valid')
print(type(part2))
print(part2[:10])

# STEP 4 - Combining with code from Part 1 of Challenge (see: AoC_Day1_Part1_21.py for further details)
differences2 = np.diff(part2)
print(differences2[:100])

# Create list comprehensions & display results
number_of_increases2 = [x for x in differences2 if x > 0]
number_of_decreases2 = [x for x in differences2 if x < 0]
number_no_change = [x for x in differences2 if x == 0]
print(f"Where there is no measurement before the first measurement:\n\nThere were a total of {len(number_of_increases2)} three-measurements sliding windows that were larger than the previous sliding sums.")
print(f"There were a total of {len(number_of_decreases2)} three-measurement sliding windows that were smaller than the previous sliding sums.")
print(f"There were a total of {len(number_no_change)} three-measurement sliding windows where there was no change in sum value.")

print("Challenge 1 Pt 2 Complete! - Thankyou, Happy Advent of Code 2021 :D")
