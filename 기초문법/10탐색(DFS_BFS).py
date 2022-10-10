문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.


from collections import deque

n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def BFS(start):
  queue = deque()
  queue.append(start)
  
  visited[start] = True

  while queue:
    v = queue.popleft();
    print(v, end=' ')
    graph[v].sort()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

def DFS(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  graph[v].sort()
  for i in graph[v]:
    if not visited[i]:
      DFS(graph,i, visited)
        
DFS(graph, v, visited)
print()
visited = [False for _ in range(n+1)]
BFS(v)

--------

from collections import deque


n,m = map(int,input().split())

graph = []

for i in range(n):
    graph[i].append(list(map(int,input().split())))
    
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx >= x or ny<0 or ny>=y:
                continue
            
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
            
    return graph[n-1][m-1]

print(bfs)