import sys

T = int(sys.stdin.readline())

for _ in range(T):
    line = sys.stdin.readline()
    A, B = line.split()
    A_list = list(A)
    B_list = list(B)

    # 버블 정렬
    n = len(A_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if A_list[j] > A_list[j + 1]:
                A_list[j], A_list[j + 1] = A_list[j + 1], A_list[j]

    # 버블 정렬
    m = len(B_list)
    for i in range(m):
        for j in range(0, m - i - 1):
            if B_list[j] > B_list[j + 1]:
                B_list[j], B_list[j + 1] = B_list[j + 1], B_list[j]

    sorted_A = ''.join(A_list)
    sorted_B = ''.join(B_list)

    if (sorted_A == sorted_B):
        print(f"{A} & {B} are anagrams.")
    else:
        print(f"{A} & {B} are NOT anagrams.")