import random
import sys

input = sys.stdin.readline

numbers = [random.randint(1, 100) for _ in range(5)]
numbers = [20, 61, 51, 14, 42]

def quickSort(numbers, start, end):
    
    left = start
    right = end
    
    if left >= right:
        return
    
    pivot = (left+right)//2
    pivotValue = numbers[pivot]
    
    print(f"start: {start}, end: {end}")
    print(numbers[start:end+1])
    
    while left <= right:
        while left <= right and numbers[left] < pivotValue:
            left += 1
        while left <= right and numbers[right] > pivotValue:
            right -= 1
        if left <= right:
            # 교환(swap)
            print(f"pivot: {pivot}({numbers[pivot]}), left: {left}({numbers[left]}), right: {right}({numbers[right]})")
            numbers[left], numbers[right] = numbers[right], numbers[left]
            print(numbers)
            left += 1
            right -= 1
            

    # 올바른 재귀 호출 - 분할된 지점을 사용
    print(f"start: {start}, right: {right}")
    quickSort(numbers, start, right)    # 왼쪽 부분
    print(f"left: {left}, end: {end}")
    quickSort(numbers, left, end)       # 오른쪽 부분

print(numbers)
quickSort(numbers, 0, len(numbers)-1)