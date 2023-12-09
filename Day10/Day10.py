# python -m venv advent
# source ./advent/bin/activate
# pip install -r requirements.txt

#import os
#import sys
#import json
#from pathlib import Path
import re
        
def getdelta(valuelist):
    deltalist = []
    for x in range(len(valuelist) - 1):
        value0 = valuelist[x]
        value1 = valuelist[x+1]
        delta = value1 - value0
        deltalist.append(delta)
    return (deltalist)

def allzero(valuelist):
    for x in valuelist:
        if x != 0:
            return False
    return True

def element(px, py):
    if ( (px>=0) and (py>=0) and (px<width) and (py<height) ):
        array_row = array[py]
        if ( len(array_row) > px ):
            return array[py][px]

# Get the file handler
filename = './Day10/example10.txt'
#filename = './Day10/day10.txt'

file = open(filename,'r').read().split('\n')

 
print("Reading:", filename)
array = []

width= 0
height = 0
# Loop through each line via file handler
for line in file:
  array.append(line)
  if (len(line) > width):
      width = len(line)

height = len(array)

numbers = []
unique_chars = ""

for x in range(width):
    for y in range(height):
        charvalue = element(x, y)
        if charvalue:
            if not charvalue in unique_chars:
                if not charvalue.isdigit():
                    unique_chars = unique_chars + charvalue

print("Unique chars:", unique_chars)
split_pattern = r"[" +  re.escape(unique_chars) + r"]"
print("split_pattern: ", split_pattern)

x = 0
y = 0
 
sequencelist = []
for line in array:
#    splitline = re.split(r'[(+*@)&=.#-/]', line)
#    splitline = re.split( r'[(.=*$#+%/@)-]', line)
#    print (line)
    if not line:
        continue
    elif line[0] == '#':
        continue
    elif len(line) == 0:
        continue
    else:
        sequence = line.split()
        item = []
        for digit in sequence:
            item.append(int(digit))
        sequencelist.append(item)

print(sequencelist)
