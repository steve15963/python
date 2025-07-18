import heapq
import sys


class RTOSBellmanFord:
    def __init__(self, nodes, start):
        self.nodes = nodes
        self.start = start
        self.adj = [[] for _ in range(nodes)]
        self.dist = [float('inf')] * nodes
        self.dist[start] = 0
        
        self.pq = [(0, start)]
        self.in_pq = [False] * nodes
        self.in_pq[start] = True
        self.count = [0] * nodes
        
        self.done = False
        self.neg_cycle = False
        self.steps = 0

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))

    def step(self):
        if not self.pq or self.done:
            self.done = True
            return False

        d, u = heapq.heappop(self.pq)
        self.in_pq[u] = False
        self.steps += 1

        if d > self.dist[u]:
            return True

        if self.count[u] >= self.nodes:
            self.neg_cycle = True
            self.done = True
            return False

        for v, w in self.adj[u]:
            if self.dist[u] + w < self.dist[v]:
                self.dist[v] = self.dist[u] + w
                if not self.in_pq[v]:
                    heapq.heappush(self.pq, (self.dist[v], v))
                    self.in_pq[v] = True
                    self.count[v] += 1

        return True

    def run_all(self):
        while self.step():
            pass

def test():
    print("RTOS Bellman-Ford Test")
    print("=====================")
    
    bf = RTOSBellmanFord(4, 0)
    
    # Add edges
    edges = [(0,1,1), (0,2,4), (1,2,-3), (1,3,2), (2,3,1)]
    for u, v, w in edges:
        bf.add_edge(u, v, w)
        print(f"Edge: {u} -> {v} weight {w}")
    
    print(f"Start: {bf.start}")
    print(f"Initial: {bf.dist}")
    print()
    
    # Step by step
    step = 1
    while bf.step():
        print(f"Step {step}: {bf.dist} (queue: {len(bf.pq)})")
        step += 1
    
    print()
    print("Final Results:")
    if bf.neg_cycle:
        print("Negative cycle detected!")
    else:
        for i in range(bf.nodes):
            if bf.dist[i] == float('inf'):
                print(f"Node {bf.start} -> {i}: No path")
            else:
                print(f"Node {bf.start} -> {i}: {bf.dist[i]}")
    
    print(f"Total steps: {bf.steps}")

if __name__ == "__main__":
    test() 