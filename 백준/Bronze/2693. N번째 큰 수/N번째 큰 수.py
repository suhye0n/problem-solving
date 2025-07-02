import sys

T = int(sys.stdin.readline())

for _ in range(T):
    arr = list(map(int, sys.stdin.readline().split()))

    # 버블 정렬 (내림차순)
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(arr[2])