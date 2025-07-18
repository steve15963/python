import sys
from queue import PriorityQueue
input = sys.stdin.readline

#정점 = Node
#간선 = Edge

nodeSize, edgeSize = map(int,input().split())

startNode = int(input())

# 입력력

visit = [False] * nodeSize

adjList = [[] for _ in range(nodeSize)]

bestWeight = [sys.maxsize] * nodeSize

bestWeight[startNode] = 0

for _ in range(edgeSize):
	fr, to, weight = map(int, input().split())
	adjList[fr].append((to,weight))

pq = PriorityQueue()

pq.put((0,startNode))

while not pq.empty():
	target = pq.get()
	targetNode = target[1]
	targetWeight = target[0]
	
	if visit[targetNode]:
		continue
	
	visit[targetNode] = True

	for next in adjList[targetNode]:
		nextNode = next[0]
		nextWeight = next[1]
		if bestWeight[nextNode] > bestWeight[targetNode] + nextWeight:
			bestWeight[nextNode] = bestWeight[targetNode] + nextWeight
			pq.put((bestWeight[nextNode], nextNode))

for i in range(nodeSize):
	if bestWeight[i] == sys.maxsize:
		print("INF", end=" ")
	else:
		print(bestWeight[i],end=" ")
