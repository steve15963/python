import heapq
import sys


class RTOSBellmanFord:
    def __init__(self, node_count, start_node):
        self.node_count = node_count
        self.start_node = start_node
        self.adj_list = [[] for _ in range(node_count)]
        self.distances = [sys.maxsize] * node_count
        self.distances[start_node] = 0
        
        # Priority Queue와 상태 관리
        self.pq = [(0, start_node)]
        self.in_queue = [False] * node_count
        self.in_queue[start_node] = True
        self.update_count = [0] * node_count
        
        self.completed = False
        self.has_negative_cycle = False
        self.iterations = 0
    
    def add_edge(self, from_node, to_node, weight):
        self.adj_list[from_node].append((weight, to_node))
    
    def step(self):
        """한 스텝 실행"""
        if not self.pq or self.completed:
            self.completed = True
            return False
        
        current_dist, current_node = heapq.heappop(self.pq)
        self.in_queue[current_node] = False
        self.iterations += 1
        
        # 이미 더 좋은 거리가 있으면 스킵
        if current_dist > self.distances[current_node]:
            return True
        
        # 음수 사이클 검사
        if self.update_count[current_node] >= self.node_count:
            self.has_negative_cycle = True
            self.completed = True
            return False
        
        # 인접 노드들 완화
        for weight, next_node in self.adj_list[current_node]:
            new_dist = self.distances[current_node] + weight
            if new_dist < self.distances[next_node]:
                self.distances[next_node] = new_dist
                
                if not self.in_queue[next_node]:
                    heapq.heappush(self.pq, (new_dist, next_node))
                    self.in_queue[next_node] = True
                    self.update_count[next_node] += 1
        
        return True
    
    def get_result(self):
        return {
            'distances': self.distances.copy(),
            'completed': self.completed,
            'has_negative_cycle': self.has_negative_cycle,
            'iterations': self.iterations,
            'queue_size': len(self.pq)
        }

def demo():
    print("=== RTOS용 벨만-포드 알고리즘 ===")
    
    # 그래프 설정
    bf = RTOSBellmanFord(4, 0)
    edges = [(0, 1, 1), (0, 2, 4), (1, 2, -3), (1, 3, 2), (2, 3, 1)]
    
    for fr, to, weight in edges:
        bf.add_edge(fr, to, weight)
        print(f"간선 추가: {fr} -> {to} (가중치: {weight})")
    
    print()
    print("단계별 실행:")
    
    step_num = 1
    while not bf.completed:
        result = bf.get_result()
        print(f"스텝 {step_num} 이전: {result['distances']}")
        
        bf.step()
        
        new_result = bf.get_result()
        print(f"스텝 {step_num} 이후: {new_result['distances']}")
        print(f"  상태: 반복={new_result['iterations']}, 큐크기={new_result['queue_size']}")
        print()
        
        step_num += 1
        if step_num > 10:  # 무한 루프 방지
            break
    
    # 최종 결과
    final = bf.get_result()
    print("=== 최종 결과 ===")
    
    if final['has_negative_cycle']:
        print("음수 사이클이 존재합니다!")
    else:
        print("최단 거리:")
        for i in range(bf.node_count):
            if final['distances'][i] == sys.maxsize:
                print(f"  노드 0 -> {i}: 경로 없음")
            else:
                print(f"  노드 0 -> {i}: {final['distances'][i]}")
    
    print(f"총 반복 횟수: {final['iterations']}")
    return bf

if __name__ == "__main__":
    demo() 