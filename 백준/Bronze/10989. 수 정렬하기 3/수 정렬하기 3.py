import sys

input = sys.stdin.readline

N = int(input())
MAX_NUM = 10000

count = [0] * (MAX_NUM + 1)

for _ in range(N):
    num = int(input())
    count[num] += 1

# 계수 정렬
for i in range(1, MAX_NUM + 1):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)