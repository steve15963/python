import sys
from queue import PriorityQueue

input = sys.stdin.readline

nodeSize, edgeSize = map(int, input().split())

pq = PriorityQueue()

parent = [i for i in range(nodeSize+1)]

for i in range(edgeSize):
    fr, to, weight = map(int, input().split())
    pq.put((weight, fr, to))

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        
useEdge = 0
result = 0

while useEdge < nodeSize-1:
    weight, fr, to = pq.get()
    if find(fr) != find(to):
        union(fr, to)
        result += weight
        useEdge += 1
        
print(result)
        