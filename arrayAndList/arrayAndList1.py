import sys

input = sys.stdin.readline

n, m = map(int, input().split())

input_list = [
    [0] * ( n + 1 )
]
SubSum = [
    [0] * ( n + 1 )
    for _ in range( n + 1 )
]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    input_list.append(A_row)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        SubSum[i][j] = SubSum[i][j - 1] + SubSum[i - 1][j] - SubSum[i - 1][j - 1] + input_list[i][j]

print(input_list)
print(SubSum)

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = SubSum[x2][y2] - SubSum[x1 - 1][y2] - SubSum[x2][y1 - 1] + SubSum[x1 - 1][y1 - 1]
    print(result)