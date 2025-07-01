A, B, C = map(int, input().split())
arr = [A, B, C]

# 선택 정렬
for i in range(3):
    min_idx = i
    for j in range(i+1, 3):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr[1])