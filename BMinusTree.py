class BTreeNode:
    """B-Tree 노드 클래스"""
    def __init__(self, is_leaf=False):
        self.keys = []          # 키들을 저장하는 리스트
        self.children = []      # 자식 노드들을 저장하는 리스트
        self.is_leaf = is_leaf  # 리프 노드인지 여부
        
    def __str__(self):
        return str(self.keys)

class BTree:
    """B-Tree 클래스"""
    def __init__(self, degree=3):
        """
        B-Tree 초기화
        degree: 최소 차수 (각 노드가 가질 수 있는 최소 키 개수)
        """
        self.root = BTreeNode(is_leaf=True)
        self.degree = degree
        
    def search(self, key, node=None):
        """키 검색"""
        if node is None:
            node = self.root
            
        # 현재 노드에서 키 찾기
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
            
        # 키를 찾은 경우
        if i < len(node.keys) and key == node.keys[i]:
            return (node, i)
            
        # 리프 노드인 경우 키가 없음
        if node.is_leaf:
            return None
            
        # 자식 노드에서 재귀 검색
        return self.search(key, node.children[i])
    
    def insert(self, key):
        """키 삽입"""
        root = self.root
        
        # 루트가 가득 찬 경우 분할
        if len(root.keys) == (2 * self.degree) - 1:
            new_root = BTreeNode()
            self.root = new_root
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self._insert_non_full(new_root, key)
        else:
            self._insert_non_full(root, key)
    
    def _insert_non_full(self, node, key):
        """가득 차지 않은 노드에 키 삽입"""
        i = len(node.keys) - 1
        
        if node.is_leaf:
            # 리프 노드인 경우 직접 삽입
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            # 내부 노드인 경우 적절한 자식을 찾아 삽입
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            
            # 자식이 가득 찬 경우 분할
            if len(node.children[i].keys) == (2 * self.degree) - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
                    
            self._insert_non_full(node.children[i], key)
    
    def _split_child(self, parent, index):
        """자식 노드 분할"""
        degree = self.degree
        full_child = parent.children[index]
        new_child = BTreeNode(is_leaf=full_child.is_leaf)
        
        # 키를 반으로 나누기
        mid_index = degree - 1
        mid_key = full_child.keys[mid_index]
        
        # 새로운 자식에 오른쪽 절반 할당
        new_child.keys = full_child.keys[mid_index + 1:]
        
        # 기존 자식은 왼쪽 절반만 유지
        full_child.keys = full_child.keys[:mid_index]
        
        # 자식들도 분할 (리프가 아닌 경우)
        if not full_child.is_leaf:
            new_child.children = full_child.children[mid_index + 1:]
            full_child.children = full_child.children[:mid_index + 1]
        
        # 부모에 중간 키와 새로운 자식 추가
        parent.keys.insert(index, mid_key)
        parent.children.insert(index + 1, new_child)
    
    def delete(self, key):
        """키 삭제"""
        self._delete(self.root, key)
        
        # 루트가 비어있는 경우 새로운 루트 설정
        if len(self.root.keys) == 0:
            if not self.root.is_leaf:
                self.root = self.root.children[0]
    
    def _delete(self, node, key):
        """노드에서 키 삭제"""
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        
        if i < len(node.keys) and key == node.keys[i]:
            # 키를 찾은 경우
            if node.is_leaf:
                # 리프 노드에서 직접 삭제
                node.keys.pop(i)
            else:
                # 내부 노드에서 삭제
                self._delete_internal_node(node, key, i)
        elif not node.is_leaf:
            # 자식에서 삭제
            flag = (i == len(node.keys))
            
            if len(node.children[i].keys) < self.degree:
                self._fill(node, i)
            
            if flag and i > len(node.keys):
                self._delete(node.children[i - 1], key)
            else:
                self._delete(node.children[i], key)
    
    def _delete_internal_node(self, node, key, index):
        """내부 노드에서 키 삭제"""
        key = node.keys[index]
        
        # 왼쪽 자식이 충분한 키를 가진 경우
        if len(node.children[index].keys) >= self.degree:
            predecessor = self._get_predecessor(node, index)
            node.keys[index] = predecessor
            self._delete(node.children[index], predecessor)
        
        # 오른쪽 자식이 충분한 키를 가진 경우
        elif len(node.children[index + 1].keys) >= self.degree:
            successor = self._get_successor(node, index)
            node.keys[index] = successor
            self._delete(node.children[index + 1], successor)
        
        # 두 자식 모두 최소 개수의 키만 가진 경우
        else:
            self._merge(node, index)
            self._delete(node.children[index], key)
    
    def _get_predecessor(self, node, index):
        """이전 키 찾기"""
        current = node.children[index]
        while not current.is_leaf:
            current = current.children[-1]
        return current.keys[-1]
    
    def _get_successor(self, node, index):
        """다음 키 찾기"""
        current = node.children[index + 1]
        while not current.is_leaf:
            current = current.children[0]
        return current.keys[0]
    
    def _fill(self, node, index):
        """자식 노드의 키 개수 채우기"""
        # 왼쪽 형제에서 빌려오기
        if index != 0 and len(node.children[index - 1].keys) >= self.degree:
            self._borrow_from_prev(node, index)
        
        # 오른쪽 형제에서 빌려오기
        elif index != len(node.children) - 1 and len(node.children[index + 1].keys) >= self.degree:
            self._borrow_from_next(node, index)
        
        # 형제와 병합
        else:
            if index != len(node.children) - 1:
                self._merge(node, index)
            else:
                self._merge(node, index - 1)
    
    def _borrow_from_prev(self, node, index):
        """왼쪽 형제에서 키 빌려오기"""
        child = node.children[index]
        sibling = node.children[index - 1]
        
        child.keys.insert(0, node.keys[index - 1])
        
        if not child.is_leaf:
            child.children.insert(0, sibling.children.pop())
        
        node.keys[index - 1] = sibling.keys.pop()
    
    def _borrow_from_next(self, node, index):
        """오른쪽 형제에서 키 빌려오기"""
        child = node.children[index]
        sibling = node.children[index + 1]
        
        child.keys.append(node.keys[index])
        
        if not child.is_leaf:
            child.children.append(sibling.children.pop(0))
        
        node.keys[index] = sibling.keys.pop(0)
    
    def _merge(self, node, index):
        """자식 노드들 병합"""
        child = node.children[index]
        sibling = node.children[index + 1]
        
        child.keys.append(node.keys[index])
        child.keys.extend(sibling.keys)
        
        if not child.is_leaf:
            child.children.extend(sibling.children)
        
        node.keys.pop(index)
        node.children.pop(index + 1)
    
    def display(self, node=None, level=0):
        """트리 출력"""
        if node is None:
            node = self.root
            
        print("  " * level + f"레벨 {level}: {node.keys}")
        
        if not node.is_leaf:
            for child in node.children:
                self.display(child, level + 1)
    
    def inorder_traversal(self, node=None):
        """중위 순회"""
        if node is None:
            node = self.root
            
        result = []
        if node.is_leaf:
            result.extend(node.keys)
        else:
            for i in range(len(node.keys)):
                result.extend(self.inorder_traversal(node.children[i]))
                result.append(node.keys[i])
            result.extend(self.inorder_traversal(node.children[-1]))
        
        return result


def main():
    """B-Tree 예제 실행"""
    print("=== B-Tree 구현 예제 ===")
    print()
    
    # B-Tree 생성 (차수 3)
    btree = BTree(degree=3)
    print("차수 3인 B-Tree를 생성했습니다.")
    print()
    
    # 키 삽입 예제
    keys_to_insert = [10, 20, 5, 6, 12, 30, 7, 17, 15, 18, 25, 40, 16]
    print("다음 키들을 순서대로 삽입합니다:", keys_to_insert)
    print()
    
    for key in keys_to_insert:
        print(f"키 {key} 삽입...")
        btree.insert(key)
        print("현재 트리 구조:")
        btree.display()
        print()
    
    # 중위 순회 결과
    print("중위 순회 결과 (정렬된 순서):")
    sorted_keys = btree.inorder_traversal()
    print(sorted_keys)
    print()
    
    # 검색 예제
    search_keys = [6, 15, 25, 100]
    print("검색 예제:")
    for key in search_keys:
        result = btree.search(key)
        if result:
            print(f"키 {key}: 찾음 (노드: {result[0].keys}, 인덱스: {result[1]})")
        else:
            print(f"키 {key}: 찾을 수 없음")
    print()
    
    # 삭제 예제
    keys_to_delete = [6, 17, 20]
    print("삭제 예제:")
    for key in keys_to_delete:
        print(f"키 {key} 삭제 전:")
        btree.display()
        btree.delete(key)
        print(f"키 {key} 삭제 후:")
        btree.display()
        print("중위 순회:", btree.inorder_traversal())
        print()
    
    print("=== B-Tree 예제 완료 ===")


if __name__ == "__main__":
    main()
