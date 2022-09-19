# 최단경로 알고리즘 - 길찾기 문제
# 각 지점 : 노드, 연결 도로 : 간선
# 코테에서는 다익스트라, 플로이드 워셜 알고리즘 많이 나옴
# 그리디, 동적계획법 알고리즘의 한 유형으로 볼 수도 있음

# 다익스트라 알고리즘
# 특정 노드에서 출발해 다른 모든 노드로 가는 최단 경로를 계산한다. 
# 음의 간선이 없을 때 정상적으로 동작
# 그리디 알고리즘으로 분류됨
# 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정 반복

# 그리디 알고리즘 : 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택해 임의의 과정을 반복
# 한 번 처리된 노드의 최단 거리는 고정
# 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해

# 다익스트라 간단한 방법 O(v 제곱)
# 노드가 5000개 이하여야 사용가능

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())

# 시작 노드
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]

# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)

# 최단거리 테이블을 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
  # a번 노드에서 b번노드로 가는 비용이 c라는 의미
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  # 시작 노드에 대해 초기화
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]
  # 시작 노드를 제외한 전체 n-1개으,ㅣ 노드에 대해 반복
  for i in range(n-1):
    # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
    now = get_smallest_node()
    visited[now] = True
    # 현재 노드와 연결된 다른 노드를 확인
    for j in graph[now]:
      cost = distance[now] + j[1]
      # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[j[0]]:
        distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

for i in range(1, n+1):
  print(distance[i])

# 다익스트라 개선된 구현 방법
# 우선순위 큐 - 우선순위가 가장 높은 데이터를 가장 먼저 삭제 하는 자료구조
# 여러개 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터 꺼내서 확인해야 하는 경우 사용
# 힙(Heap) - 우선순위 큐를 구현하기 위해 사용하는 자료구조 O(logN)
# 최소 힙, 최대 힙

import heapq # 기본적으로 최소힙으로 구현됨

def heapsort(iterable):
  h = []
  result = []
  #모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

# 개선된 구현 방법
# 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 힙 자료구조를 이용
# 다익스트라 알고리즘 동작하는 기본원리는 동일
# O(ElogV)

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n,m = map(int,input().split())

# 시작 노드
start = int(input())

# 각 노드 연결된 노드정보
graph = [[] for _ in range(n+1)]

# 최단 거리 테이블
distance = [INF for _ in range(n+1)]

# 경로 추적
trace = [0 for _ in range(n+1)]

# 모든 간선정보 입력 받기
for i in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))
  #graph[b].append((a,c)) # 양방향일 경우!

def dijkstra(start):
  q = []
  # 시작 노드로 가기 위한 최단 거리는 0으로 설정하며, 큐에 삽입
  heapq.heappush(q,(0, start))
  distance[start] = 0

  while q: # 큐가 비어있지 않다면
    # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if distance[now] < dist:
      continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      cost = dist + i[1]
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        trace[i[0]] = now
        heapq.heappush(q, (cost,i[0]))

dijkstra(start)

path = [finish]
tmp = trace[finish]
while tmp!=0:
  path.append(tmp)
  tmp = trace[tmp]
print(*path[::-1], sep='\n')

path = [finish]
temp = trace[finish]
while temp != 0:
  path.append(tmp)
  temp = trace[temp]
print(*path[::-1])

#########################

# 플로이드 워셜 알고리즘
# 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산
# 단계별로 거쳐 가는 노드를 기준으로 알고리즘 수행
# 다만 다익스트라처럼 매 단계마다 방문하지 않은 노드 중 최단 거리 노드를 찾는 과정은 필요없음
# 2차원 테이블에 최단거리 정보를 저장
# 다이나믹 프로그래밍 유형
# 점화식 : D(ab) = min(D(ab), D(ak) + D(kb))
# 특정 노드 K를 거쳐가는 경우를 확인
# O(n^3) 이기 때문에 노드의 개수 N이 작을때만 사용

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int,input().split())

# 2차원 리스트 (그래프 표현)을 만들고, 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기자신으로 가는 비용 0으로 초기화
for a in range(1,n+1):
  for b in range(1,n+1):
    if a == b:
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
  # a에서 b로 가는 비용 c
  a,b,c = map(int,input().split())
  graph[a][b] = c

# 점화식에 따라 플로이드 위셜 알고리즘 수행
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])

# 수행된 결과 출력
for a in range(1, n+1):
  for b in range(1,n+1):
    if graph[a][b] == INF:
      print("INFINITY", end=" ")
    else:
      print(graph[a][b], end=" ")
  print()