# 주요 라이브러리

# itertools - 반복되는 형태의 데이터를 처리하는 기능 제공, 순열과 조합 라이브러리를 제공

# data = ['A','B','C']
# 모든 경우의 수를 고려해야 할 떄!

#순열 - 서로다른 n개에서 서로다른 r개 선택해서 일렬로 나열하는 것 nPr (permutations) ==> list(permutaions(data,r))

#조합 - 서로다른 n개에서 순서상관없이 서로 다른 r개를 선택하는 것 nCr (combinations) ==> list(combinations(data,r))

#product는 순열과 같이 객체에서 r개 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산 ( 다만 원소를 중복하여 뽑음 ) ==> list(product(data, repeat=r))

#combinations_with_replacement는 조합과 같이 객체에서 r개의 데이터를 뽑아 수선를 고려하지 않고 나열하는 모든 경우를 계산 ( 다만 원소를 중복하여 뽑음 ) ==> list(combinations_with_replacement(data,r))

# heapq - 힙 자료구조를 제공 - 일반적으로 우선순위 큐 기능을 구현하기 위해 사용 ( 다익스트라 )
# 힙 삽입 : heapq.heappush(), 삭제 : heappop()
import heapq

def heapsort(iterable):
  h = []
  result = []
  for value in iterable:
    heapq.heappush(h, value)
  
  print(h)

  for _ in range(len(h)):
    result.append(heapq.heappop(h))
    
  return result

result = heapsort([1,5,3,6,4,7])
print(result)
#최대 힙 을 위해서는 넣고 뺄때 -부호로 임시변경


# bisect - 이진 탐색 기능을 제공 ( 정렬된 배열 에서 특정한 원소를 찾아야 할 떄 매우 효과적으로 사용))
# bisect_left(a,x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a,x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
# ex) 정렬된 [1,2,4,4,8] 에 4를 삽입하려 할때 bisect_left는 2, bisect_right는 4 인덱스 번호를 반환
# bisect 함수는 정렬된 리스트에서 특정범위에 속하는 원소의 개수를 구하조가 할때 효과적
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a,right_value)
  left_index = bisect_left(a,left_value)
  return right_index - left_index

a= [1,2,3,3,3,3,4,4,4,5,6]

print(count_by_range(a,4,4))
print(count_by_range(a,3,4))

# collections - 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함함
# deque를 사용해 큐를 구현함 ( 큐 : 선입선출 )
# 리스트에서 append() 하거나, pop()할때 마지막원소를 기준으로 수행됨 따라서 앞쪽에 있는 원소 처리할때는 리스트에 포함된 데이터의 개수에 따라 많은 시간 걸릴 수 있음 O(N) - deque 사용시 O(1)
# deque는 리스트와 달리 인덱싱, 슬라이싱은 불가 - 다만 연속적으로 나열된 데이터의 시작or끝부분 데이터 삽입삭제 매우 효과적 - 스택이나 큐의 기능을 모두 포함 ( 스택 큐 대용으로 사용 )
# popleft() : 첫번째 원소 제거, pop() 마지막원소 제거, appendleft(x) 첫번째 인덱스에 원소삽입, append(x)
# 따라서 deque를 큐 자료구조로 이용할 때 원소삽입은 append() 삭제는 popleft()를 사용하면 됨
from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

# collections라이브러리의 Counter는 등장 횟수를 세는 기능 제공 - 리스트와 같은 iterable 객체가 주어졌을 때,객체 내부의 원소가 몇 번씩 등장했는지를 알려줌
from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(counter['red'])
print(dict(counter))

# math - 필수적인 수학적 기능을 제공 - 팩토리얼, 제곱근, 최대공약수, 삼각함수 관련 함수부터 파이와 같은 상수 포함
#sum, min, max, eval, sorted,
# math 라이브러리의 factorial 함수는 x! 값을 반환함
import math
print(math.factorial(5)) # 5!
# math 라이브러리의 sqrt(x) 함수는 x의 제곱근을 반환 
import math
print(math.sqrt(7)) # 2.64575...
# 최대공약수는 gcd(a,b) 함수 사용
import math
print(math.gcd(21,14)) # 7
# 상수가 필요할때도 사용
import math
print(math.pi) # 파이(pi) 출력 3.14159...
print(math.e) # 자연상수 e 출력 2.7182...