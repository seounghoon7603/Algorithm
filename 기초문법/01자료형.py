#리스트 자료형

#크기가 10이고 모든값이 0인 1차원리스트
a = [0] * 10

#리스트 컴프리헨션
#리스트를 초기화하는방법으로 []안에 조건문 반목문 넣는 방식
array = [i for i in range(10)]

print(array)
# 두번째 원소부터 네번째 원소까지
print(array[1:4])

array2 = [i for i in range(20) if i % 2 == 1]

print(array2)

n = 4
m = 3
array3 = [[0] * m for _ in range(n)]

print(array3)

a = [1,2,3,4,5,5,5,5] 
remove_set = {3,5}
result = [i for i in a if i not in remove_set]
print(result)

a = "안녕"
b = "아아아아"
print(a+b)

#튜플 ( 공간 활용적 ) - 변경 불가능
#서로 다른 성질의 데이터 묶어서 관리해야 할 떄 - 최단경로알고리즘(비용,노드번호)
# - 해싱의 키값,  
a = (1,2,3,4,5,6)
print (a[1])

#사전자료형 - 키,값의 쌍을 데이터로 가짐
#해시테이블을 사용하여 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리 가능
#키만 뽑을때 keys(), 값만뽑을때 values()
data = dict()
data['a'] = 'Apple'
data['b'] = 'banana'
data['c'] = 'CAdns'
data['d'] = 'Dafdsv'
if 'a' in data:
  print('존재')

key_list = list(data.keys())
print(key_list)

#집합 자료형
# 중복허용 x, 순서없음
# 리스트 혹은 문자열을 이용해 초기화 가능 set()
# 데이터 조회 및 수정에 있어 O(1)의 시간
a = {1,2,3,4,5}
b = {3,4,5,6,7}
#합집합
print(a|b)
#교집합
print(a&b)
#차집합
print(a-b)
#원소추가
a.add(9)
#원소 여러개 추가
a.update([7,8])
#특정한 값을 갖는 원소 삭제
a.remove(4)