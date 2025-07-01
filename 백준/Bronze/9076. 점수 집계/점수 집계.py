T = int(input())
arr = []

for _ in range(T):
    a, b, c, d, e = map(int, input().split())
    arr = [a, b, c, d, e]

    # 선택 정렬
    for i in range(5):
        min_idx = i
        for j in range(i+1, 5):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    arr.remove(arr[4])
    arr.remove(arr[0])

    if (arr[2] - arr[0] >= 4):
        print("KIN")
    else:
        print(sum(arr))