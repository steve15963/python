import random


def binaryInsertionSort(arr, start, end):
    """Binary Insertion Sort - 하나의 함수로 구현"""
    if start >= end:
        return
    
    # start+1부터 end까지 하나씩 정렬된 부분에 삽입
    for i in range(start + 1, end + 1):
        key = arr[i]
        
        # 이진 탐색으로 삽입할 위치 찾기
        left = start
        right = i - 1
        
        # 이진 탐색 (함수 대신 인라인으로)
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        
        # left가 삽입할 위치
        insert_pos = left
        
        print(f"단계 {i-start}: 값 {key}를 위치 {insert_pos}에 삽입")
        print(f"구간 [{start}:{end}]: {arr[start:end+1]}")
        
        # 요소들을 오른쪽으로 한 칸씩 이동
        for j in range(i, insert_pos, -1):
            arr[j] = arr[j-1]
        
        # 키를 올바른 위치에 삽입
        arr[insert_pos] = key
        
        print(f"결과: {arr[start:end+1]}")
        print()

# 테스트 - quicksort.py와 같은 방식
numbers = [20, 61, 51, 14, 42]
print("=== Binary Insertion Sort (단일 함수) ===")
print(f"정렬 전: {numbers}")
binaryInsertionSort(numbers, 0, len(numbers)-1)
print(f"정렬 후: {numbers}")

# 추가 테스트
test_arrays = [
    [64, 34, 25, 12, 22, 11, 90],
    [5, 2, 8, 6, 1, 9, 4],
    [1, 2, 3, 4, 5],  # 이미 정렬된 경우
    [5, 4, 3, 2, 1],  # 역순
]

for i, test_array in enumerate(test_arrays):
    print(f"\n=== 테스트 {i+1} ===")
    original = test_array.copy()
    print(f"정렬 전: {original}")
    binaryInsertionSort(test_array, 0, len(test_array)-1)
    print(f"정렬 후: {test_array}")

print("\n=== 일반 Insertion Sort (비교용) ===")
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # 선형 탐색으로 위치 찾기
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
        print(f"단계 {i}: {arr}")
    
    return arr

numbers2 = [20, 61, 51, 14, 42]
print(f"정렬 전: {numbers2}")
insertion_sort(numbers2) 