#코테에서 자주 사용되는 입출력
#input() 한줄의 문자열 입력 받음
#map() 리스트의 모든 원소에 각각 특정한 함수를 적용할 떄 사용

#ex) 공백을 기준으로 구분된 데이터를 입력 받을 떄는 다음과 같다
list(map(int, input().split()))

#ex) 공백을 기준으로 구분된 데이터의 개수가 많지 않다면
a, b, c = map(int, input().split())

#빠르게 입력 받기
#사용자한테 빠르게 입력 받아야 하는 경우
# sys.stdin.readline() 사용
# 단, 입력 후 엔터가 입력되니까 
# rstrip() 같이 사용 - 줄바꿈 제거

import sys
data = sys.stdin.readline().rstrip()
print(data)


######################

array = [('홍길동', 50),('이순신', 32),('아무개', 74)]

def my_key(x):
  return x[1]

print(sorted(array, key=my_key))

print(sorted(array, key=lambda x: x[1]))

array.sort(key=lambda x: x[1])
print(array)

list1 = [1,2,3,4,5]
list2 = [6,7,8,10]

result = map(lambda a, b: a + b, list1, list2)

print(list(result))