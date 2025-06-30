import sys

n = int(sys.stdin.readline())
# 친구 관계
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

INF = 1000

# 거리 표
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j: # 자기 자신
            dist[i][j] = 0
        elif graph[i][j] == 'Y': # 친구
            dist[i][j] = 1

# 플로이드 워셜
for i in range(n): # 중간 친구
    for j in range(n): # 시작
        for k in range(n): # 도착
            if dist[j][k] > dist[j][i] + dist[i][k]:
                dist[j][k] = dist[j][i] + dist[i][k]

max_count = 0
for i in range(n):
    count = 0
    for j in range(n):
        if i != j and dist[i][j] <= 2:
            count += 1
    if count > max_count:
        max_count = count

print(max_count)