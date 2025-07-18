import dis
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

node = [[] for _ in range(N + 1)]

edges = []

distance = [sys.maxsize] * (N + 1)

for i in range(M):
    fr, to, weight = map(int, input().split())
    edges.append((fr, to, weight))
    
distance[1] = 0

for _ in range(N - 1):
    for fr, to, weight in edges:
        if distance[fr] != sys.maxsize and distance[to] > distance[fr] + weight:
            distance[to] = distance[fr] + weight
            
mCycle = False

for fr, to, weight in edges:
    if distance[fr] != sys.maxsize and distance[to] > distance[fr] + weight:
        mCycle = True
        break
    

if not mCycle:
    for i in range(2, N + 1):
        if distance[i] == sys.maxsize:
            print(-1)
        else:
            print(distance[i])