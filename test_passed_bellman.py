import sys


def test_passed_bellman():
    print("=== passed 변수로 개선된 벨만-포드 ===")
    
    # 테스트 데이터
    nodeSize, edgeSize = 4, 5
    startNode = 0
    
    adjList = [[] for _ in range(nodeSize)]
    bestWeight = [sys.maxsize] * nodeSize
    bestWeight[startNode] = 0
    
    # 간선 추가
    edges = [(0, 1, 1), (0, 2, 4), (1, 2, -3), (1, 3, 2), (2, 3, 1)]
    for fr, to, weight in edges:
        adjList[fr].append((weight, to))
        print(f"간선: {fr} → {to} (가중치: {weight})")
    
    print(f"초기 거리: {bestWeight}\n")
    
    # passed 변수를 사용한 효율적인 벨만-포드 구현
    hasNegativeCycle = False
    
    for i in range(nodeSize - 1):
        passed = True  # 이번 반복에서 변경사항이 있었는지 추적
        print(f"--- {i+1}번째 반복 ---")
        
        # 모든 노드를 순회
        for fr in range(nodeSize):
            # 모든 간선을 순회
            for weight, to in adjList[fr]:
                # 현재 노드의 최단 거리와 다음 노드의 최단 거리를 비교
                if bestWeight[fr] != sys.maxsize and bestWeight[to] > bestWeight[fr] + weight:
                    old_dist = bestWeight[to] if bestWeight[to] != sys.maxsize else "∞"
                    bestWeight[to] = bestWeight[fr] + weight
                    passed = False  # 변경사항 발생!
                    print(f"  업데이트: {fr}→{to}, {old_dist} → {bestWeight[to]}")
        
        print(f"  현재 거리: {bestWeight}")
        print(f"  passed: {passed}")
        
        # 변경사항이 없으면 조기 종료 (수렴 완료)
        if passed:
            print(f"  🎉 {i+1}번째 반복에서 수렴 완료! (조기 종료)")
            break
        print()
    else:
        # for문이 break 없이 끝났다면 (V-1번 모두 반복했는데도 변경사항 있음)
        # 음수 사이클 존재
        hasNegativeCycle = True
        print("  ⚠️ V-1번 반복 후에도 변경사항 존재 → 음수 사이클!")
    
    # 결과 출력
    print(f"\n=== 최종 결과 ===")
    if hasNegativeCycle:
        print("음수 사이클이 존재합니다.")
    else:
        for i in range(nodeSize):
            if bestWeight[i] == sys.maxsize:
                print(f"노드 {startNode}에서 노드 {i}로 가는 경로가 없습니다.")
            else:
                print(f"노드 {startNode}에서 노드 {i}까지의 최단 거리: {bestWeight[i]}")

def test_negative_cycle():
    print("\n" + "="*60)
    print("=== 음수 사이클 테스트 ===")
    
    # 음수 사이클이 있는 그래프
    nodeSize, edgeSize = 3, 3
    startNode = 0
    
    adjList = [[] for _ in range(nodeSize)]
    bestWeight = [sys.maxsize] * nodeSize
    bestWeight[startNode] = 0
    
    # 음수 사이클: 0→1→2→0 = 1+(-3)+1 = -1
    edges = [(0, 1, 1), (1, 2, -3), (2, 0, 1)]
    for fr, to, weight in edges:
        adjList[fr].append((weight, to))
        print(f"간선: {fr} → {to} (가중치: {weight})")
    
    print(f"사이클 가중치 합: 1 + (-3) + 1 = -1 (음수!)")
    print(f"초기 거리: {bestWeight}\n")
    
    hasNegativeCycle = False
    
    for i in range(nodeSize - 1):
        passed = True
        print(f"--- {i+1}번째 반복 ---")
        
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
            break
        print()
    else:
        hasNegativeCycle = True
        print("  ⚠️ 음수 사이클 감지됨!")
    
    print(f"\n최종 결과: {'음수 사이클 존재' if hasNegativeCycle else '정상'}")

if __name__ == "__main__":
    test_passed_bellman()
    test_negative_cycle() 