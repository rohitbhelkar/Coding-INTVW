#Uses python3

import sys

def isAcyclic(node,adj,visited) :
    if len(adj[node]) == 0:
       return 0
     
    visited.append(node)
    for neighbour in adj[node] :

      if neighbour not in visited:
        if isAcyclic(neighbour,adj,visited) == 1:
           #print("1. neighbour = %s visite=%s" %(neighbour,visited))
           return 1
      elif neighbour in visited:
        #print("2. neighbour = %s visite=%s" %(neighbour,visited))
        return 1
    visited.remove(node)  
    return 0    

def acyclic(adj):
 retVal = 0
 
 for nodeNum in range(len(adj)):
     visited = []
     retVal = isAcyclic(nodeNum,adj,visited) 
     if retVal:
        #print(nodeNum)
        return retVal
 return retVal

if __name__ == '__main__':
  input = sys.stdin.read()
  data = list(map(int, input.split()))
  n, m = data[0:2]
  data = data[2:]
  edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
  adj = [[] for _ in range(n)]
  for (a, b) in edges:
    adj[a - 1].append(b - 1)
  print(acyclic(adj))
  #27-->96-->34-->41-->30-->41