import io
import sys


def test_bellman_ford():
    # 테스트 케이스들
    test_cases = [
        {
            "name": "테스트 1: 일반적인 음수 가중치 포함",
            "input": """4 5
0
0 1 1
0 2 4
1 2 -3
1 3 2
2 3 1""",
            "expected": "0, 1, -2, -1 (시작점 0에서 각 노드까지의 최단거리)"
        },
        {
            "name": "테스트 2: 음수 사이클 존재",
            "input": """3 3
0
0 1 1
1 2 -3
2 0 1""",
            "expected": "음수 사이클 감지"
        },
        {
            "name": "테스트 3: 도달 불가능한 노드",
            "input": """4 2
0
0 1 5
2 3 3""",
            "expected": "0, 5, -1, -1"
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*60}")
        print(f"{test_case['name']}")
        print(f"{'='*60}")
        print("입력:")
        print(test_case['input'])
        print("\n예상 결과:", test_case['expected'])
        print("\n실제 결과:")
        
        # 표준 입력을 테스트 데이터로 변경
        old_stdin = sys.stdin
        sys.stdin = io.StringIO(test_case['input'])
        
        try:
            # belmanpord3.py의 코드를 직접 실행
            exec(open('belmanpord3.py').read())
        except Exception as e:
            print(f"오류 발생: {e}")
        finally:
            # 표준 입력 복원
            sys.stdin = old_stdin

if __name__ == "__main__":
    test_bellman_ford() 