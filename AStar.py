import heapq

# 간선 정보: (출발역, 도착역, 시간(분))
edges = [
    ('강남','교대',2), ('교대','고속터미널',3), ('고속터미널','사당',2),
    ('사당','이수',2), ('이수','서울대입구',3), ('서울대입구','신림',2),
    ('신림','신대방',3), ('신대방','여의도',4), ('여의도','당산',2),
    ('당산','합정',2), ('합정','홍대입구',2), ('홍대입구','신촌',2),
    ('신촌','이대',1), ('이대','서강대',1), ('서강대','용산',3),
    ('용산','서울역',3), ('서울역','회현',1), ('회현','명동',1),
    ('명동','충무로',1), ('충무로','종로3가',2), ('종로3가','동대문',2),
    ('동대문','청량리',4), ('종로3가','왕십리',5), ('왕십리','성수',2),
    ('성수','건대입구',2), ('건대입구','선릉',5), ('선릉','삼성',2),
    ('삼성','잠실',3), ('잠실','잠실새내',1), ('교대','선릉',7),
    ('강남','선릉',4), ('당산','용산',5), ('고속터미널','홍대입구',10),
]

# 그래프 생성
graph = {}
for u, v, w in edges:
    graph.setdefault(u, []).append((v, w))
    graph.setdefault(v, []).append((u, w))

def heuristic(u, v):
    return 0

def transferTime(u, v):
    return 0

def isNotSameLine(u, v):
    return True

def a_star(start, goal):
    pq = [(heuristic(start, goal), 0, start, [start])]
    visited = dict()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            return g, path

        if node in visited and visited[node] <= g:
            continue
        visited[node] = g

        for neighbor, weight in graph.get(node, []):
            ng = g + weight
            
            if isNotSameLine(node, neighbor):
                ng += transferTime(node, neighbor)
            
            if neighbor in visited and visited[neighbor] <= ng:
                continue
            nh = heuristic(neighbor, goal)
              
            heapq.heappush(pq, (ng + nh, ng, neighbor, path + [neighbor]))

    return float('inf'), []

if __name__ == "__main__":
    start_station = "강남"
    end_station = "이대"
    dist, route = a_star(start_station, end_station)
    if dist < float('inf'):
        print(f"경로 찾음 : {dist}분 | 경로:", " → ".join(route))
    else:
        print("경로를 찾을 수 없습니다.")
