#Uses python3

import sys

def dfs(adj, used, order, x):
    #write your code here
    used[x] = 1
    for neighbour in adj[x] :
      if used[neighbour] == 0:
         dfs(adj,used,order,neighbour) 
    order.insert(0,x)

    return used,order


def toposort(adj):
    visited = [0] * len(adj)
    order = []
    n = len(adj) - 1
    #write your code here
    for node in range(len(adj)) :
      if visited[node] == 0:
         visited,order = dfs(adj,visited, order,node)
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

