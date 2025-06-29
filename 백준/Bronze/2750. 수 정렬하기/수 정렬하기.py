N = int(input())
arr = []

for _ in range(N):
    num = int(input())
    arr.append(num)

# 선택 정렬
for i in range(N):
    min_idx = i
    for j in range(i + 1, N):
        if arr[j] < arr[min_idx]:
            min_idx = j
    temp = arr[i]
    arr[i] = arr[min_idx]
    arr[min_idx] = temp

for num in arr:
    print(num)