import sys


def bellman_ford_with_passed():
    # 테스트 데이터
    nodeSize, edgeSize = 4, 5
    startNode = 0
    edges = [
        (0, 1, 1),
        (0, 2, 4), 
        (1, 2, -3),
        (1, 3, 2),
        (2, 3, 1)
    ]
    
    adjList = [[] for _ in range(nodeSize)]
    bestWeight = [sys.maxsize] * nodeSize
    bestWeight[startNode] = 0
    
    print("=== passed 변수를 사용한 벨만-포드 ===")
    
    # 간선 정보 출력
    for fr, to, weight in edges:
        adjList[fr].append((weight, to))
        print(f"간선: {fr} → {to} (가중치: {weight})")
    
    print(f"초기 거리: {bestWeight}\n")
    
    # passed 변수를 사용한 벨만-포드
    for iteration in range(nodeSize - 1):  # 최대 V-1번 반복
        passed = True  # 이번 반복에서 변경사항이 있었는지 추적
        
        print(f"--- {iteration + 1}번째 반복 ---")
        
        for fr in range(nodeSize):
            for weight, to in adjList[fr]:
                if bestWeight[fr] != sys.maxsize and bestWeight[to] > bestWeight[fr] + weight:
                    old_dist = bestWeight[to] if bestWeight[to] != sys.maxsize else "∞"
                    bestWeight[to] = bestWeight[fr] + weight
                    passed = False  # 변경사항 발생!
                    print(f"  업데이트: {fr}→{to}, {old_dist} → {bestWeight[to]}")
        
        print(f"  현재 거리: {bestWeight}")
        print(f"  passed: {passed}")
        
        # 변경사항이 없으면 조기 종료
        if passed:
            print(f"  🎉 {iteration + 1}번째 반복에서 수렴 완료!")
            print(f"\n=== 최종 결과 (조기 완료) ===")
            for i in range(nodeSize):
                if bestWeight[i] == sys.maxsize:
                    print(f"노드 {startNode}에서 노드 {i}로 가는 경로가 없습니다.")
                else:
                    print(f"노드 {startNode}에서 노드 {i}까지의 최단 거리: {bestWeight[i]}")
            return bestWeight, False  # 음수 사이클 없음
        
        print()
    
    # V-1번 반복 후에도 passed가 False면 음수 사이클 존재
    print("⚠️  V-1번 반복 후에도 수렴하지 않음 → 음수 사이클 존재!")
    return bestWeight, True  # 음수 사이클 있음

def test_negative_cycle_case():
    print("\n" + "="*50)
    print("=== 음수 사이클 테스트 ===")
    
    # 음수 사이클이 있는 그래프
    nodeSize, edgeSize = 3, 3
    startNode = 0
    edges = [
        (0, 1, 1),
        (1, 2, -3),
        (2, 0, 1)  # 사이클: 0→1→2→0 = 1+(-3)+1 = -1
    ]
    
    adjList = [[] for _ in range(nodeSize)]
    bestWeight = [sys.maxsize] * nodeSize
    bestWeight[startNode] = 0
    
    for fr, to, weight in edges:
        adjList[fr].append((weight, to))
        print(f"간선: {fr} → {to} (가중치: {weight})")
    
    print(f"초기 거리: {bestWeight}\n")
    
    for iteration in range(nodeSize - 1):
        passed = True
        print(f"--- {iteration + 1}번째 반복 ---")
        
        for fr in range(nodeSize):
            for weight, to in adjList[fr]:
                if bestWeight[fr] != sys.maxsize and bestWeight[to] > bestWeight[fr] + weight:
                    old_dist = bestWeight[to] if bestWeight[to] != sys.maxsize else "∞"
                    bestWeight[to] = bestWeight[fr] + weight
                    passed = False
                    print(f"  업데이트: {fr}→{to}, {old_dist} → {bestWeight[to]}")
        
        print(f"  현재 거리: {bestWeight}")
        print(f"  passed: {passed}")
        
        if passed:
            print(f"  수렴 완료 (음수 사이클 없음)")
            return
        print()
    
    print("⚠️  음수 사이클 감지됨!")

if __name__ == "__main__":
    # 정상적인 그래프 테스트
    distances, has_negative_cycle = bellman_ford_with_passed()
    
    # 음수 사이클이 있는 그래프 테스트
    test_negative_cycle_case() 