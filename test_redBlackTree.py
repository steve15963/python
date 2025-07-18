# test_redBlackTree.py

from redBlackTree import RedBlackTree

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