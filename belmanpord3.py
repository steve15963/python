import sys

input = sys.stdin.readline

nodeSize, edgeSize = map(int,input().split())

startNode = int(input())

adjList = [[] for _ in range(nodeSize)]

bestWeight = [sys.maxsize] * nodeSize

bestWeight[startNode] = 0

for _ in range(edgeSize):
    fr, to, weight = map(int,input().split())
    adjList[fr].append((to,weight))

# 벨만-포드 메인 알고리즘: nodeSize-1번 반복
for _ in range(nodeSize-1):
    for fr in range(nodeSize):
        for to, weight in adjList[fr]:
            if bestWeight[fr] != sys.maxsize and bestWeight[to] > bestWeight[fr] + weight:
                bestWeight[to] = bestWeight[fr] + weight

# 음수 사이클 검출
hasNegativeCycle = False
for fr in range(nodeSize):
    for to, weight in adjList[fr]:
        if bestWeight[fr] != sys.maxsize and bestWeight[to] > bestWeight[fr] + weight:
            hasNegativeCycle = True
            break
    if hasNegativeCycle:
        break

# 결과 출력
if hasNegativeCycle:
    print("음수 사이클이 존재합니다.")
else:
    for weight in bestWeight:
        if weight == sys.maxsize:
            print(-1)
        else:
            print(weight)
