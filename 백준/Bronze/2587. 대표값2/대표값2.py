arr = []

for i in range(5):
    arr.append(int(input()))

# 선택 정렬
for i in range(5):
    min_idx = i
    for j in range(i+1, 5):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(int(sum(arr)/5))
print(arr[2])