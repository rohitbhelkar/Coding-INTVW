#Uses python3

import sys

sys.setrecursionlimit(200000)

def dfs(node,adj,visited,stack) :

    visited[node] = 1  
    for neighbour in adj[node] :
        if visited[neighbour] == 1:
           continue
        if visited[neighbour] == 0:
           visited[neighbour] = 1
        visited,stack = dfs(neighbour,adj,visited,stack)
    stack.insert(0,node)
    return (visited,stack)
def reverseGraph(adj) :
    
    reverseAdj = ['']*len(adj)

    for node in range(len(adj)):
        for neighbour in adj[node] :
            if reverseAdj[neighbour] == '' :
               reverseAdj[neighbour] = [node]
            else:
               reverseAdj[neighbour].append(node)

    return reverseAdj           

def dfs_mod(source,visited,node,reverseAdj,index,ccList) :

    visited[node] = 1
    
    #print("node: %s neighbour: %s " %(node,reverseAdj[node]))
    for neighbour in reverseAdj[node] :
        if visited[neighbour] == None :
           ccList[index].append(neighbour)
           ccList[index].sort()
           dfs_mod(source,visited,neighbour,reverseAdj,index,ccList) 
           
    return 1 

def getConnectedComponents(reverseAdj,stack) :
    visited = [None]*len(adj)
    
    index = 0
    ccList = [None]*len(adj)
    result = 0
    while len(stack) != 0 :
      currentNode = stack.pop(0)
      if visited[currentNode] == 1:
         continue
       
      ccList[index] = [currentNode] 
      result += dfs_mod(currentNode,visited,currentNode, reverseAdj,index,ccList)
      index += 1
           
    #for x in ccList:
    #   if x != None:
    #      print x
    return result      


def number_of_strongly_connected_components(adj):
    result = 0
    #write your code here 
    visited = [0] * len(adj)
    stack = []

    for node in range(len(adj)) :
        if visited[node] == 0 :
           visited, stack = dfs(node,adj,visited,stack)
    #for x in stack :
    #    print x
    reverseAdj = reverseGraph(adj)
    #for x in reverseAdj:
    #    print x
    result = getConnectedComponents(reverseAdj,stack)
    #print("adj: %s" %(adj))
    #print("reverseAdj: %s" %(reverseAdj))
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
    print(number_of_strongly_connected_components(adj))