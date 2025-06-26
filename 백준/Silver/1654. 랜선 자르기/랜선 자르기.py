import sys

K, N = map(int, input().split()) # 가지고 있는 랜선 수, 필요한 랜선 수
cables = []

for _ in range(K):
    length = int(sys.stdin.readline())
    cables.append(length)

# 이분 탐색 범위
start = 1
end = max(cables)

while start <= end:
    mid = (start + end) // 2 # 자를 길이
    count = 0 # 만들어지는 랜선 개수

    for cable in cables:
        count += cable // mid # mid 길이로 잘랐을 때 몇 개 나오는지

    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
