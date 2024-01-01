# Using a Python dictionary to act as an adjacency list
graph = [1, 1, 1, 10, 9, 4, 10,11,9,12,4,5,6,11,12,4,6,1,6,12]

connections = []

def longestpathto(node, listtonode):  #function for dfs 
    print("longestpathto node: ", node, "listnode", listtonode)
    maxlength = -1
    maxlistnode = []
    for fromnode in range(node):
      if node in connections[fromnode]:
        if (fromnode >= 0):
          fromlist = listtonode.copy()
          if fromnode not in fromlist:
            fromlist.append(fromnode)
            length, fromlist = longestpathto(fromnode, fromlist)
            if length > maxlength:
              maxlength = length
              maxlistnode = fromlist.copy()
              maxlistnode =  maxlistnode + [fromnode] 
    maxlength = maxlength + 1
    print("longestpathto return: maxlength", maxlength, "maxlistnode", maxlistnode)
    return maxlength, maxlistnode       

def getconnections():
  for x in range(len(graph)):
      connectionfornode = []
      connections.append(connectionfornode)
      for y in range(x+1, len(graph)):
          if graph[y] > graph[x]:
              connections[x].append(y)
# Driver Code
getconnections()
print(graph)
#print(connections)

maxlenth = -1
longestpath = []
for k in range(7):
  length, fromlist = longestpathto(k, [k])
  length = length + 1
  fromlist.append(k)
  if (length > maxlenth):
     maxlenth = length
     longestpath = fromlist.copy()
  print(k, length, fromlist)

first = True
print("Longest:", maxlenth, longestpath)
for x in longestpath:
   if (first):
     print(graph[x], end="")
     first = False
   else:
     print(" > ", graph[x], end="")
 