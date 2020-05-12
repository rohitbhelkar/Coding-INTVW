#Uses python3

import sys
import heapq
def findInHeap(minHeap,node) :
    for x in minHeap :
      if x[1] == node:
         return x[0]
    return 0   
def findEdgeCost(adj,cost,node,neighbour) :
    index = adj[node].index(neighbour) 
    return cost[node][index]
def updateMinHeap(minHeap,node,cost) :
    for index in range(len(minHeap)):
        if minHeap[index][1] == node:
           minHeap[index][0] = cost
           return minHeap
    return minHeap 

def negative_cycle(adj, cost):
    #write your code here
    visited = []
    visited = [99999999 for _ in range(n)]
    visited[0] = 0
    parentMapDict = {}
    parentMapDict[0] = ''
    for iteration in range(len(adj) - 1) :
        for source in range(len(adj)) :
          for dest in adj[source] :
          
              costOfSource = visited[source]
              costOfDest = visited[dest]

              edgeCost = findEdgeCost(adj,cost,source,dest)

              if costOfDest > costOfSource + edgeCost:
                 visited[dest] = costOfSource + edgeCost
                 parentMapDict[dest] = source
    for source in range(len(adj)) :
      for dest in adj[source] :
          
          costOfSource = visited[source]
          costOfDest = visited[dest]

          edgeCost = findEdgeCost(adj,cost,source,dest)

          if costOfDest > costOfSource + edgeCost:
             visited[dest] = costOfSource + edgeCost
             return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
