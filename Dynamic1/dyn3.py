# Using "a Python dictionary to act as an adjacency list
# L W H
# to stack i on j Li < Lj and Wi < Wj
boxes = [(2,2,3),(3,3,4),(4,4,2)]

stacks = []

def getstacks(theboxes):
    for x in range(len(theboxes)):
        for y in range(len(theboxes)):
            if (boxes[x][0] < boxes[y][0]):  #Length 
                if (boxes[x][1] < boxes[y][1]):  #Width
                    stackitem = (x,y)
                    stacks.append(stackitem) 

def maxheight(boxindexlist):
    thenewboxes = []

    mymaxheight = -1
    for x in range(len(boxindexlist)):
        box = boxindexlist[x]
        for y in range(len(boxindexlist)):
            if x != y:
                stackbox = boxindexlist[y]
                if stackbox in stacks[box]:
                    newboxindexlist = []
                    for z in range(len(boxindexlist)):
                        boxlistindex = boxindexlist[z]
                        if (boxlistindex != stackbox):
                            newboxindexlist.append(boxlistindex)
                    height = boxes[stackbox][2] + maxheight(newboxindexlist)
        if height > mymaxheight:
            mymaxheight = height

    return mymaxheight


getstacks(boxes)
print(stacks)
maxheight([0,1,2])