import sys


def bellman_ford_test(nodeSize, edgeSize, startNode, edges):
    """벨만 포드 알고리즘 직접 구현"""
    adjList = [[] for _ in range(nodeSize)]
    bestWeight = [sys.maxsize] * nodeSize
    bestWeight[startNode] = 0
    
    # 간선 정보 입력
    for fr, to, weight in edges:
        adjList[fr].append((to, weight))
    
    print(f"그래프: {nodeSize}개 노드, {edgeSize}개 간선, 시작점: {startNode}")
    for i, edge_list in enumerate(adjList):
        if edge_list:
            print(f"노드 {i}: {edge_list}")
    
    # 벨만-포드 메인 알고리즘
    for iteration in range(nodeSize-1):
        updated = False
        for fr in range(nodeSize):
            for to, weight in adjList[fr]:
                if bestWeight[fr] != sys.maxsize and bestWeight[to] > bestWeight[fr] + weight:
                    old_weight = bestWeight[to] if bestWeight[to] != sys.maxsize else "∞"
                    bestWeight[to] = bestWeight[fr] + weight
                    updated = True
                    print(f"  반복 {iteration+1}: {fr}→{to}, {old_weight} → {bestWeight[to]}")
        
        if not updated:
            print(f"반복 {iteration+1}에서 조기 수렴!")
            break
    
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
    print(f"\n결과:")
    if hasNegativeCycle:
        print("음수 사이클이 존재합니다.")
    else:
        for i, weight in enumerate(bestWeight):
            if weight == sys.maxsize:
                print(f"노드 {i}: 도달 불가능 (-1)")
            else:
                print(f"노드 {i}: {weight}")
    
    return not hasNegativeCycle

def run_tests():
    print("=== 벨만 포드 알고리즘 테스트 ===\n")
    
    # 테스트 1: 일반적인 케이스
    print("테스트 1: 음수 가중치 포함 일반 케이스")
    print("-" * 40)
    edges1 = [(0, 1, 1), (0, 2, 4), (1, 2, -3), (1, 3, 2), (2, 3, 1)]
    bellman_ford_test(4, 5, 0, edges1)
    
    print("\n" + "="*50 + "\n")
    
    # 테스트 2: 음수 사이클
    print("테스트 2: 음수 사이클 존재")
    print("-" * 40)
    edges2 = [(0, 1, 1), (1, 2, -3), (2, 0, 1)]
    bellman_ford_test(3, 3, 0, edges2)
    
    print("\n" + "="*50 + "\n")
    
    # 테스트 3: 연결되지 않은 그래프
    print("테스트 3: 도달 불가능한 노드")
    print("-" * 40)
    edges3 = [(0, 1, 5), (2, 3, 3)]
    bellman_ford_test(4, 2, 0, edges3)

if __name__ == "__main__":
    run_tests() 