import sys
from queue import PriorityQueue

input = sys.stdin.readline

nodeSize, edgeSize = map(int,input.split())

startNodeNum = int(input())

adjList = [[] for _ in range(nodeSize)]

visit = [False] * (nodeSize)

bestWeight = [sys.maxsize] * nodeSize
bestWeight[startNodeNum] = 0

for _ in range(edgeSize):
	fr, to, weigth = map(int,input.split())
	adjList[fr].append((weigth,to))

q = PriorityQueue() 

q.put((0, startNodeNum))

while not q.empty():
	targetNode = q.get()
    # 우선순위 큐를 위하여 순서 바뀜 참고!
	targetNodeNum = targetNode[1]
	targetNodeWeight = targetNode[0]
	
	if targetNodeWeight == sys.maxsize:
		continue
	
	for adj in adjList[targetNodeNum]:
        # 일관성을 위하여 0과 1이 바뀜
		nextNode = adj[1]
		nextWeight = adj[0]
        # 최단거리 갱신
		if bestWeight[nextNode] > bestWeight[targetNodeNum] + nextWeight:
			bestWeight[nextNode] = bestWeight[targetNodeNum] + nextWeight
			q.put((bestWeight[nextNode], nextNode))

for i in bestWeight:
	if i == sys.maxsize:
		print('INF')
	else:
		print(i)