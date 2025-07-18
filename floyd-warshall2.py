import sys

input = sys.stdin.readline

nodeSize, edgeSize = map(int,input().split())

adjMatrix = [[sys.maxsize] * nodeSize for _ in range(nodeSize)]

# 자기 자신으로의 거리는 0으로 초기화
for i in range(nodeSize):
    adjMatrix[i][i] = 0
    
# 간선 정보 입력
for _ in range(edgeSize):
    fr, to, weight = map(int,input().split())
    adjMatrix[fr][to] = weight

# adjMatrix를 bestWeight에 복사
bestWeight = [[adjMatrix[i][j] for j in range(nodeSize)] for i in range(nodeSize)]

# Floyd-Warshall 알고리즘
for k in range(nodeSize):
    for i in range(nodeSize):
        for j in range(nodeSize):
            if bestWeight[i][j] > bestWeight[i][k] + bestWeight[k][j]:
                bestWeight[i][j] = bestWeight[i][k] + bestWeight[k][j]

# 결과 출력
for i in range(nodeSize):
    for j in range(nodeSize):
        if bestWeight[i][j] == sys.maxsize:
            print("INF", end=" ")
        else:
            print(bestWeight[i][j], end=" ")
    print()
