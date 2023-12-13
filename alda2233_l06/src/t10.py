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
from functions import treadmill
# Constants

burnt_per_minute = float(input("Enter calories burnt per minute: "))
start = int(input("Enter start time in minutes: "))
end = int(input("Enter end time in minutes: "))
inc = int(input("Enter increment in minutes: "))

treadmill(burnt_per_minute, start, end, inc)
