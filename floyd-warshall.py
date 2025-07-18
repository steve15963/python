import sys

input = sys.stdin.readline

nodeSize, edgeSize = map(int, input().split())

bestWeight = [[sys.maxsize] * nodeSize for _ in range(nodeSize)]

for i in range(nodeSize):
    bestWeight[i][i] = 0

for _ in range(edgeSize):
    fr, to, weight = map(int, input().split())
    if bestWeight[fr][to] > weight:
        bestWeight[fr][to] = weight
    
for k in range(nodeSize):
    for i in range(nodeSize):
        for j in range(nodeSize):
            if bestWeight[i][j] > bestWeight[i][k] + bestWeight[k][j]:
                bestWeight[i][j] = bestWeight[i][k] + bestWeight[k][j]
        
for i in range(nodeSize):
    for j in range(nodeSize):
        if bestWeight[i][j] == sys.maxsize:
            print(0, end=" ")
        else:
            print(bestWeight[i][j], end=" ")
    print()