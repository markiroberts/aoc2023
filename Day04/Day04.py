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
  line = line.replace(":","")
#  line = line.replace("|","")
  line = line.replace("Card ","")
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

#Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
#1 41 48 83 86 17  83 86  6 31 17  9 48 53
#Card   1: 33 56 23 64 92 86 94  7 59 13 | 86 92 64 43 10 70 16 55 79 33 56  8  7 25 82 14 31 96 94 13 99 29 69 75 23

totalpoints = 0
cards = []

for line in array:
#    splitline = re.split(r'[(+*@)&=.#-/]', line)
#    splitline = re.split( r'[(.=*$#+%/@)-]', line)
    line.replace(":","")
#    print(line)
#    splitline = re.split(pattern=split_pattern, string=line)
    splitline = re.split(pattern=r'[ ]', string=line)
    card = splitline[0]
 
    digit = 0
    card = -1
    cardnumbers = []
    mynumbers = []
    mine = False
    for s in splitline:
        if s == '|':
            mine = True
        if s.isdigit():
            digit = digit + 1
            number = int(s)
            if (digit == 1):
                card = number
            elif not mine:
                cardnumbers.append(number)
            elif mine:
                mynumbers.append(number)
 
    matches = 0
    points = 0
    for cardnumber in cardnumbers:
        if cardnumber in mynumbers:
            matches = matches + 1
            if points == 0:
                points = 1
            else:
                points = points * 2
#    print (line, ' => ', card, cardnumbers, mynumbers, matches, points)
    inlist = 1
    won = 0
    newcard = [card,matches, points, inlist, won]
    cards.append(newcard)
 #   print(newcard)
 #   print(cards)
    digit = digit + 1
    totalpoints = totalpoints + points

print ("Part A: ", totalpoints)
#print(cards)

for newcard in cards:
# newcard = [card,matches, points, inlist, won]    
    cardnumber = newcard[0]
    inlist = newcard[3]
    won = newcard[4]
    matches = newcard[1]
    woncard = cardnumber
    for winningcard in range(matches):
        if woncard < len(cards):
            cards[woncard][4] = cards[woncard][4] + ( inlist + won )
        woncard = woncard + 1

totalscratchcards  = 0
for newcard in cards:
    inlist = newcard[3]
    won = newcard[4]
    totalscratchcards = totalscratchcards + inlist + won

print ("Part B: ", totalscratchcards)