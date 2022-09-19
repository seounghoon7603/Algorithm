# 이진탐색 문제는 입력 데이터가 많거나, 탐색범위가 큼
# 입력데이터가 많을경우 빠르게 입력받을 수 있는 sys 라이브러리 사용
import sys
input_data = sys.stdin.readline().rstrip()

# while문을 이용한 이진탐색
def binary_search(array,target,start,end):
  while start <= end:
    mid = (start+end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None


# 값이 특정 범위에 속하는 데이터 개수 구하기
# bisect는 정렬된 배열에 특정값이 들어갈 위치(인덱스번호)를 알려준다.
from bisect import bisect_left, bisect_right

def count_by_range(array,left_value,right_value):
  right_index = bisect_right(array,right_value)
  left_index = bisect_left(array,left_value)
  return right_index - left_index

# 파라메트릭 서치 ( 이진탐색으로 해결 가능 )
# 최적화 문제를 결정 문제(yes or no)로 바꾸어 해결하는 기법
# ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
