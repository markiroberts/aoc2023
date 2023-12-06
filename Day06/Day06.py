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


# Get the file handler
#filename = './Day06/example06.txt'
filename = './Day06/day06c.txt'
#filename = './Day06/another.txt'

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

#Time:      7  15   30
#Distance:  9  40  200

race = 0
mapping = ""
mapping_digits = []
mappinglist = []
maplist = []
seedlist = []
lineinfile = 0
race_time = []
race_record_distance = []
race_record = []

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

    if lineinfile == 0:
        before_colon = line.split(":",1)[0].strip()
        after_colon = line.split(":",1)[1].strip()
        if ( before_colon == 'Time' ):
            race_time = [int(x) for x in after_colon.split()]
        elif ( before_colon == 'Distance' ):
            race_record_distance = [int(x) for x in after_colon.split()]

print(race_time, race_record_distance)
index = 0
for time in race_time:
    item = [time,race_record_distance[index]]
    race_record.append(item)
    index = index + 1

print("Output")
print(race_record)

beaten_ways = []
for race in race_record:
    this_race_record_time = race[0]
    this_race_record_distance = race[1]
    print("Record time: ", this_race_record_time, " Record Distance: ", this_race_record_distance)
    beaten = 0
    for trial_hold in range(this_race_record_time):
        available_time = this_race_record_time - trial_hold
        if available_time > 0:
            launch_speed = trial_hold
            distance_travelled = launch_speed * available_time
            if distance_travelled > this_race_record_distance:
                beaten = beaten + 1
                if beaten % 1000000 == 0:
                    print(trial_hold / this_race_record_time, beaten)
#               print("Beaten: hold ", trial_hold, " Distance ", distance_travelled)
    beaten_ways.append(beaten)

print("beaten", beaten)
print("beaten_ways: ", len(beaten_ways))
combinations = 1
for way in beaten_ways:
#    print(way)
    combinations = combinations * way

print("product of ways ", combinations)


