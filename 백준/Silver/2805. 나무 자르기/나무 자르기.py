N, M = map(int, input().split())
trees = list(map(int, input().split()))

# 이분 탐색 범위
low = 0
high = max(trees)

while low <= high:
    mid = (low + high) // 2 # 자를 높이
    total = 0 # 잘라서 얻은 나무 길이 합계

    for height in trees:
        if height > mid:
            total += height - mid # 자른 부분 더하기

    if total >= M:
        low = mid + 1
    else:
        high = mid - 1

print(high)
