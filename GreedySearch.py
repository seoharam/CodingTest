"""
0. 개념
- 그리디탐색(Greedy Search): 현재 차례의 최고의 답을 찾는 문제 (=최선의 결과)
   ㄴ 하지만 이게 최선인지 증명하기가 어려워서 이 이유를 찾는 연습을 해야함 (반례를 찾으면 쉬움)

1. 아이디어
- 동전을 저장한뒤, 반대로 뒤집음
- 동전을 for문 돌면서, 동전 사용개수 추가 + 동전 사용한만큼 K값 갱신

2. 시간복잡도 (2억 = 1e+8)
- O(N)

3. 자료구조
- 동전 금액: int[]
- 동전 사용 cnt: int
- 남은 금액: int

"""

import sys
input = sys.stdin.readline                  # 입력속도 개선

N, K = map(int, input().split())            # 동전 종류 개수 N, 만들어야 할 금액 K
coins = [int(input()) for _ in range(N)]    # 동전 금액을 한 줄에 하나씩 N개 입력받음
coins.reverse()                             # 오름차순으로 주어지는 입력을 내림차순으로 뒤집음 (큰 동전부터 써야 최소 개수)
cnt = 0                                     # 사용한 동전의 총 개수

for each_coin in coins:                     # 큰 동전부터 차례대로
    cnt += K // each_coin                   # 이 동전으로 최대한 많이 채우고, 사용한 개수를 누적
    K = K % each_coin                       # 채우고 남은 금액만 다음(더 작은) 동전으로 넘김

print(cnt)                                  # 사용한 동전 개수의 최솟값 출력