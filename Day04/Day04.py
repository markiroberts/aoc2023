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
        return array[py][px]

def partofnumber_with_symbols(px,py):
    for number in numbers_with_symbols:
        start_x = number[1]
        end_x = number[1] +  len(number[0])
        start_y = number[2]

        if (( start_x == px ) and ( start_y == py )):
            return True
        else:
            if start_y == py:
                if px >= start_x and px < end_x: 
                     return True
    return False

def partofnumber_without_symbols(px,py):
    for number in numbers_without_symbols:
        start_x = number[1]
        end_x = number[1] +  len(number[0])
        start_y = number[2]

        if (( start_x == px ) and ( start_y == py )):
            return True
        else:
            if start_y == py:
                if px >= start_x and px < end_x: 
                     return True
    return False

def partofnumber_with_gears(px,py):

    for number in numbers_with_symbols:
        lookfornumber = int(number[0])
        if lookfornumber in  connected_gear_list:
            start_x = number[1]
            end_x = number[1] +  len(number[0])
            start_y = number[2]
            if (( start_x == px ) and ( start_y == py )):
                return True
            else:
                if start_y == py:
                    if px >= start_x and px < end_x: 
                        return True
    return False

# Get the file handler
#filename = './Day04/example04.txt'
filename = './Day04/day04.txt'
#filename = './Day04/another.txt'

file = open(filename,'r').read().split('\n')

 
print("Reading:", filename)
array = []

# Loop through each line via file handler
for line in file:
  array.append(line)

width = len(array[0])
height = len(array)

numbers = []
unique_chars = ""

for x in range(width):
    for y in range(height):
        charvalue = element(x, y)
        if not charvalue in unique_chars:
            if not charvalue.isdigit():
                unique_chars = unique_chars + charvalue

print("Unique chars:", unique_chars)
split_pattern = r"[" +  re.escape(unique_chars) + r"]"
print("split_pattern: ", split_pattern)

x = 0
y = 0

for line in array:
#    splitline = re.split(r'[(+*@)&=.#-/]', line)
#    splitline = re.split( r'[(.=*$#+%/@)-]', line)
    splitline = re.split(pattern=split_pattern, string=line)
    for s in splitline:
        if s.isdigit():
            x = line.find(s)
            newline = line[:x] + "?" + line[x+1:]
            if(len(s))>1:
                newline = newline[:x+1] + "?" + newline[x+2:]
            if(len(s))>2:
                newline = newline[:x+2] + "?" + newline[x+3:]                
            if(len(s))>3:
                newline = newline[:x+3] + "?" + newline[x+4:]  
            line = newline

            numbers.append([s, x, y])
        else:
            if len(s) > 0:
                print("not digit",s)
    y = y + 1

#print (numbers)
total_numbers = 0
numbers_with_symbols = []
numbers_without_symbols = []
if (width > height):
    maxdimension = width
else:
    maxdimension = height

gear1 = [[0 for x in range(maxdimension)] for y in range(maxdimension)]

for number in numbers:
    length = len(number[0])
    number_value = int(number[0])

    number_start_x = number[1]
    number_start_y = number[2]
    leftx = number_start_x - 1
    rightx = number_start_x + length
 
    abovey = number_start_y - 1
    belowy = number_start_y + 1
 
    number_edge = []
    for x in range(leftx, rightx+1):
        y = abovey
        number_edge.append([x, y])
    for x in range(leftx, rightx+1):
        y = belowy
        number_edge.append([x, y])
    number_edge.append([leftx, number_start_y])
    number_edge.append([rightx, number_start_y])

    hasSymbolOnEdge = False
    for edge in number_edge:
        x = edge[0]
        y = edge[1]
        char = element(x, y)
        if char:
            if  char != '.' and not char.isdigit()  :  
               hasSymbolOnEdge = True
            if  char == '*' :  
               newgear =int(number[0])
               if gear1[x][y] == 0:
                   gear1[x][y] = [newgear]
               else:
                   gear1[x][y].append(newgear)
               hasGearOnEdge = True

    if ( hasSymbolOnEdge ):  
        numbers_with_symbols.append([number[0], number_start_x, number_start_y])
        total_numbers = total_numbers + int(number[0])
    else:
        numbers_without_symbols.append([number[0], number_start_x, number_start_y])

connected_gears = []
connected_gear_list = []
for gearrow in gear1:
    for gearcol in gearrow:
        if (gearcol != 0):
            if len(gearcol) >= 2:
                connected_gears.append(gearcol)
                connected_gear_list.append(gearcol[0])
                connected_gear_list.append(gearcol[1])

#print("Numbers with symbols:", numbers_with_symbols )
#print("Numbers without symbols:", numbers_without_symbols)
#print("Gear1:", gear1)
#print("Connected gears:", connected_gears)
#print("connected_gear_list", connected_gear_list)
print("3a Part Number Total:", total_numbers)
total_gear_ratio = 0
for gear in connected_gears:
    total_gear_ratio = total_gear_ratio + (gear[0] * gear[1])
print("3b Gear Ratio Total:", total_gear_ratio)

for y in range(0, height):
    line = ""
    for x in range(0, width):
        if element(x,y):
            if(partofnumber_with_symbols(x,y)):
                if(partofnumber_with_gears(x,y)):
                    print (color.GREEN, element(x,y), sep='', end='' ) 
                else:   
                   print (color.RED, element(x,y), sep='', end='' )
            elif(partofnumber_without_symbols(x,y)):
                print (color.BOLD, element(x,y), sep='', end='' )
            else:
                print (color.END, element(x,y), sep='', end='' )
    print("")
 