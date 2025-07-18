import sys

input = sys.stdin.readline

n, m = map(int,input().split())

input_list = list(map(int, input().split()))

subSum = [0] * n
subDivide = [0] * m

answer = 0

subSum[0] = input_list[0]
for i in range(1, n) :
    subSum[i] = subSum[i - 1] + input_list[i] 

for i in range(n):
    remainder = subSum[i] % m
    if remainder == 0:
        answer += 1
    subDivide[remainder] += 1
    
print(answer)

for i in range(m):
    if subDivide[i] > 1:
        answer += ( subDivide[i] * (subDivide[i] - 1) // 2 )
        print('     ' + str(answer))
        print('     ' + str(subDivide[i]))
        
print(answer)

print(subDivide)
print(subSum)
