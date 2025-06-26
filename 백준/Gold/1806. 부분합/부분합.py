N, S = map(int, input().split())
numbers = list(map(int, input().split()))

start = 0
end = 0
current_sum = 0
min_length = float('inf')

while True:
    if current_sum >= S:
        # 합이 S 이상일 경우
        min_length = min(min_length, end - start)
        current_sum -= numbers[start]
        start += 1
    elif end == N:
        # 끝까지 탐색했을 경우
        break
    else:
        # 합이 S 미만일 경우
        current_sum += numbers[end]
        end += 1

if min_length == float('inf'):
    print(0)
else:
    print(min_length)
