# python -m venv advent
# source ./advent/bin/activate
# pip install -r requirements.txt

#import os
#import sys
#import json
#from pathlib import Path
import re

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
       
import re

def element(px, py):
    if ( (px>=0) and (py>=0) and (px<width) and (py<height) ):
        arrayline = array[py]
        if (px>=0) and (px<len(arrayline)):
            return array[py][px]

# Get the file handler
#filename = './Day01/example01.txt'
#filename  = './Day01/example01b.txt'
filename = './Day01/day01.txt'
#filename = './Day01/another.txt'

file = open(filename,'r').read().split('\n')

 
print("Reading:", filename)
lines = len(file)
array = []

width = 0
# Loop through each line via file handler
for line in file:
  array.append(line)
  if ( len(line) > width ):
      width = len(line)

height = len(array)
numbers = [[] for y in range(lines)]   
unique_chars = ""

for x in range(width):
    for y in range(height):
        charvalue = element(x, y)
        if charvalue:
            if not charvalue in unique_chars:
                if not charvalue.isdigit():
                    unique_chars = unique_chars + charvalue

split_pattern = r"[" +  re.escape(unique_chars) + r"]" 

for y in range(height):
    first_digit_pos = 9999
    first_digit = 9999
    last_digit_pos = -1
    last_digit = -1
    
    digits = [['1','one',1],['2','two',2],['3','three',3],['4','four',4],['5','five',5],['6','six',6],['7','seven',7],['8','eight',8],['9','nine',9]]

    for digit in digits:
        to_find = digit[0]
        value = digit[2]

        if to_find in array[y]:
            first_position = array[y].find(to_find)
            last_position = first_position

            while(to_find in array[y][last_position+1:]):
                second_find = array[y][last_position+1:].find(to_find)
                last_position = last_position + second_find + 1

            if first_position < first_digit_pos:
                first_digit_pos = first_position
                first_digit = value
            if last_position > last_digit_pos:
                last_digit_pos = last_position
                last_digit = value
    numbers[y] = [first_digit, last_digit]

total = 0
for numberrow in numbers:
    if numberrow:
        first = numberrow[0]
        last = numberrow[len(numberrow)-1]
        value = ( first * 10 ) + last
#        print(first, last, value)
        total = total + value

print ("Part a : Total with just 1-9 digits:", total)

for y in range(height):
    first_digit_pos = 9999
    first_digit = 9999
    last_digit_pos = -1
    last_digit = -1
    
    digits = [['1','one',1],['2','two',2],['3','three',3],['4','four',4],['5','five',5],['6','six',6],['7','seven',7],['8','eight',8],['9','nine',9]]

    for digit in digits:
        to_find = digit[0]
        value = digit[2]

        if to_find in array[y]:
            first_position = array[y].find(to_find)
            last_position = first_position

            while(to_find in array[y][last_position+1:]):
                second_find = array[y][last_position+1:].find(to_find)
                last_position = last_position + second_find + 1

            if first_position < first_digit_pos:
                first_digit_pos = first_position
                first_digit = value
            if last_position > last_digit_pos:
                last_digit_pos = last_position
                last_digit = value
        to_find = digit[1]
        value = digit[2]
        if to_find in array[y]:
            first_position = array[y].find(to_find)
            last_position = first_position
            len_find = len(to_find)
            while(to_find in array[y][last_position+len_find:]):
                second_find = array[y][last_position+len_find:].find(to_find)
                last_position = last_position + second_find + len_find

            if first_position < first_digit_pos:
                first_digit_pos = first_position
                first_digit = value      
            if last_position > last_digit_pos:
                last_digit_pos = last_position
                last_digit = value
    numbers[y] = [first_digit, last_digit]

total = 0
for numberrow in numbers:
    if numberrow:
        first = numberrow[0]
        last = numberrow[len(numberrow)-1]
        value = ( first * 10 ) + last
        total = total + value

print ("Part b : Total with 1-9 digits and text digits ('one'-'nine'):", total)
