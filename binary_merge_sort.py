import random


def binaryMergeSort(arr, left, right):
    """Binary Merge Sort - 분할 정복 + 이진 탐색 병합"""
    if left >= right:
        return
    
    print(f"분할: [{left}:{right}] = {arr[left:right+1]}")
    
    # 중간점 계산
    mid = (left + right) // 2
    
    # 왼쪽과 오른쪽 각각 재귀적으로 정렬
    binaryMergeSort(arr, left, mid)      # 왼쪽 절반
    binaryMergeSort(arr, mid + 1, right) # 오른쪽 절반
    
    # 이진 탐색을 이용한 병합
    binaryMerge(arr, left, mid, right)

def binaryMerge(arr, left, mid, right):
    """이진 탐색을 활용한 병합 함수"""
    print(f"병합: 왼쪽 {arr[left:mid+1]} + 오른쪽 {arr[mid+1:right+1]}")
    
    # 임시 배열 생성
    temp_left = arr[left:mid+1]
    temp_right = arr[mid+1:right+1]
    
    result = []
    i, j = 0, 0
    
    # 두 배열을 병합하면서 이진 탐색 활용
    while i < len(temp_left) and j < len(temp_right):
        if temp_left[i] <= temp_right[j]:
            result.append(temp_left[i])
            i += 1
        else:
            # 이진 탐색으로 temp_right[j]가 들어갈 위치 찾기
            pos = binary_search_position(temp_left, temp_right[j], i, len(temp_left)-1)
            
            # temp_right[j]를 먼저 추가
            result.append(temp_right[j])
            j += 1
    
    # 남은 요소들 추가
    while i < len(temp_left):
        result.append(temp_left[i])
        i += 1
    
    while j < len(temp_right):
        result.append(temp_right[j])
        j += 1
    
    # 원본 배열에 복사
    for k in range(len(result)):
        arr[left + k] = result[k]
    
    print(f"병합 결과: {arr[left:right+1]}")
    print()

def binary_search_position(arr, target, start, end):
    """이진 탐색으로 target이 들어갈 위치 찾기"""
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

# 일반적인 Merge Sort (비교용)
def normalMergeSort(arr, left, right):
    """일반적인 Merge Sort"""
    if left >= right:
        return
    
    mid = (left + right) // 2
    normalMergeSort(arr, left, mid)
    normalMergeSort(arr, mid + 1, right)
    normalMerge(arr, left, mid, right)

def normalMerge(arr, left, mid, right):
    """일반적인 병합 함수"""
    temp_left = arr[left:mid+1]
    temp_right = arr[mid+1:right+1]
    
    i = j = 0
    k = left
    
    while i < len(temp_left) and j < len(temp_right):
        if temp_left[i] <= temp_right[j]:
            arr[k] = temp_left[i]
            i += 1
        else:
            arr[k] = temp_right[j]
            j += 1
        k += 1
    
    while i < len(temp_left):
        arr[k] = temp_left[i]
        i += 1
        k += 1
    
    while j < len(temp_right):
        arr[k] = temp_right[j]
        j += 1
        k += 1

# 테스트 - quicksort.py와 같은 방식
numbers = [20, 61, 51, 14, 42]
print("=== Binary Merge Sort ===")
print(f"정렬 전: {numbers}")
binaryMergeSort(numbers, 0, len(numbers)-1)
print(f"정렬 후: {numbers}")

print("\n" + "="*50)

# 비교용 일반 Merge Sort
numbers2 = [20, 61, 51, 14, 42]
print("=== 일반 Merge Sort (비교용) ===")
print(f"정렬 전: {numbers2}")
normalMergeSort(numbers2, 0, len(numbers2)-1)
print(f"정렬 후: {numbers2}")

# 추가 테스트
test_arrays = [
    [64, 34, 25, 12, 22, 11],
    [5, 2, 8, 6, 1, 9],
    [1, 2, 3, 4, 5],  # 이미 정렬된 경우
    [5, 4, 3, 2, 1],  # 역순
]

print("\n=== 추가 테스트 ===")
for i, test_array in enumerate(test_arrays):
    print(f"\n테스트 {i+1}: {test_array}")
    test_copy = test_array.copy()
    binaryMergeSort(test_copy, 0, len(test_copy)-1)
    print(f"결과: {test_copy}") 