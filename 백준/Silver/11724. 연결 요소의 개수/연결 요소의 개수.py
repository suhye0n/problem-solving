from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

# 간선 정보 입력
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
count = 0

for i in range(1, N+1):
    if not visited[i]:
        bfs(graph, i, visited)
        count += 1 # bfs 끝날 때마다 +1

print(count)
