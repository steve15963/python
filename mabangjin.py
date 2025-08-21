# 해커랭크 
#https://www.hackerrank.com/challenges/magic-square-forming
import sys

input = sys.stdin.readline

#-------------- create Magic Square start -------------------

preMatrix = []

# 첫행의 중앙을 1로 두고 시작
startPoint = [
    [0,1], 
    [1,0], 
    [1,2], 
    [2,1]
]

# 우측 대각선 및 좌측 대각선 상대 좌표.
dyx = [
    [
        [-1 ,  1],
        [-1 , -1]
    ],
    [
        [-1, -1],
        [ 1, -1]
    ],
    [
        [ 1,  1],
        [-1,  1]
    ],
    [
        [ 1,  1],
        [ 1,  -1]
    ]
]

#충돌시 이동 방향향
dd =[
    [ 1, 0],
    [ 0, 1],
    [ 0,-1],
    [-1, 0]
]

# 출발.
for rotate,(startY, startX) in enumerate(startPoint):
    for d in range(len(dyx[rotate])):
        matrix = [[-1] * 3 for _ in range(3)]
        y = startY
        x = startX
        matrix[y][x] = 1
        for i in range(2,10):
            newY = (y + dyx[rotate][d][0]) % 3
            newX = (x + dyx[rotate][d][1]) % 3
            if matrix[newY][newX] == -1:
                y = newY
                x = newX
            else:
                y = (y + dd[rotate][0]) % 3
                x = (x + dd[rotate][1]) % 3
            matrix[y][x] = i
        preMatrix.append(matrix)
        print(matrix)

#-------------- create Magic Square End -------------------

# Input Start
inputMatrix = []

for i in range(3):
    line = list(map(int,input().split(' ')))
    inputMatrix.append(line)
    
# Input End

# Search Start

# 최소 비용 초기화
minCost = sys.maxsize

# 모든 마방진 탐색
for matrix in preMatrix:
    # 비용 초기화
    current_Cost = 0
    # 가능한 마방진의 모든 칸을 탐색하여 오차 계산
    for y in range(3):
        for x in range(3):
            # 다른 값이 있는 경우 오차 계산산
            if matrix[y][x] != inputMatrix[y][x]:
                current_Cost += abs(matrix[y][x] - inputMatrix[y][x])
    # 최소 비용 갱신
    minCost = min(minCost, current_Cost)

#출력
print(minCost)
            




