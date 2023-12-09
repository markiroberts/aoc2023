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
        array_row = array[py]
        if ( len(array_row) > px ):
            return array[py][px]

def add_mapping(mapping_from, mapping_to, source, destination, range ):
#            item = [mapping_from, mapping_to, mapping_source_from + x, mapping_destination_from + x]
    for mapping_item in maplist:
        if mapping_item[1] == mapping_from and mapping_item[2] == mapping_to:
            mapping_item.append([source, destination, range])

def find_mapping(mapping_from, mapping_to, source):
    for mapping_item in maplist:
        if mapping_item[1] == mapping_from and mapping_item[2] == mapping_to:
            for mapping in mapping_item[3:]:
                offset = source - mapping[0]
                range = mapping[2]
                destination_start = mapping[1]
                if offset >= 0 and offset < range:
                    return destination_start + offset
    return source
        
def addseedproperty(sourceseed, mapping_to, destination):
#    print("addseedproperty", source, mapping_to, destination)
    item = [mapping_to, destination]
    for seed in seedlist:
        if seed[0] == sourceseed:
            seed.append(item)

def getseedproperty(sourceseed, mapping_to):
#    print("addseedproperty", source, mapping_to, destination)
#    item = [mapping_to, destination]
    for seed in seedlist:
        if seed[0] == sourceseed:
            for seedproperty in seed[1:]:
                if seedproperty[0] == mapping_to:
                    return seedproperty[1]
                
handtypedict = {
    "Five of a kind":  7,
    "Four of a kind":  6,
    "Full house":      5,
    "Three of a kind": 4,
    "Two pair":        3,
    "One pair":        2,
    "High card":       1
}
                
cardvalue = [
  {'card': '0', 'value': 0},
  {'card': '1', 'value': 1},
  {'card': '2', 'value': 2},
  {'card': '3', 'value': 3},
  {'card': '4', 'value': 4},
  {'card': '5', 'value': 5},
  {'card': '6', 'value': 6},
  {'card': '7', 'value': 7},
  {'card': '8', 'value': 8},
  {'card': '9', 'value': 9},
  {'card': 'T', 'value': 10},
  {'card': 'J', 'value': 11},
  {'card': 'Q', 'value': 12},
  {'card': 'K', 'value': 13},
  {'card': 'A', 'value': 14}
]
                
def getcardvalue(e):
   if e >= '0' and e <= '9':
       return int(e)
   elif e == 'T':
       return 10
   elif e == 'J':
       return 11
   elif e == 'Q':
       return 12
   elif e == 'K':
       return 13
   elif e == 'A':
       return 14
   else:
       return 99

def getsortedcards(cards):
    cardlist = []
    sortedcards = ""
    for position in range(len(cards)):
        onecard = cards[position]
        cardlist.append(onecard)
        cardlist.sort(key=getcardvalue, reverse=True)
    for position in range(len(cardlist)):
        onecard = cardlist[position]
        sortedcards = sortedcards + onecard
    return sortedcards

def gethandvalue_cardsbet(cardsbet):
    return (gethandvalue(cardsbet[0]))

def gethandvalue(cards):
    handtype = gethandtype(cards)
    handtypevalue = handtypedict[handtype]
    handvalue = handtypevalue * 10000000000  + getcardvalue(cards[4]) + ( 100 * getcardvalue(cards[3]) ) + ( 10000 * getcardvalue(cards[2]) ) + ( 1000000 * getcardvalue(cards[1]) ) + ( 100000000 * getcardvalue(cards[0]) )
    return(handvalue)
                    
def gethandtype(cards):
    sortedcards = getsortedcards(cards)
    if (sortedcards[0] == sortedcards[1] == sortedcards[2] == sortedcards[3] == sortedcards[4]):
        return 'Five of a kind'
    
    elif (sortedcards[0] == sortedcards[1] == sortedcards[2] == sortedcards[3]):
        return 'Four of a kind'
    elif (sortedcards[1] == sortedcards[2] == sortedcards[3] == sortedcards[4]):
        return 'Four of a kind'
    
    elif (sortedcards[0] == sortedcards[1] == sortedcards[2] and sortedcards[3] == sortedcards[4] ):
        return 'Full house'
    elif (sortedcards[0] == sortedcards[1] and sortedcards[2] == sortedcards[3] == sortedcards[4] ):
        return 'Full house'    
    
    elif (sortedcards[0] == sortedcards[1] == sortedcards[2]):
        return 'Three of a kind'
    elif (sortedcards[1] == sortedcards[2] == sortedcards[3]):
        return 'Three of a kind'   
    elif (sortedcards[2] == sortedcards[3] == sortedcards[4]):
        return 'Three of a kind'  
    
    elif (sortedcards[0] == sortedcards[1] and sortedcards[2] == sortedcards[3] ):
        return 'Two pair'
    elif (sortedcards[0] == sortedcards[1] and sortedcards[3] == sortedcards[4] ):
        return 'Two pair' 
    elif (sortedcards[1] == sortedcards[2] and sortedcards[3] == sortedcards[4] ):
        return 'Two pair' 
    
    elif (sortedcards[0] == sortedcards[1]):
        return 'One pair'
    elif (sortedcards[1] == sortedcards[2]):
        return 'One pair' 
    elif (sortedcards[2] == sortedcards[3]):
        return 'One pair'   
    elif (sortedcards[3] == sortedcards[4]):
        return 'One pair'       
    else:
        return 'High card'



# Get the file handler
#filename = './Day07/example07.txt'
filename = './Day07/day07.txt'
#filename = './Day07/another.txt'

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
handbetlist = []

#32T3K 765
for line in array:
#    splitline = re.split(r'[(+*@)&=.#-/]', line)
#    splitline = re.split( r'[(.=*$#+%/@)-]', line)
#    print (line)
    if line == '':
        mapping = ''
        mapping_from = ''
        mapping_to = ''
    else:
        if line[0] == '#':
            continue

#32T3K 765
        before_space = line.split(" ",1)[0].strip()
        after_space = line.split(" ",1)[1].strip()
        hand = before_space
        bet = after_space
        item=[hand,bet]
        handbetlist.append(item)

print("Cards")
for handbed in handbetlist:
    cards = handbed[0]
    handtype = gethandtype(cards)
    handvalue = gethandvalue(cards)
    print(cards, handtype, handvalue)

handbetlist.sort(key=gethandvalue_cardsbet)

totalwinnings = 0
rank = 1
print("Ranked hands worst first")
for handbet in handbetlist:
    cards = handbet[0]
    bet = int(handbet[1])
    handtype = gethandtype(cards)
    handvalue = gethandvalue(cards)
    print(cards, handtype, handvalue, "Rank:", rank, "Bet:", bet)
    totalwinnings = totalwinnings + (bet * rank)
    rank = rank + 1

print ("Total winnings", totalwinnings)