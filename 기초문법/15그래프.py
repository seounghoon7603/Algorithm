# 서로소 집합 : 공통 원소가 없는 두 집합
# 서로소 집합 자료구조
# - 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
# - 서로소 집합 자료구조는 두 종류의 연산을 지원
#   - 합집합 : 두개의 원소가 포합된 집합을 하나의 집합으로 합치는 연산
#   - 찾기 : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
# - 서로소 집합 자료구조는 합치기 찾기 자료구조 라고도 불림

# 기본 서로소 집합 자료구조는 루트 노드 찾기 위해 부모 테이블 계속 확인해야 함

###
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  # 루트 노드를 찾을 때까지 재귀 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기 
v,e = map(int, input().split())
parent = [0] * (v+1) # 부모테이블 초기화

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
  parent[i] = i

#Union 연산을 각각 수행
for i in range(e):
  a,b = map(int, input().split())
  union_parent(parent, a,b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합 : ', end = '')
for i in range(1, v+1):
  print(find_parent(parent, i), end = ' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블 : ', end='')
for i in range(1,v+1):
  print(parent[i], end=' ')

###

# 서로소 집합을 활용한 사이클 판별
# 서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용
# (방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별)
# 사이클 판별 알고리즘
# 1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인
#   1) 루트 노드가 서로 다르다면 두 노드에 대하여 합집합 연산 수행
#   2) 루트 노드가 서로 같다면 사이클(Cycle)이 발생한 것.
# 2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정 반복

###

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  # 루트 노드를 찾을 때까지 재귀 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기 
v,e = map(int, input().split())
parent = [0] * (v+1) # 부모테이블 초기화

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
  parent[i] = i

Cycle = False # 사이클 발생 여부

for i in range(e):
  a,b = map(int, input().split())
  if find_parent(parent,a) == find_parent(parent,b):
    Cycle = True
    break
  else:
    union_parent(parent,a,b)

if Cycle:
  print('사이클 발생')
else:
  print('사이클 없음')

###

# 신장 트리
# 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 '트리'의 조건이기도 함

# 최소 신장 트리
# 퇴소한의 비용으로 구성되는 신장 트리를 찾아야 할 때
# ex) N개의 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결될 수 있게 도로를 설치하는 경우

# 크루스칼 알고리즘 O(ElogE)
# 대표적인 최소 신장 트리 알고리즘 ( 그리디 알고리즘으로 분류 )
# 동작과정
# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
#   1) 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
#   2) 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않음
# 3. 모든 간선에 대하여 2번과정 반복

###
def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  else:
    parent[x]

def union_parent(parent, a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력
v,e = map(int, input().split())
parent = [0 for _ in range(v+1)]

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
  parent[i] = i

# 모든 간선에 대한 정보를 입력
for _ in range(e):
  a,b, cost = map(int, input().split())
  # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
  edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
  cost, a, b = edge
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)

###

# 위상 정렬
# '사이클이 없는 방향 그래프(DAG)'의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것을 의미.
# ex) 선수과목을 고려한 학습 순서 설정

# 진입차수 : 특정한 노드로 들어오는 간선의 개수 (indegree)
# 진출차수 : 특정한 노드에서 나가는 간선의 개수 (outdegree)

# 위상 정렬 알고리즘 O(V+E)
# 큐를 이용하는 위상 정렬 알고리즘 동작 과정
# 1. 진입차수가 0인 모든 노드를 큐에 넣는다.
# 2. 큐가 빌 때까지 다음의 과정을 반복
#  1) 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다.
#  2) 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
# ==> 결과적으로 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과와 같다.

# 특징
# DAG(순환하지 않는 방향 그래프) 만족해야 함
# 여러 가지 답 존재 가능
# 모든 원소를 방문하기 전 큐가 빈다면 사이클이 존재한다고 판단할 수 있음
# 스택을 활용한 DFS를 이용해 위상정렬 수행도 가능

###
from collections import deque

# 노드의 개수와 간선의 개수를 입력 받기
v,e = map(int, input().split())

# 모든 노드에 대한 진입차수 0으로 초기화
indegree = [0 for _ in range(v+1)]

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
  a,b = map(int, input().split())
  graph[a].append(b) # 정점 A에서 B로 이동 가능
  # 진입 차수를 1증가
  indegree[b] += 1

#위상 정렬 함수
def topology_sort():
  result = [] # 알고리즘 수행 결과를 담을 리스트
  q = deque() # 큐 기능을 위한 deque 라이브러리 사용
  # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)

  # 큐가 빌때까지 반본
  while(q):
    # 큐에서 원소 꺼내기
    now = q.popleft()
    result.append(now)
    #해당 원소와 연결된 노드들의 진입차수에서 1빼기
    for i in graph[now]:
      indegree[i] -= 1
      # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)

  # 위상 정렬을 수행한 결과 출력
  for i in result:
    print(i, end=' ')

topology_sort()

###