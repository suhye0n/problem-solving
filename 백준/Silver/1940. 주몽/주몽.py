N = int(input())
M = int(input())
materials = list(map(int, input().split()))

materials.sort()

# 이분 탐색 범위
left = 0
right = N - 1

# 만들 수 있는 갑옷 개수
count = 0

while left < right:
    total = materials[left] + materials[right]

    if total == M:
        count += 1
        left += 1
        right -= 1
    elif total < M:
        left += 1
    else:
        right -= 1

print(count)
