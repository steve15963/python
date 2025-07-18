import sys

input = sys.stdin.readline

nodeSize, edgeSize = map(int, input().split())

startNode = int(input())

adjList = [[] for _ in range(nodeSize)]

bestWeight = [sys.maxsize] * nodeSize

bestWeight[startNode] = 0

for _ in range(edgeSize):
    fr, to, weight = map(int, input().split())
    adjList[fr].append((weight, to))

# 벨만-포드 알고리즘: V-1번 반복 필수!
# 다익스트라와 다르게 모든 간선을 확인하는 것이 핵심
# 모든 간선은 노드 개수 - 1 만큼 반복하면 최단 거리를 구할 수 있다.
# 왜냐하면 N개의 노드에선 N-1개의 간선으로 모두 연결 할 수 있고
# N-1번을 반복하면 모든 노드의 최단 거리를 구할 수 있다.
for i in range(nodeSize - 1):
    # 모든 노드를 순회
    for fr in range(nodeSize):
        # 모든 간선을 순회
        for weight, to in adjList[fr]:
            # 현재 노드의 최단 거리와 다음 노드의 최단 거리를 비교
            # 다음 노드의 최단 거리가 현재 노드의 최단 거리 + 간선의 가중치보다 크다면
            # 다음 노드의 최단 거리를 현재 노드의 최단 거리 + 간선의 가중치로 업데이트
            if bestWeight[fr] != sys.maxsize and bestWeight[to] > bestWeight[fr] + weight:
                bestWeight[to] = bestWeight[fr] + weight

# 음수 사이클 검사
hasNegativeCycle = False
for fr in range(nodeSize):
    for weight, to in adjList[fr]:
        if bestWeight[fr] != sys.maxsize and bestWeight[to] > bestWeight[fr] + weight:
            hasNegativeCycle = True
            break
    if hasNegativeCycle:
        break

# 결과 출력
if hasNegativeCycle:
    print("음수 사이클이 존재합니다.")
else:
    for i in range(nodeSize):
        if bestWeight[i] == sys.maxsize:
            print(f"노드 {startNode}에서 노드 {i}로 가는 경로가 없습니다.")
        else:
            print(f"노드 {startNode}에서 노드 {i}까지의 최단 거리: {bestWeight[i]}")



