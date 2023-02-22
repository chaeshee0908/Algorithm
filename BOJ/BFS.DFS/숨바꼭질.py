# 실버1 1697번
# https://www.acmicpc.net/problem/1697

from collections import deque

n, k = map(int, input().split())
dist = [0] * 100001

def bfs(x):
    queue = deque([x])
    while queue:
        x = queue.popleft()
        if x == k:
            print(dist[x])
            break
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= 100000 and not dist[i]:
                dist[i] = dist[x] + 1
                queue.append(i)

bfs(n)