import sys

input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())

K = int(input())

distance = [sys.maxsize] * (V + 1)
visited = [False] * (V + 1)

adjList = [[] for _ in range( V + 1 )]

q = PriorityQueue()
for _ in range(E):
    fr, to, weight = map(int, input().split())
    adjList[fr].append((to,weight))
    
q.put((0, K))

distance[K] = 0

while q.qsize() > 0:
    #노드를 가져와서
    node = q.get()
    #다음 노드를 본다.
    targetNode = node[1]
    #방문했으면 넘어간다.
    if visited[targetNode]:
        continue
    #방문했다고 표시한다.
    visited[targetNode] = True
    #다음 노드를 본다.
    for next in adjList[targetNode]:
        #인접리스트에서 다음 노드를 가져온다.
        next_node = next[0]
        next_weight = next[1]
        #거리를 계산해서 만약 거리가 더 작으면
        if distance[next_node] > distance[targetNode] + next_weight:
            #거리를 업데이트한다.
            distance[next_node] = distance[targetNode] + next_weight
            #앞으로 더 갱신될 수 있으므로 큐에 넣는다.
            q.put((distance[next_node], next_node))

for i in range(1, V + 1):
    if distance[i] == sys.maxsize:
        print("INF")
    else:
        print(distance[i])
            



