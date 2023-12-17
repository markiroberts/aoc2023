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
        self.list = ()

    def additem(self, item):
        if item not in self.list:
            if type(self.list) is tuple:
                self.list = self.list + (item,)
            else:
                self.list.append(item)

    def list(self):
        for x in self.list:
            print(x)

    def __repr__(self):
        if type(self.list) is tuple:
            string = "("
        else:
            string = "["

        for x in self.list:
            if len(string) > 1:
                string = string + ", "
            string = string + "{}".format(x)
        if type(self.list) is tuple:
            string = string + ")"
        else:
            string = string + "]"
 
#        string = "{}".format(type(self.list)) + " " + string
        return  string 

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

def getcombinations(combinations, defectrun, condition, broken):
    print(combinations, defectrun, condition, broken)
    if (defectrun == 2):
        print("Hello")
# ???.###                   [1, 1, 3] 
    if len(condition) == 0:
        if broken[0] == defectrun and len(broken) == 1:
            defectrun = 0
            return combinations + 1
    else:    
#        for char in range(len(condition)):
        #   print (condition[char])
            x = condition[0]
            if x in '.?':
                if defectrun:
                    newcombos = getcombinations(combinations, defectrun, condition[1:], broken[:1])
                    if newcombos:
                        combinations = combinations + newcombos
                    defectrun = 0
                else:
                    newcombos = getcombinations(combinations, defectrun, condition[1:], broken[:1])
                    if newcombos:
                        combinations = combinations + newcombos
            
            if x in '#?':
                defectrun = defectrun + 1
                newcombos = getcombinations(combinations, defectrun, condition[1:], broken[:1])
                if newcombos:
                    combinations = combinations + newcombos

            return combinations

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
    partbroken = [int(n) for n in brokenlengths.split(",")]
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
    astring = "{:<5} {:<25} {} \t unknownlist: {}".format(y, conditionlist[y], brokenlist[y], unknownlist[y] )
    print(astring)#,  '\t', brokenlist[y], '\t', unknownlist[y].list,)

y = 0
condition = conditionlist[y]
broken = brokenlist[y]
unknown = unknownlist[y]
condition = '.##?.'
broken = [3]
unknown = []
print("...")
print(condition, broken, unknown)
combinations = 0
defectrun = 0
print(getcombinations(combinations, defectrun, condition,broken   ))
        

