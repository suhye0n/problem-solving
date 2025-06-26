from collections import deque

T = int(input())

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, farm, visited, M, N): # queue가 비었다 = 모두 탐색하였다
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        # 상하좌우 방향으로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 밭 바깥으로 나갔을 경우
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            # 배추가 있고, 탐색하지 않았을 경우
            if farm[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

for _ in range(T):
    M, N, K = map(int, input().split())

    farm = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]

    # 배추 위치
    for _ in range(K):
        x, y = map(int, input().split())
        farm[x][y] = 1

    # 지렁이
    warm = 0

    for i in range(M):
        for j in range(N):
            if farm[i][j] == 1 and not visited[i][j]:
                bfs(i, j, farm, visited, M, N)
                warm += 1 # bfs 끝날 때마다 +1

    print(warm)