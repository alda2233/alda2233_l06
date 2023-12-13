"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-10-27"
-------------------------------------------------------
"""
# Imports
from functions import statistics
# Constants
n = int(input("Enter the number of values to process: "))
minimum, maximum, total, average = statistics(n)

if minimum is not None:
    print(f"({minimum:.2f}, {maximum:.2f}, {total:.2f}, {average:.2f})")
