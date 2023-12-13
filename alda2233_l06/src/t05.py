"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""
# Imports
from functions import draw_rectangle
# Constants
height = int(input("Enter the height of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
char = input("Enter the character to draw with: ")
draw_rectangle(height, width, char)
