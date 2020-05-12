#Uses python3

import sys
import queue

def bipartite(adj):
    #write your code here
    black = 1
    white = 0
    colored = [2]*len(adj)
    visited = [0]*len(adj)
    Queue = []
    Queue.insert(-1,0)
    

    while len(Queue) != 0 :
       
       node = Queue.pop(0)
       if visited[node] == 1:
          continue
       visited[node] = 1
       if colored[node] == 2:
          colored[node] = black
          node_color = black
          neighbour_color = white
       elif colored[node] == 1:
          node_color = black
          neighbour_color = white
       elif colored[node] == 0:
          node_color = white
          neighbour_color = black
       for neighbour in adj[node] :
           Queue.insert(-1,neighbour)
           if colored[neighbour] == 2:
              colored[neighbour] = neighbour_color
           elif colored[neighbour] != neighbour_color:
              return 0


    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
