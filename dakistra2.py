import sys
from queue import PriorityQueue

input = sys.stdin.readline

NodeSize, EdgeSize = map(int, input().split())

startNode = int(input())

distance = [sys.maxsize] * NodeSize

visited = [False] * NodeSize

adjList = [[] for _ in range(NodeSize)]

for _ in range(EdgeSize):
    fr, to, weight = map(int, input().split())
    adjList[fr].append((to, weight))  # 이미 0-based
distance[startNode] = 0

q = PriorityQueue()
q.put((startNode, 0))

while q.qsize() > 0:
    targetNode = q.get()
    targetNodeNumber = targetNode[0]
    targetNodeDistance = targetNode[1]    
    if visited[targetNodeNumber]:
        continue
    
    visited[targetNodeNumber] = True
    
    for nextNode, nextNodeDistance in adjList[targetNodeNumber]:
        if distance[nextNode] != sys.maxsize and distance[nextNode] > distance[targetNodeNumber] + nextNodeDistance:
            distance[nextNode] = distance[targetNodeNumber] + nextNodeDistance
            q.put((nextNode, distance[nextNode]))
            
for i in range(NodeSize):
    if distance[i] == sys.maxsize:
        print("INF")
    else:
        print(distance[i])

    





