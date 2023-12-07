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
#    item = [mapping_to, destination]
#   item = [destination]
    index = seedlist.index(sourceseed)
    mapping_index = seedpropertylist.index(mapping_to)
    seedlist[index][mapping_index+1] = destination

#def getseedproperty(sourceseed, mapping_to):
#    for seed in seedlist:
#    print("addseedproperty", source, mapping_to, destination)
#    item = [mapping_to, destination]
#    index = seedlist.index(sourceseed)
#    mapping_index = seedpropertylist.index(mapping_to)
#    return seedlist[index][mapping_index+1]


# Get the file handler
filename = './Day05/example05sh.txt'
#filename = './Day05/day05.txt'
#filename = './Day05/another.txt'

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

mappings = 0
for line in file:
  if ':' in line:
    mappings = mappings + 1

print("mappings: ", mappings)
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

#seeds: 79 14 55 33  (list of seeds to be planted)
#
#X-to-Y map:
#destinationX-to-Y sourceX-to-Y range_length

#seed-to-soil map:
#50 98 2
#52 50 48
#seed-to-soil map:
#destination range start / source range start / range length
#Any source numbers that aren't mapped correspond to the same destination
#seed 0 -> seed-to-soil map: 0   (if only one line 50 98 2)
#seed 1 -> seed-to-soil map: 1   (if only one line 50 98 2)
...
#seed 95 -> seed-to-soil map: 97   (from 52 50 48)
#seed 97 -> seed-to-soil map: 99   (from 52 50 48)
#seed 98 -> seed-to-soil map: 50
#seed 99 -> seed-to-soil map: 51

#[seed-to-soil,79,81]
#[['seed',79],['soil',81]]

row = 0
mapping = ""
mapping_digits = []
mappinglist = []
maplist = []
seedlist = []
seedpropertylist = []

for line in array:
#    splitline = re.split(r'[(+*@)&=.#-/]', line)
#    splitline = re.split( r'[(.=*$#+%/@)-]', line)
    print (line)
    mapping_digits = []
    if line == '':
        mapping = ''
        mapping_from = ''
        mapping_to = ''
    else:
        if line[0] == '#':
            continue

        before_colon = line.split(":",1)[0]
        before_space = line.split(" ",1)[0]
        if ( before_colon == 'seeds' ):
            mapping = 'seeds'
            mapping_from = 'seeds'
            mapping_to = ''
            after_colon = line.split(":",1)[1].strip()
            mapping_digits = [int(x) for x in after_colon.split()]
        elif ( before_space.isdigit() ):
            mapping_digits = [int(x) for x in line.split()]
        else:
            mapping = line.split("map",1)[0].strip()
            mapping_from = mapping.split("-to-",1)[0].strip()
            mapping_to = mapping.split("-to-",1)[1].strip()

#    print(mapping, mapping_from, ' > ', mapping_to, mapping_digits)
    if mapping_to == "":
# list of seeds
        if mapping_from == 'seeds':
            digit = 0
            for x in mapping_digits:
                if digit % 2 == 0:
                    seed = x
                else:
#                    for offset in range(x):
#                        item = [seed+offset, ['seed', seed+offset]]
#                        item = [seed+offset]
                     print("Creating :", seed, x)
                     item = ['seed',seed,'seed',seed,x]
                     print("Created  Item:", item)
                     seedlist.append(item)
                digit = digit + 1
    elif len(mapping_digits) == 0:
#        print("leave default empty no mapping for x return x")
        maplist.append([mapping, mapping_from, mapping_to])
        mappinglist.append([mapping, mapping_from, mapping_to])
        seedpropertylist.append(mapping_to)
#        for x in range(100):
#            item = [mapping_from, mapping_to, x, x]
#            maplist.append(item)
    else:
        #destination range start / source range start / range length
        mapping_destination_from = mapping_digits[0]
        mapping_source_from = mapping_digits[1]        
        mapping_length = mapping_digits[2]  
        add_mapping(mapping_from, mapping_to, mapping_source_from , mapping_destination_from, mapping_length)
#        maplist['from','to',digit_from,digit_to]

print("Output")
#print ("seedlist ",seedlist) 
print ("mappinglist", mappinglist)
#print ("maplist  ",maplist)

for processmapping in maplist:
    newseed = []
#        maplist['from','to',digit_from,digit_to,[mapping],[mapping]]    
    mapping_from_to, mapping_from, mapping_to = processmapping[:3]
    thismappings = processmapping[3:]
    print ("Processing:", mapping_from_to)
# seed = ['seed',79,'seed',79,14]
    seedlist_index = 0
    for seed in seedlist:
        source_property, source_from, target_property, target_from, range = seed
        source_to = source_from + range - 1
        target_to = target_from + range - 1
# if no overlap do nothing, at end make 1:1 mapping to target property
        if ( mapping_from == target_property ):
            for onemapping in thismappings:
                print ("one mapping: ", onemapping, seed )
                if seed:
                    mapping_source_from, mapping_target_from, mapping_range = onemapping
                    mapping_source_to = mapping_source_from + mapping_range - 1
                    mapping_target_to = mapping_target_from + mapping_range - 1
                    print("mapping  : ", mapping_source_from, " - ", mapping_source_to, " maps to ", mapping_target_from, " - ", mapping_target_to, " range ", mapping_range)
                    print("property : ", target_from, " - ", target_to, " range ", range)
                    if mapping_source_to < target_from:
                        print("out of range - mapping below target")
                    if mapping_source_from > target_to:
                        print("out of range - mapping above target")
                    elif mapping_source_to >= target_from and mapping_source_to <= target_to:
                        print("some overlap 1")
                    elif mapping_source_to >= target_from and mapping_source_from <= target_to:
                        if target_from > mapping_source_from and target_to < mapping_source_to:
                            print("Engulfed by mapping")
    #                       source_property, source_from, target_property, target_from, range = seed
    #                       mapping_from = target_property #'soil'
    #                       mapping_source_from, mapping_target_from, mapping_range
                            new_source_property   = source_property #seed ?
                            new_source_from       = source_from     #as engulfed
                            new_target_property   = mapping_to      #soil in first instance
                            new_target_from       = target_from + ( mapping_target_from - mapping_source_from )
                            new_range             = range
    #                       seed = ['seed',79,'seed',79,14]
                            new_item = [new_source_property, new_source_from, new_target_property, new_target_from, new_range]
                            seedlist[seedlist_index] = new_item
                            print(new_item)
                            print(seedlist)
                            seed = None
                        else:
                            print("some overlap 2")
                    else:
                        print("Other?!")
        print("end of mappings what is seed:",seed)
        if seed:
            new_source_property   = source_property #seed ?
            new_source_from       = source_from     #as engulfed
            new_target_property   = mapping_to      #soil in first instance
            new_target_from       = target_from     #unchanged
            new_range             = range
#                       seed = ['seed',79,'seed',79,14]
            new_item = [new_source_property, new_source_from, new_target_property, new_target_from, new_range]
            seedlist[seedlist_index] = new_item
            print("progressed seedlist:", seedlist)
            print("end")
        seedlist_index = seedlist_index + 1
#            maplist[0]
#            ['seed-to-soil', 'seed', 'soil', [98, 50, 2], [50, 52, 48]]
#            destination range start of 50, a source range start of 98, and a range length of 2.
#            50 98 2
#        destination = find_mapping(mapping_from, mapping_to, source)
#            print(mapping_from, source, ' ==> ', mapping_to, destination)
#           addseedproperty(sourceseed, mapping_to, destination)
#
#   else:
#        for seed in seedlist:
#            sourceseed = seed
#            source = getseedproperty(sourceseed, mapping_from)
#            destination = find_mapping(mapping_from, mapping_to, source)
#            addseedproperty(sourceseed, mapping_to, destination)

#print ("seedlist ",seedlist) 
lowestlocation = 99999999999999
for seed in seedlist:
    sourceseed = seed
    mapping_from = 'location'
    property = seed[3]
    print(sourceseed, 'lowest location:\t', property)
    if property:
        if (property < lowestlocation):
            lowestlocation = property
print("Lowest location:\t", lowestlocation)



 
#    card = int(line.split(":",1)[0].split(" ",1)[1]  )
#    try:
#        a, b = line.split(": ")[1].split(" | ")
#    except:
#        print("error")
#    cardnumbers = [int(x) for x in a.split()]
#    mynumbers = [int(x) for x in b.split()]
#
 #   print(line, " > ", card, cardnumbers, mynumbers)
# 
#    matches = 0
#    points = 0
#    for cardnumber in cardnumbers:
#        if cardnumber in mynumbers:
#            matches = matches + 1
#            if points == 0:
#                points = 1
#            else:
#                points = points * 2
#    print (line, ' => ', card, cardnumbers, mynumbers, matches, points)
#    inlist = 1
#    won = 0
#    newcard = [card,matches, points, inlist, won]
#    cards.append(newcard)
#    totalpoints = totalpoints + points

#print ("Part A: ", totalpoints)
#print(cards)
