# 큐 - 선입선출 방식 
# 데크 - 양방향 큐 - 앞 뒤 양방향으로 엘리먼트 추가제거 가능

# 데크는 양 끝 엘리먼트 append() pop() 압도적으로 빠름
# List는 O(n), deque는 O(1)

from collections import deque

deq = deque()

deq.appendleft(10)
deq.append(10)
deq.popleft()
deq.pop()

# 데크는 스택처럼 사용할수도 있고, 큐처럼 사용도 가능
