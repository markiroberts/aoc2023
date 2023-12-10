# python -m venv advent
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser  
# .\advent\Scripts\activate
# source ./advent/bin/activate
# python.exe -m pip install --upgrade pip
# pip install -r requirements.txt
# pip install matplotlib
# pip install numpy

#import os
#import sys
#import json
#from pathlib import Path
import re
import matplotlib.pyplot as plt
import numpy as np

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
        
        
def getcellconnection( character, left, right, up, down ):

    if left:
        enterleft = (1,left)
    else:
        enterleft = ()

    if right:
        enterright = (3,right)
    else:
        enterright = ()

    if up:
        enterup = (2,up)
    else:
        enterup = ()

    if down:
        enterdown = (0,down)
    else:
        enterdown = ()

    match character:
        case '─':
            connection = [(),        enterleft,     (),         enterright]
        case '└':
            connection = [enterright, enterup,           (),    ()        ]
        case '┘':
            connection = [enterleft,  (), (), enterup]
        case '┐':
            connection = [(), (), enterleft,  enterdown]
        case '┌':
            connection = [(), enterdown, enterright,  ()]
        case '.':
            connection = [(), (), (), ()]     
        case '|':
            connection = [enterdown, (), enterup, ()]             
        case 'S':
            connection = [('?')]  
            start = {"x": x, "y": y}          
        case _:
            connection = [('Unknown')] 
            print("Unknown ", character)
    return connection
        
def getanimalrun(pConnectionList, pStart, pFirstDirection):
    nodelist = []
    newNode = pStart
    if not newNode:
        print("uh?")

    connection = pConnectionList[pStart['y']][pStart['x']][pFirstDirection]
    while connection:
        newDirection = connection[0]
        newNode = connection[1]
        if not newNode:
            print("uh?")
 
        new_x = newNode['x']
        new_y = newNode['y']
 

#        print("Enter", newNode, "From", newDirection, " new cell: ", maze[new_y][new_x])
        connection = pConnectionList[newNode['y']][newNode['x']][newDirection]
        nodelist.append(newNode)
        if newNode['x'] == pStart['x'] and newNode['y'] == pStart['y']:
            return(nodelist)
        
def getpossibleconnectionlist(initiallist, startloc, possiblestartchar):
    possibleconnectionlist = initiallist
    x = startloc['x']
    y = startloc['y']
    left_x = x - 1
    right_x = x + 1
    up_y = y - 1
    down_y = y + 1
    noconection = {}
    if (left_x >= 0) and left_x < len(maze[y]):
        left = {"x": left_x, "y": y}
    else:
        left = noconection

    if (right_x >= 0) and right_x < len(maze[y]):
        right = {"x": right_x, "y": y}
    else:
        right = noconection

    if (up_y >= 0) and up_y < len(maze[y]):
        up = {"x": x, "y": up_y}
    else:
        up = noconection

    if (down_y >= 0) and down_y < len(maze[y]):
        down = {"x": x, "y": down_y}
    else:
        down = noconection

    connection = getcellconnection( possiblestartchar, left, right, up, down )

#    match possiblestartchar:
#        case '─':
#            connection = [(),        (1, left),     (),         (3, right)]
#        case '└':
#            connection = [(3, right),  (2, up),     (),           ()        ]
#        case '┘':
#            connection = [(1, left),  (), (), (2, up)]
#        case '┐':
#            connection = [(), (), (1, left),  (0, down)]
#        case '┌':
#            connection = [(), (0, down), (3, right),  ()]
#        case '.':
#            connection = [(), (), (), ()]     
#        case '|':
#            connection = [(0, down), (), (2, up), ()]             
#        case 'S':
#            connection = [('?')]  
#            start = {"x": x, "y": y}          
#        case _:
#            print("Unknown ", possiblestartchar)
    newrow = possibleconnectionlist[y][:x]
    newrow.append(connection)
    newrow.extend(possibleconnectionlist[y][x+1:])
    possibleconnectionlist[y] = newrow

    maze[y][x] = possiblestartchar

    return possibleconnectionlist
        
def getconnectionlist():
    connectionlist = []
    for y in range(len(maze)):
        connectionrow = []
        for x in range(len(maze[y])):
            left_x = x - 1
            right_x = x + 1
            up_y = y - 1
            down_y = y + 1
            noconection = {}
            if (left_x >= 0) and left_x < len(maze[y]):
                left = {"x": left_x, "y": y}
            else:
                left = noconection

            if (right_x >= 0) and right_x < len(maze[y]):
                right = {"x": right_x, "y": y}
            else:
                right = noconection

            if (up_y >= 0) and up_y < len(maze[y]):
                up = {"x": x, "y": up_y}
            else:
                up = noconection

            if (down_y >= 0) and down_y < len(maze[y]):
                down = {"x": x, "y": down_y}
            else:
                down = noconection

            connection = getcellconnection(maze[y][x], left, right, up, down)
            if (maze[y][x] == 'S'):
                 start = {"x": x, "y": y}   

#            match maze[y][x]:
#                case '─':
#                    connection = [(),        (1, left),     (),         (3, right)]
#                case '└':
#                    connection = [(3, right), (),           (2, up),    ()        ]
#                case '┘':
#                    connection = [(1, left),  (), (), (2, up)]
#                case '┐':
#                    connection = [(), (), (1, left),  (0, down)]
#                case '┌':
#                    connection = [(), (0, down), (3, right),  ()]
#                case '.':
#                    connection = [(), (), (), ()]     
#                case '|':
#                    connection = [(0, down), (), (2, down), ()]             
#                case 'S':
#                    connection = [('?')]  
#                    start = {"x": x, "y": y}          
#                case _:
#                    print("Unknown at x,y: ", x, y, maze[y][x])
            connectionrow.append(connection)
        connectionlist.append(connectionrow)
    return connectionlist, start

def checkpossiblestart(initialconnectionlist, start, possiblestartchar):
    possibleconnectionlist = getpossibleconnectionlist(initialconnectionlist, start, possiblestart)
#    print("possiblestart ", possiblestart, "gives:")
    loops = 0
    firstrunnorth = firstrunsouth = firstrunwest = firstruneast = None
    firstrunnorth = getanimalrun(possibleconnectionlist, start, 0)
    firstruneast = getanimalrun(possibleconnectionlist, start, 1)
    firstrunsouth = getanimalrun(possibleconnectionlist, start, 2)
    firstrunwest = getanimalrun(possibleconnectionlist, start, 3)
    if firstrunnorth:
        loops = loops + 1
#        print("North:", firstrunnorth)
    if firstruneast:
        loops = loops + 1
#        print("East:", firstruneast)
    if firstrunsouth:
        loops = loops + 1    
#        print("South:", firstrunsouth)        
    if firstrunwest:
        loops = loops + 1
#        print("West:", firstrunwest)

    if loops >= 2:
        return possibleconnectionlist
    
def showmaze(showconnectionlist, run):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            onTrail = False
            for step in run:
                step_x = step['x']
                step_y = step['y']
                if step_x == x and step_y == y:
                    onTrail = True
            if onTrail:
                print(color.GREEN, maze[y][x], sep='', end="")
            else:
                print(color.BLUE, maze[y][x], sep='', end="")
        print("", sep='', end="\n")
    return "Hello"

def listpath(run):
    for step in run:
        step_x = step['x']
        step_y = step['y']
        print(step_x, step_y)
    step = run[0]
    step_x = step['x']
    step_y = step['y']
    print(step_x, step_y)


def plotpath(plt, run, freepoints, enclosedpoints):
#    plt.style.use('_mpl-gallery')

    x = []
    y = []
    for step in run:
        step_x = step['x']
        step_y = 10-step['y']
        x.append(step_x)
        y.append(step_y)
    step = run[0]
    step_x = step['x']
    step_y = 10-step['y']
    x.append(step_x)
    y.append(step_y)

    freex = []
    freey = []
    freesize = []
    freecolor = []
    for step in freepoints:
        step_x = step['x']
        step_y = 10-step['y']
        freex.append(step_x)
        freey.append(step_y)
        freesize.append(33)
        freecolor.append(3)

    enclosedx = []
    enclosedy = []
    enclosedsize = []
    enclosedcolor = []
    for step in enclosedpoints:
        enclosed_x = step['x']
        enclosed_y = 10-step['y']
        enclosedx.append(enclosed_x)
        enclosedy.append(enclosed_y)
        enclosedsize.append(66)
        enclosedcolor.append('#1f77b4')        

    # plot
#    fig, plots = plt.subplots(nrows=1, ncols=2, sharex=True)

    plt.plot(x, y, linewidth=2.0)
#    plt.set(xlim=(-1,len(maze[0])+1), xticks=np.arange(0, len(maze[0])+1),
#        ylim=(-1,len(maze)+1), yticks=np.arange(0, len(maze)+1))
    
    plt.scatter(freex, freey, s=freesize, c=freecolor, vmin=0, vmax=2)
    plt.scatter(enclosedx, enclosedy, s=enclosedsize, c=enclosedcolor, vmin=0, vmax=2)
#    plt.set(xlim=(-1,len(maze[0])+1), xticks=np.arange(0, len(maze[0])+1),
#        ylim=(-1,len(maze)+1), yticks=np.arange(0, len(maze)+1))

    plt.show()

def getfreepoints(showconnectionlist, run):
    freepoints = []
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            step_in_run = False
            for step in run:
                step_x = step['x']
                step_y = step['y']
                if x == step_x and y == step_y:
                    step_in_run = True
            if not step_in_run:
                freepoint = {"x": x, "y": y}
                freepoints.append(freepoint)
    return(freepoints)

def getenclosedpoints(possibleconnectionlist, run, freepoints):
    lastchar = ''
    enclosedpoints = []
    for point in freepoints:
        enclosed = False
        y = point['y']
        x = point['x']
        for fromleftx in range(0,x):
            onrun = False
            for runstep in run:
                runstep_x = runstep['x']
                runstep_y = runstep['y']
                if runstep_x == fromleftx and runstep_y == y:
                    onrun = True
            if onrun:
                charonpath = maze[y][fromleftx]
                match charonpath:
                    case '┌':
#                        enclosed = not enclosed#True
                        lastchar = charonpath
                    case '└':
#                        enclosed = not enclosed#True
                        lastchar = charonpath
                    case '┐':
                        if (lastchar =='└'):
                            enclosed = not enclosed
                        lastchar = ""
                    case '┘':
                        if (lastchar =='┌'):
                            enclosed = not enclosed
                        lastchar = ""
                    case '|':
                        enclosed = not enclosed
                    case '─':
                        enclosed = enclosed #no change
                    case 'S':
                        print("Start !!!!")
#                    print(color.GREEN, maze[y][x], sep='', end = '')
#            else:
#                print(color.BLUE, maze[y][x], sep='', end = '')
        if enclosed:
            print("enclosed", point)
            enclosedpoints.append(point)
#        print("")
#    enclosedpoints.append(freepoints[2])
#    enclosedpoints.append(freepoints[12])
    print(enclosedpoints)
    return enclosedpoints


# Get the file handler
#filename = './Day10/example10.txt'
#filename = './Day10/example10m.txt'
filename = './Day10/day10.txt'

file = open(filename,'r', encoding='utf8').read().split('\n')


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
 
 
maze = []
mydict = {"-": "─", "L": "└", "J": "┘", "7": "┐", "F": "┌"}
mytable = str.maketrans(mydict)
for line in array:
#    splitline = re.split(r'[(+*@)&=.#-/]', line)
#    splitline = re.split( r'[(.=*$#+%/@)-]', line)
#    print (line)
    if not line:
        continue

    line = line.strip()

    if line[0] == '#':
        continue
    elif len(line) == 0:
        continue
    else:
        line = line.translate(mytable)
        item = []
        for digit in line:
            item.append(digit)
    maze.append(item)

initialconnectionlist, start = getconnectionlist()

print("start x,y", start['x'], ',', start['y'])
print(initialconnectionlist[0])
print(initialconnectionlist[1])
print(initialconnectionlist[2])
print(initialconnectionlist[3])
print(initialconnectionlist[4])

print(initialconnectionlist[start['y']][start['x']])

#  ─ └ ┘ ┐ ┌ S .

possiblestarts = "┌ ─ ┐ └ ┘ |"
 
for possiblestart in possiblestarts.split():
    possibleconnectionlist = checkpossiblestart(initialconnectionlist, start, possiblestart)
    if possibleconnectionlist:
        print("possiblestart:", possiblestart)
        firstrunnorth = getanimalrun(possibleconnectionlist, start, 0)
        firstruneast = getanimalrun(possibleconnectionlist, start, 1)
        firstrunsouth = getanimalrun(possibleconnectionlist, start, 2)
        firstrunwest = getanimalrun(possibleconnectionlist, start, 3)
        maxlength = 0        
        if firstrunnorth:
            if len(firstrunnorth) > maxlength:
                maxlength = len(firstrunnorth) 
        if firstruneast:
            if len(firstruneast) > maxlength:
                maxlength = len(firstruneast) 
        if firstrunsouth:
            if len(firstrunsouth) > maxlength:
                maxlength = len(firstrunsouth) 
        if firstrunwest:
            if len(firstrunwest) > maxlength:
                maxlength = len(firstrunwest) 
        print("Max length:", maxlength)
        print("Max distance:", maxlength/2)
 
        if firstrunnorth:
            showmaze(possibleconnectionlist, firstrunnorth)
            freepoints = getfreepoints(possibleconnectionlist, firstrunnorth)
            enclosedpoints = getenclosedpoints(possibleconnectionlist, firstrunnorth, freepoints)
            plotpath(plt, firstrunnorth, freepoints, enclosedpoints)
        elif firstruneast:
            showmaze(possibleconnectionlist, firstruneast)
            freepoints = getfreepoints(possibleconnectionlist, firstruneast)
            enclosedpoints = getenclosedpoints(possibleconnectionlist, firstruneast, freepoints)
            plotpath(plt, firstruneast, freepoints, enclosedpoints)
        elif firstrunsouth:
            showmaze(possibleconnectionlist, firstrunsouth)
            freepoints = getfreepoints(possibleconnectionlist, firstrunsouth)
            enclosedpoints = getenclosedpoints(possibleconnectionlist, firstrunsouth, freepoints)
            plotpath(plt, firstrunsouth, freepoints, enclosedpoints)     
        elif firstrunwest:
            showmaze(possibleconnectionlist, firstrunwest)
            freepoints = getfreepoints(possibleconnectionlist, firstrunwest)
            enclosedpoints = getenclosedpoints(possibleconnectionlist, firstrunwest, freepoints)
            plotpath(plt, firstrunwest, freepoints, enclosedpoints)

print("Freepoints", len(freepoints) - len(enclosedpoints) )
print("enclosedpoints",  len(enclosedpoints) )
  
  


# 0 - north
# 1 - east
# 2 - south
# 3 - west
#
# A
# LB
# connection([3,B],none,none,[2,A])  --> node connects to south of node A if entering from west and west of node B if entering from north

