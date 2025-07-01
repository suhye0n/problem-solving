N, k = map(int, input().split())
arr = list(map(int, input().split()))

# 선택 정렬
for i in range(N):
    min_idx = i
    for j in range(i+1, N):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr[N-k])