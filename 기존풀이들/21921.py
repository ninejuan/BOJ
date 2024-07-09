"""
출력
Line 1: X일 동안 가장 많이 들어온 방문자 수
Line 2: 
"""

data = input().split()
N, X = int(data[0]), int(data[1])
# N : 블로그 시작 일수
input_num_visitor = input().split()

dn_vis = [] # daily number visitors
for i in range(0, N):
    dn_vis.append(int(input_num_visitor[i]))

if len(list(dn_vis)) == 1 and dn_vis[0] == 0: # list에서는 중복 값이 삭제되는 원리를 이용
    print("SAD")


