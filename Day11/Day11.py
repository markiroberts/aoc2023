# python -m venv advent
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser  
# .\advent\Scripts\activate
# source ./advent/bin/activate
# python.exe -m pip install --upgrade pip
# pip install -r requirements.txt
# pip install matplotlib
# pip install numpy

import os

class itemlist:
    def __init__(self):
        self.list = []

    def additem(self, item):
        if item not in self.list:
            self.list.append(item)

    def addsorteditem(self, item):
        a = item[0]
        b = item[1]
        if a > b:
            item = [b,a]
        else:
           item = [a,b]
        if item not in self.list:
            self.list.append(item)

def rowEmpty(row=0):
 
    boEmpty = True
    for universe in universelist.list:
        if universe[1] == row:
            boEmpty = False
            break
    return boEmpty

def columnEmpty(col=0):
 
    boEmpty = True
    for universe in universelist.list:
        if universe[0] == col:
            boEmpty = False
            break
    return boEmpty
    

#filename = './Day11/example11.txt'
filename = './Day11/day11.txt'
file = open(filename,'r', encoding='utf8').read().split('\n')    
print("Reading:", filename)       
width= 0
height = 0
array = []
# Loop through each line via file handler
for line in file:
    if line:
        if line[0] != '\'':
            array.append(line)
            if (len(line) > width):
                width = len(line) 
height = len(array)
            
universelist = itemlist()

for y in range(height):
    line = array[y]
    for x in range(len(line)):
        if line[x] == "#":
            pairitem = [x,y]
            universelist.additem(pairitem)

for y in range(height):
    print (array[y], rowEmpty(y))

print (universelist.list)
print ("Expand universe")
expandeduniverselist = itemlist()
for universeindex in range(len(universelist.list)):
    x = universelist.list[universeindex][0]
    y = universelist.list[universeindex][1]
    pairitem = [x,y]
    expandeduniverselist.additem(pairitem)

for y in reversed(range(height)):
    if (rowEmpty(y)):
        height = height + 1
        for universeindex in range(len(universelist.list)):
            universe            = universelist.list[universeindex]
            expandeduniverse    = expandeduniverselist.list[universeindex]
            if universe[1] > y:
                expandeduniverse[1] = expandeduniverse[1] + 1000000 - 1
#        line = array [height-2]
#        array.append(line) 
#        for ymove in reversed(range(y,height-1)):
#            array[ymove] = array[ymove-1]
#        array[y] = array[y+1]

for x in reversed(range(width)):
    if (columnEmpty(x)):
        for universeindex in range(len(universelist.list)):
            universe            = universelist.list[universeindex]
            expandeduniverse    = expandeduniverselist.list[universeindex]
            if universe[0] > x:
                expandeduniverse[0] = expandeduniverse[0] + 1000000 - 1
#        for y in range(height):
#            lineleft = array[y][:x] 
#            lineright = array[y][x:]      
#            line = lineleft + "." + lineright
#            array[y] = line

#for y in range(height):
#    print (array[y], rowEmpty(y))

print (universelist.list)
print (expandeduniverselist.list)

totaldistance = 0
pairs = 0
universecount = len(expandeduniverselist.list)
for universeindex in range(universecount):
    for otheruniverseindex in range(universeindex+1, universecount):
        delta_x = expandeduniverselist.list[universeindex][0] - expandeduniverselist.list[otheruniverseindex][0]
        delta_y = expandeduniverselist.list[universeindex][1] - expandeduniverselist.list[otheruniverseindex][1]
        distance = abs(delta_y) + abs(delta_x)
        totaldistance = totaldistance + distance
        print(expandeduniverselist.list[universeindex], " -> ", expandeduniverselist.list[otheruniverseindex], " delta ", delta_x, delta_y, "distance ", distance, "total", totaldistance)
        pairs = pairs + 1

print("Pairs", pairs, "Total Distance", totaldistance)
