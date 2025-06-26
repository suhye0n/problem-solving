from collections import deque

N = int(input()) # 지역 크기
graph = [] # 지역 높이
max_h = 0 # 최대 높이

for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    for h in row:
        if h > max_h:
            max_h = h # 최대 높이 갱신

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, height, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > height and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

count = 0

for h in range(max_h):
    visited = [[False]*N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            # 물에 잠기지 않고 방문하지 않았다면
            if graph[i][j] > h and not visited[i][j]:
                bfs(i, j, h, visited)
                cnt += 1 # bfs 끝날 때마다 +1

    if cnt > count:
        count = cnt

print(count)
