import sys

from sympy import true

input = sys.stdin.readline

stack = []

input_list = list(
    map(
        int,
        input()
            .split()
    )
)

answer = [-1] * len(input_list)

# stack.append(0)

for i in range(len(input_list)):
    while stack and input_list[stack[-1]] < input_list[i]:
        answer[ stack.pop() ] = input_list[i]
        
    stack.append(i)

print(answer)







