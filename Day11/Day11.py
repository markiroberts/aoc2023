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
        a = item[0]
        b = item[1]
        if a > b:
            item = [b,a]
        else:
           item = [a,b]
        if item not in self.list:
            self.list.append(item)


filename = './Day11/example11.txt'
file = open(filename,'r', encoding='utf8').read().split('\n')    
print("Reading:", filename)       
width= 0
height = 0
array = []
# Loop through each line via file handler
for line in file:
    if line:
        if line[0] != '#':
            array.append(line)
            if (len(line) > width):
                width = len(line) 
height = len(array)
            
universelist = itemlist()

for y in range(height):
    line = array[y]
    print (line)
    for x in range(len(line)):
        if line[x] == "#":
            pairitem = [x,y]
            universelist.additem(pairitem)

print (universelist.list)

mylist = itemlist()
pairitem = [1,2]
mylist.additem(pairitem)
pairitem = [3,3]
mylist.additem(pairitem)
pairitem = [3,4]
mylist.additem(pairitem)
pairitem = [4,3]
mylist.additem(pairitem)
pairitem = [3,43123]
mylist.additem(pairitem)
print (mylist.list)


