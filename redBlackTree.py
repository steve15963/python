# redBlackTree.py

class Node:
    def __init__(self, key, color, left=None, right=None, parent=None):
        self.key = key
        self.color = color  # 'R' or 'B'
        self.left = left
        self.right = right
        self.parent = parent

class RedBlackTree:
    def __init__(self):
        # Null이 아닌 NIL노드를 사용하는 이유는
        # 노드가 하나도 없을 때 루트가 널이 되는 것을 방지하기 위함도 있고
        # R인지 B인지 구분하기 위함도 있음
        # 또한 노드가 하나도 없을 때 루트가 널이 되는 것을 방지하기 위함도 있음
        # NIL = Sentinel Node로 Not IN List의 약자이다.
        self.NIL = Node(None, 'B')
        self.root = self.NIL

    def insert(self, key):
        node = Node(key, 'R', self.NIL, self.NIL)
        parent = None
        current = self.root

        # 삽입할 노드의 위치를 찾는 과정
        while current != self.NIL:
            # 삽입할 노드의 위치를 업데이트 해준다.
            parent = current
            # 만약 키값이 현재 노드의 키값보다 작으면 왼쪽으로 이동
            if node.key < current.key:
                current = current.left
            # 만약 키값이 현재 노드의 키값보다 크면 오른쪽으로 이동
            else:
                current = current.right

        # 삽입할 노드의 위치를 찾았으면 삽입해준다.
        node.parent = parent
        # 만약 삽입할 노드의 부모가 없으면 루트가 된다.
        if parent is None:
            self.root = node
        # 만약 삽입할 노드의 키값이 부모의 키값보다 작으면 왼쪽에 삽입
        elif node.key < parent.key:
            parent.left = node
        # 만약 삽입할 노드의 키값이 부모의 키값보다 크면 오른쪽에 삽입
        else:
            # 삽입할 노드의 키값이 부모의 키값보다 크면 오른쪽에 삽입
            parent.right = node

        # 삽입한 노드의 색상을 조정하는 함수
        self.insert_fixup(node)

    def insert_fixup(self, node):
        # 삽입한 노드가 루트가 아니고 부모가 레드일 때 계속 반복
        while node != self.root and node.parent.color == 'R':
            # 만약 삽입할 노드의 부모가 왼쪽 자식일 때
            # 좌측 트리일때 오른쪽 트리일때 나눠서 처리
            if node.parent == node.parent.parent.left:
                # 삽입할 노드의 부모의 형제 노드를 찾는다.
                uncle = node.parent.parent.right
                # 만약 삽입할 노드의 부모의 형제 노드가 레드일 때
                if uncle.color == 'R':
                    # 삽입할 노드의 부모와 형제 노드를 블랙으로 바꾸고 부모의 부모를 레드로 바꾼다.
                    node.parent.color = 'B'
                    # 삽입할 노드의 부모의 형제 노드를 블랙으로 바꾼다.
                    uncle.color = 'B'
                    # 삽입할 노드의 부모의 부모를 레드로 바꾼다.
                    node.parent.parent.color = 'R'
                    # 삽입할 노드의 부모의 부모를 새로운 삽입할 노드로 업데이트 해준다.
                    node = node.parent.parent
                # 만약 삽입할 노드의 부모의 형제 노드가 블랙일 때
                else:
                    # 만약 삽입할 노드가 부모의 오른쪽 자식일 때
                    # 할머니 보다는 크고
                    # 부모보다는 작은 경우
                    # 부모 노드를 변경하여 정렬을 수행한다.
                    # 부분 트리 처리
                    if node == node.parent.right:
                        # 삽입할 노드를 부모로 올린다.
                        node = node.parent
                        # 왼쪽 회전을 한다.
                        self.left_rotate(node)
                    # 삽입할 노드의 부모를 블랙으로 바꾸고 부모의 부모를 레드로 바꾼다.
                    node.parent.color = 'B'
                    # 삽입할 노드의 부모의 부모를 레드로 바꾼다.
                    node.parent.parent.color = 'R'
                    # 오른쪽 회전을 한다.
                    self.right_rotate(node.parent.parent)
            # 만약 삽입할 노드의 부모가 오른쪽 자식일 때
            else:
                # 삽입할 노드의 부모의 형제 노드를 찾는다.
                uncle = node.parent.parent.left
                # 만약 삽입할 노드의 부모의 형제 노드가 레드일 때
                if uncle.color == 'R':
                    # 삽입할 노드의 부모와 형제 노드를 블랙으로 바꾸고 부모의 부모를 레드로 바꾼다.
                    node.parent.color = 'B'
                    # 삽입할 노드의 부모의 형제 노드를 블랙으로 바꾼다.
                    uncle.color = 'B'
                    # 삽입할 노드의 부모의 부모를 레드로 바꾼다.
                    node.parent.parent.color = 'R'
                    # 삽입할 노드의 부모의 부모를 새로운 삽입할 노드로 업데이트 해준다.
                    node = node.parent.parent
                # 만약 삽입할 노드의 부모의 형제 노드가 블랙일 때
                else:
                    # 만약 삽입할 노드가 부모의 왼쪽 자식일 때
                    if node == node.parent.left:
                        # 삽입할 노드를 부모로 올린다.
                        node = node.parent
                        # 오른쪽 회전을 한다.
                        self.right_rotate(node)
                    # 삽입할 노드의 부모를 블랙으로 바꾸고 부모의 부모를 레드로 바꾼다.
                    node.parent.color = 'B'
                    # 삽입할 노드의 부모의 부모를 레드로 바꾼다.
                    node.parent.parent.color = 'R'
                    # 왼쪽 회전을 한다.
                    self.left_rotate(node.parent.parent)
        # 루트 노드를 블랙으로 바꾼다.
        self.root.color = 'B'

    def left_rotate(self, grandParent):
        # 오른쪽 자식을 찾는다.
        right = grandParent.right
        # 오른쪽 자식의 왼쪽 자식을 찾는다.
        grandParent.right = right.left
        # 오른쪽 자식의 왼쪽 자식의 부모를 오른쪽 자식으로 바꾼다.
        # 즉 NIL이 아니면 오른쪽 자식의 왼쪽 자식의 부모를 오른쪽 자식으로 바꾼다.
        if right.left != self.NIL:
            # 오른쪽 자식의 왼쪽 자식의 부모를 오른쪽 자식으로 바꾼다.
            right.left.parent = grandParent
        # 오른쪽 자식의 부모를 오른쪽 자식의 부모로 바꾼다.
        right.parent = grandParent.parent
        # 만약 오른쪽 자식의 부모가 없으면 루트가 된다.
        if grandParent.parent is None:
            # 루트를 오른쪽 자식으로 바꾼다.
            self.root = right
        # 만약 오른쪽 자식이 오른쪽 자식의 부모의 왼쪽 자식일 때
        elif grandParent == grandParent.parent.left:
            # 오른쪽 자식의 부모의 왼쪽 자식을 오른쪽 자식으로 바꾼다.
            grandParent.parent.left = right
        # 만약 오른쪽 자식이 오른쪽 자식의 부모의 오른쪽 자식일 때
        else:
            # 오른쪽 자식의 부모의 오른쪽 자식을 오른쪽 자식으로 바꾼다.
            grandParent.parent.right = right
        # 오른쪽 자식의 왼쪽 자식을 오른쪽 자식으로 바꾼다.
        right.left = grandParent
        # 오른쪽 자식의 부모를 오른쪽 자식으로 바꾼다.
        grandParent.parent = right
        
    # 시계방향으로 트리를 회전하는 함수
    def right_rotate(self, grandParent):
        # 왼쪽 자식을 찾는다.
        left = grandParent.left
        # 왼쪽 자식의 오른쪽 자식을 왼쪽 자식으로 바꾼다.
        grandParent.left = left.right
        # 왼쪽 자식의 오른쪽 자식의 부모를 왼쪽 자식으로 바꾼다.
        if left.right != self.NIL:
            # 왼쪽 자식의 오른쪽 자식의 부모를 왼쪽 자식으로 바꾼다.
            left.right.parent = grandParent
        # 왼쪽 자식의 부모를 왼쪽 자식의 부모로 바꾼다.
        left.parent = grandParent.parent
        # 만약 왼쪽 자식의 부모가 없으면 루트가 된다.
        if grandParent.parent is None:
            # 루트를 왼쪽 자식으로 바꾼다.
            self.root = left
        # 만약 왼쪽 자식이 왼쪽 자식의 부모의 오른쪽 자식일 때
        elif grandParent == grandParent.parent.right:
            # 왼쪽 자식의 부모의 오른쪽 자식을 왼쪽 자식으로 바꾼다.
            grandParent.parent.right = left
        # 만약 왼쪽 자식이 왼쪽 자식의 부모의 왼쪽 자식일 때
        else:
            # 왼쪽 자식의 부모의 왼쪽 자식을 왼쪽 자식으로 바꾼다.
            grandParent.parent.left = left
        # 왼쪽 자식의 오른쪽 자식을 왼쪽 자식으로 바꾼다.
        left.right = grandParent
        # 왼쪽 자식의 부모를 왼쪽 자식으로 바꾼다.
        grandParent.parent = left

    def inorder(self, node=None, res=None):
        # 결과를 저장할 리스트를 초기화 해준다.
        if res is None:
            # 결과를 저장할 리스트를 초기화 해준다.
            res = []
        # 만약 노드가 없으면 루트를 찾는다.
        if node is None:
            # 루트를 찾는다.
            node = self.root
        # 만약 노드가 NIL이 아니면 중위 순회를 한다.
        if node != self.NIL:
            # 왼쪽 자식을 중위 순회 한다.
            self.inorder(node.left, res)
            # 노드를 결과에 추가한다.
            res.append((node.key, node.color))
            # 오른쪽 자식을 중위 순회 한다.
            self.inorder(node.right, res)
        return res


def main():
    print("=== 레드 블랙 트리 테스트 ===")
    rbt = RedBlackTree()
    
    # 테스트 데이터
    data = [20, 15, 25, 10, 5, 1, 30, 22, 50]
    
    print(f"삽입할 데이터: {data}")
    
    # 데이터 삽입
    for num in data:
        print(f"삽입: {num}")
        rbt.insert(num)
    
    print("\n중위 순회 결과 (key, color):")
    result = rbt.inorder()
    for key, color in result:
        print(f"{key}({color})", end=' ')
    print()
    
    # 추가 테스트: 더 많은 데이터로 테스트
    print("\n=== 추가 테스트 ===")
    rbt2 = RedBlackTree()
    data2 = [7, 3, 18, 10, 22, 8, 11, 26, 2, 6, 13]
    
    print(f"삽입할 데이터: {data2}")
    for num in data2:
        rbt2.insert(num)
    
    print("중위 순회 결과:")
    result2 = rbt2.inorder()
    for key, color in result2:
        print(f"{key}({color})", end=' ')
    print()

if __name__ == "__main__":
    main() 