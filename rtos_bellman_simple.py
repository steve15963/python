import heapq
import sys
import time


class RTOSBellmanFord:
    def __init__(self, node_count, start_node):
        self.node_count = node_count
        self.start_node = start_node
        self.edges = []
        self.distances = [sys.maxsize] * node_count
        self.distances[start_node] = 0
        
        # Priority Queue: (거리, 노드)
        self.pq = [(0, start_node)]
        self.in_queue = [False] * node_count
        self.in_queue[start_node] = True
        self.update_count = [0] * node_count
        
        self.completed = False
        self.negative_cycle = False
        self.iterations = 0
    
    def add_edge(self, from_node, to_node, weight):
        self.edges.append((from_node, to_node, weight))
    
    def step(self):
        """한 스텝 실행. 반환값: 계속 실행할지 여부"""
        if not self.pq or self.completed:
            self.completed = True
            return False
        
        # 가장 거리가 짧은 노드 처리
        dist, node = heapq.heappop(self.pq)
        self.in_queue[node] = False
        self.iterations += 1
        
        # 이미 더 좋은 거리가 있으면 스킵
        if dist > self.distances[node]:
            return True
        
        # 음수 사이클 검사 (한 노드가 너무 많이 업데이트됨)
        if self.update_count[node] >= self.node_count:
            self.negative_cycle = True
            self.completed = True
            return False
        
        # 이 노드에서 시작하는 모든 간선 처리
        for from_node, to_node, weight in self.edges:
            if from_node == node:
                new_dist = self.distances[node] + weight
                if new_dist < self.distances[to_node]:
                    self.distances[to_node] = new_dist
                    
                    # 큐에 없으면 추가
                    if not self.in_queue[to_node]:
                        heapq.heappush(self.pq, (new_dist, to_node))
                        self.in_queue[to_node] = True
                        self.update_count[to_node] += 1
        
        return True
    
    def run_steps(self, max_steps):
        """최대 max_steps만큼 실행"""
        for _ in range(max_steps):
            if not self.step():
                break
    
    def run_with_time_limit(self, time_limit_ms):
        """시간 제한 내에서 실행"""
        start_time = time.time() * 1000
        while True:
            current_time = time.time() * 1000
            if current_time - start_time >= time_limit_ms:
                return False  # 시간 초과
            
            if not self.step():
                return True  # 완료
    
    def get_status(self):
        if self.negative_cycle:
            return "음수 사이클 감지"
        elif self.completed:
            return "완료"
        else:
            return f"진행 중 (큐: {len(self.pq)}개, 반복: {self.iterations})"
    
    def print_results(self):
        print(f"상태: {self.get_status()}")
        if self.negative_cycle:
            print("음수 사이클이 존재합니다.")
        else:
            for i in range(self.node_count):
                if self.distances[i] == sys.maxsize:
                    print(f"노드 {self.start_node} → {i}: 경로 없음")
                else:
                    print(f"노드 {self.start_node} → {i}: {self.distances[i]}")

def test_rtos():
    print("=== RTOS용 벨만-포드 테스트 ===")
    
    # 그래프 생성 (4개 노드, 시작점 0)
    bf = RTOSBellmanFord(4, 0)
    
    # 간선 추가
    edges = [(0, 1, 1), (0, 2, 4), (1, 2, -3), (1, 3, 2), (2, 3, 1)]
    for fr, to, weight in edges:
        bf.add_edge(fr, to, weight)
        print(f"간선: {fr} → {to} (가중치: {weight})")
    
    print(f"\n초기 거리: {bf.distances}")
    print(f"시작 노드: {bf.start_node}\n")
    
    # 단계별 실행
    step = 1
    while not bf.completed:
        print(f"--- 스텝 {step} ---")
        old_distances = bf.distances.copy()
        bf.run_steps(1)  # 1스텝만 실행
        
        print(f"상태: {bf.get_status()}")
        print(f"거리: {bf.distances}")
        
        # 변경사항 표시
        for i in range(bf.node_count):
            if old_distances[i] != bf.distances[i]:
                old = "∞" if old_distances[i] == sys.maxsize else old_distances[i]
                new = "∞" if bf.distances[i] == sys.maxsize else bf.distances[i]
                print(f"  노드 {i}: {old} → {new}")
        
        step += 1
        print()
    
    print("=== 최종 결과 ===")
    bf.print_results()
    
    # 시간 제한 테스트
    print(f"\n=== 시간 제한 테스트 (5ms) ===")
    bf2 = RTOSBellmanFord(4, 0)
    for fr, to, weight in edges:
        bf2.add_edge(fr, to, weight)
    
    completed = bf2.run_with_time_limit(5.0)
    print(f"5ms 내 완료: {completed}")
    print(f"처리된 반복: {bf2.iterations}")
    print(f"현재 거리: {bf2.distances}")

if __name__ == "__main__":
    test_rtos() 