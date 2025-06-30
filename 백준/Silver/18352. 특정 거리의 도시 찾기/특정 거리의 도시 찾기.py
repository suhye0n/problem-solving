import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)] # graph[0]은 안 씀

# 단방향 그래프
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

dist = [-1] * (N+1) # -1: 미방문
dist[X] = 0 # 출발 도시 거리: 0

# BFS
queue = deque([X])
while queue:
    now = queue.popleft()
    for nxt in graph[now]:
        if dist[nxt] == -1: # 아직 방문 안 했으면
            dist[nxt] = dist[now] + 1
            queue.append(nxt)

result = []
for i, d in enumerate(dist):
    if d == K:
        result.append(i)

if result:
    for city in sorted(result):
        print(city)
else:
    print(-1)