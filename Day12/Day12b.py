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

    def list(self):
        for x in self.list:
            print(x)

def conditionreport(springcondition):
    condition = []
    brokeninarow = 0
    for x in range(len(springcondition)):
        if springcondition[x] == '#':
            brokeninarow = brokeninarow + 1
        else:
            if brokeninarow > 0:
                condition.append(brokeninarow)
                brokeninarow = 0
    if brokeninarow > 0:
        condition.append(brokeninarow)
    return(tuple(n for n in condition))
    return(condition)


filename = './Day12/example12.txt'
#filename = './Day12/day12.txt'
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

unknownlist = []
conditionlist = []
brokenlist = []
            
for y in range(height):
    newlist = itemlist()
    partcondition, brokenlengths = array[y].split(" ")
    partbroken = tuple(int(n) for n in brokenlengths.split(","))
#    broken = partbroken + partbroken + partbroken + partbroken + partbroken
#    condition = partcondition + "?" + partcondition + "?" + partcondition + "?" + partcondition + "?" + partcondition
    broken = partbroken
    condition = partcondition

    print ("Condition:", condition, broken)
    for x in range(len(condition)):
        if condition[x] == '?':
            newlist.additem(x)
    
    unknownlist.append(newlist)
    conditionlist.append(condition)
    brokenlist.append(broken)
    
for y in range(height):
    print(y, unknownlist[y].list)

possiblearrangements = 0
for y in range(height):
#for y in range(1):
    combinations = 2 ** len(unknownlist[y].list)
    possible = conditionlist[y]
    brokentotal = 0
    for x in brokenlist[y]:
        brokentotal = brokentotal + x
    brokenincondition = 0
    for x in range(len(conditionlist[y])):
        char = conditionlist[y][x]
        if char == '#':
            brokenincondition = brokenincondition + 1

    unknownbroken = brokentotal - brokenincondition

 
    broken = brokenlist[y]
 
    for combo in range(combinations):
        unknowns = unknownlist[y].list
        combobroken = 0
        for digit in range(len(unknowns)):
            mask = 2 ** digit
            value = ( combo & mask )  >> digit
            if value:
                combobroken = combobroken + 1

        if combobroken == unknownbroken:
            for digit in range(len(unknowns)):
                mask = 2 ** digit
                value = ( combo & mask )  >> digit
                character = unknowns[digit]
                if value:
                    possible = possible[:character] + '#' + possible[character+1:]
                else:
                    possible = possible[:character] + '.' + possible[character+1:]
            conditioreport = conditionreport(possible)
            if conditioreport == broken:
                possiblearrangements = possiblearrangements + 1

    print("Row ",y, "of ", height-1, " possiblearrangements so far", possiblearrangements)

print("possiblearrangements", possiblearrangements)

