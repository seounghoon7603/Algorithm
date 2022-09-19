# 정렬 

# [선택정렬] O(N^2)
# 가장 작은 값을 선택해 맨앞 데이터와 바꾸기
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
  min_idx = i
  for j in range(i+1,len(array)):
    if array[j] < array[min_idx]:
      min_idx = j
  array[i], array[min_idx] = array[min_idx], array[i]
#print(array)

# [삽입정렬] O(N^2)
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(array)):
  for j in range(i, 0, -1):
    if array[j] < array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break
#print(array)

#[퀵정렬] O(NlogN)
# 기준데이터를 설정, 기준보다 큰데이터와 작은데이터 위치를 바꿈
array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(array, start, end):
  if start >= end: # 원소가 1개인 경우 종료
    return
  pivot = start # 기준데이터는 첫번째 원소
  left = start + 1
  right = end
  while left <= right:
    # 기준데이터보다 큰 데이터를 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]:
      left += 1
    # 기준데이터보다 작은 데이터를 찾을 때까지 반복
    while right > start and array[right] >= array[pivot]:
      right -= 1
    if left > right: # 엇갈렸으면 기준점과 작은값 교체
      array[pivot], array[right] = array[right], array[pivot]
    else: # 엇갈리지 않았으면 작은데이터와 큰데이터 교체
      array[left], array[right] = array[right], array[left]
  #분활 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
#print(array)

#파이썬 코드를 활용한 퀵정렬
array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort2(array):
  # 리스트가 하나 이하의 원소만을 담고 있다면 종료
  if len(array) <= 1:
    return array
  pivot = array[0] # 기준점은 첫번째 원소
  tail = array[1:] # 기준점 제외 리스트
  left_side = [x for x in tail if x <= pivot] # 분활된 왼쪽 부분
  right_side = [x for x in tail if x > pivot] # 분활된 오른쪽 부분
  return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)
#print(quick_sort2(array))

#[계수정렬] O(N+K)
# 데이터크기 범위가 제한되어 정수 형태로 표현 할 수 있을 때
array = [7,5,9,0,3,1,6,2,9,1,8,0,5,2]
#모든 범위를 포함하는 리스트 선언
count = [0] * (max(array) + 1)
for i in range(len(array)):
  count[array[i]] += 1  # 각 데이터에 해당하는 인덱스값 증가
for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')