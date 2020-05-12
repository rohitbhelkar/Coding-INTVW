#Uses python3
import sys
import math
from collections import defaultdict
from collections import defaultdict


class Node:
    '''
    A simple node class which stores rank and parent, for use in Disjoint Sets.
    By default, the parent is set to itself, unless a new parent is added.
    '''
    def __init__(self, rnk, d):
        self.rank = rnk
        self.parent = self
        self.data = d
        self.size = 1


class DisjointSet:
    '''
    A disjoint set datastructure, for implementing union find operations.
    '''

    def __init__(self):
        # The members dictionary hashes the value to the corresponding node
        self.members = dict()

    '''
    Input: Value to be retrieved from sets.
    Output: Node corresponding to the value if it is present, None otherwise.
    '''
    def get(self, val):
        if val in self.members:
            return self.members[val]
        else:
            return None

    def make_set(self, val):
        if val not in self.members:
            # The rank is initially 0 since it is a new set
            self.members[val] = Node(0, val)

    '''
    Takes input of a given node in the members dictionary.
    Returns the root of its set.
    '''
    def find(self, n):
        if n.parent != n:
            self.members[n.data].parent = self.find(n.parent)
        return n.parent

    def union(self, n1, n2):
        root_n1 = self.find(n1)
        root_n2 = self.find(n2)

        if root_n1 == root_n2:
            return True
        else:
            if root_n1.rank > root_n2.rank:
                self.members[root_n1.data].size += self.members[root_n2.data].size
                self.members[root_n2.data].parent = self.members[root_n1.data]
            elif root_n1.rank < root_n2.rank:
                self.members[root_n2.data].size += self.members[root_n1.data].size
                self.members[root_n1.data].parent = self.members[root_n2.data]
            else:
                self.members[root_n1.data].size += self.members[root_n2.data].size
                self.members[root_n2.data].parent = self.members[root_n1.data]
                self.members[root_n1.data].rank = root_n1.rank+1
def minimum_distance(x, y):
    result = 0.
    mapCoords = defaultdict()
    distList = [] 
 
    #write your code here
    ds  = DisjointSet()
    for i in range(len(x)) :
      mapCoords[i] = [x[i] , y[i]]
      #rprint("i= %s %s , %s" %(i,x[i],y[i]))
      ds.make_set(i)
      
    for start in range(len(x)):
      for end in range(start + 1 ,len(x)):
        xstart,ystart = mapCoords[start][0],mapCoords[start][1]
        xend,yend     = mapCoords[end][0],mapCoords[end][1]
        dist = math.sqrt(math.pow(xstart - xend,2) + (math.pow(ystart - yend,2)))
        distList.append([start,end,dist])
    distList.sort(key=lambda x:x[2])
    for edge in distList:
        node1 = ds.get(edge[0])
        node2 = ds.get(edge[1])
        node1Parent = ds.find(node1)
        node2Parent = ds.find(node2)
        #rprint("---------------------\n")
        #rprint("Before Node1Repr = %s Node2Repr = %s" %(node1Parent.data,node2Parent.data))
        if node1Parent != node2Parent:
           result += edge[2]
           ds.union(node1,node2)
           #rprint("Edge = %s" %(edge))

           #rprint("After Node1Repr = %s Node2Repr = %s" %(node1Parent.data,node2Parent.data))

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
