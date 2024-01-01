# Using "a Python dictionary to act as an adjacency list
graph = "???.### 1,1,3"
graph = "? 1"

connections = []

def combinations(graph, broken, lengthbroken, combossofar, wherefrom):
   print("combinations graph", graph, "broken", broken, "lengthbroken", lengthbroken, "where from", wherefrom)
   combos = None
   combos_end = None
   combos_broken = None
   if graph:
        char = graph[0]
        if char in '.?':
            if lengthbroken:
                if broken:
                    if lengthbroken == broken[0]:
                        mygraph = graph 
                        mygraph = mygraph[1:]
                        combos_end  = combinations(mygraph, broken[1:],0, combossofar, "end")  
                    else:
                        combos_end = None
                else:
                    combos_end = combossofar
        if char in '#?':
            lengthbroken = lengthbroken + 1
            combos_broken = combinations(graph[1:], broken, lengthbroken, combossofar, "broken")  

        if combos_end and combos_broken:
            combos = combossofar * 2
        elif combos_end or combos_broken:
            combos = combossofar 
   else:
       if len(broken) == 0:
           combos = combossofar

   print("Return combos", combos, "combos_end", combos_end, "combos_broken", combos_broken, "for graph", graph, "broken", broken, "lengthbroken", lengthbroken, "combossofar", combossofar )
   return combos

combos = combinations( "??.", [1], 0, 1, "init" )
print(combos)
      
                 
 