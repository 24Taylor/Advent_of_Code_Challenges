from itertools import combinations


with open("AoC_Day1.txt") as day1:
    expenses = []
    for item in day1:
        expenses.append(int(item))           
        expenses.sort()                       
        '''This loop firstly puts the numbers in the text file into an empty list (casting the numbers to integer format),
        and then sorts all of the values in the list from smallest to largest.'''
        
    print(expenses, "\n")
    print(f"There are {len(expenses)} entries in this list")
    
    
# PART 1 SOLUTION - Finding the 2 numbers in list that equal 2020 when added: 

    for item in combinations(expenses, 2):
        if item[0] + item[1] == 2020:
            print(f"\n\nPART 1: Found 'em! {item[0]} & {item[1]}")
            print(f"When multiplied, the sum of these 2 values is: {item[0]*item[1]}\n\n")
            

# PART 2 SOLUTION - Finding the 3 numbers in list that equal 2020 when added :
    for item in combinations(expenses, 3):
        if item[0] + item[1] + item[2] == 2020:
            print(f"PART 2: The 3 values in the list that equal 2020 when added together are: {item[0]}, {item[1]} & {item[2]}")
            print(f"The product of these 3 values is: {item[0]*item[1]*item[2]}\n\n")