#Uses python3

import sys

def explore(v,cc,adj,visited,ccNum):
  visited.append(v)
  ccNum[v] = cc
  for vertices in adj[v]:
    if not vertices in visited:
      explore(vertices,cc, adj,visited,ccNum)
  return (visited,ccNum)    
def number_of_components(adj):
    result = 0
    #write your code here
    cc = 1
    visited = []
    ccNum = {}
    for vertices in range(len(adj)):
        if vertices not in visited:
            #print("--->" + str(vertices))
            visited,ccNum = explore(vertices,cc,adj,visited,ccNum)
            cc = cc + 1
    result = cc - 1   
    return result

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
    print(number_of_components(adj))
