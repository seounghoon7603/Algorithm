# 그리디 알고리즘(탐욕법)은 현재 상황에서 지금 당장 좋은 것만 고르는 방법을 의미. 
# 일반적인 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구합니다.
# 그리디 해법은 그 정당성 분석이 중요
# 단순히 가장 좋아 보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지 검토가 필요

# 동전문제

# 큰 수의 법칙 ( 반복되는 수열 파악 )
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙.
# 단, 배열의 특정 인덱스에 해당하는 수가 연속해서 k번을 초과하여 더해질 수 없다.
# 배열크기 n
# 더하는 횟수 m
# 같은인덱스 k번 더하기 가능

# 숫자 카드 게임
# min(), max() 함수 알면 쉬움

# n : 행, m : 열
# 선택 행의 가장 작은 수 가 가장 큰 수

n,m = map(int,input().split())

result = 0

for i in range(n):
  data = list(map(int,input().split()))
  min_value = min(data)
  result = max(min_value,result)

print(result)

# 1이 될때 까지