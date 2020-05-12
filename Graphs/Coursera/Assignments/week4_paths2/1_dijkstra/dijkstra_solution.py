#Uses python3

import sys
import queue
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

def distance(adj, cost, s, t):
    #write your code here
    weight_index = 0
    node = 1
    visited = []
    visited = [-1 for _ in range(n)]
    minHeap = [[float('inf'),_] for _ in range(n)]
    minHeap[s] = [0,s]
    parentMapDict = {}
    heapq.heapify(minHeap)
    while len(minHeap) != 0:
        smallest = heapq.heappop(minHeap)
        #print("============ node = " + str(smallest[node]))
        if smallest[node] == s:
           parentMapDict[s] = ''
           visited[s] = 0
        else :
           visited[smallest[node]] = smallest[weight_index]
           
        for neighbour in adj[smallest[node]] :
            if visited[neighbour] != -1 :
               continue
            current_cost_to_reach_neighbour = findInHeap(minHeap,neighbour) 
            smallestNodetoNeighbourEdgeCost = findEdgeCost(adj,cost,smallest[node],neighbour)
            if current_cost_to_reach_neighbour > visited[smallest[node]] + smallestNodetoNeighbourEdgeCost :
              minHeap =  updateMinHeap(minHeap,neighbour,visited[smallest[node]] + smallestNodetoNeighbourEdgeCost)
              heapq.heapify(minHeap)
              parentMapDict[s] = smallest[node]
    if visited[t] == float('inf') :
       return -1    
    return visited[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
