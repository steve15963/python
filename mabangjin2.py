# 첫행의 중앙을 1로 두고 시작
# 시작 좌표, 우측 대각선 및 좌측 대각선 상대 좌표, 충돌시 이동 방향
startPoint = [
    [0,1, [[-1 , 1], [-1, -1]], [ 1, 0]], 
    [1,0, [[-1, -1], [ 1, -1]], [ 0, 1]], 
    [1,2, [[ 1,  1], [-1,  1]], [ 0,-1]], 
    [2,1, [[ 1,  1], [ 1, -1]], [-1, 0]]
]

# 출발.
for startY, startX, dyx, down in startPoint:
    for d in range(len(dyx)):
        matrix = [[-1] * 3 for _ in range(3)]
        y = startY
        x = startX
        matrix[y][x] = 1
        for i in range(2,10):
            newY = (y + dyx[d][0]) % 3
            newX = (x + dyx[d][1]) % 3
            if matrix[newY][newX] == -1:
                y = newY
                x = newX
            else:
                y = (y + down[0]) % 3
                x = (x + down[1]) % 3
            matrix[y][x] = i
        print(matrix)