import sys
from collections import deque

input = sys.stdin.readline

inputSize, slideSize = map(int,input().split())

input_list = list(map(int, input().split()))

slideWindow = deque()

for i in range(inputSize):
    if i < slideSize:
        slideWindow.append(input_list[i])
    else:
        slideWindow.append(input_list[i])
        slideWindow.popleft()

    print(min(slideWindow), end = ' ')

