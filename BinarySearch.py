"""
0. 개념
- 이진탐색(Binary Search): 어떤 값을 탐색할 때 정렬(분기)의 특징을 이용해 빨리 찾음 (1차원 정렬)

0-1. 핵심 코드 -> 이건 꼭 외워야 함
def search(st, en, target):
    if st==en:
        // ~~
        return
    mid = (st + en) // 2
    if nums[mid] < target:
        search(mid + 1, en, target)
    else:
        search(st, mid, target)

1. 아이디어
- N개의 숫자를 정렬
- M개를 for 돌면서, 이진 탐색을 수행
- 이진 탐색 안에서 마지막에 데이터 찾으면 1출력 아니면 0출력

2. 시간복잡도 (2억 = 1e+8)
- N개 입력값 정렬 = O(NlgN)
- M개를 N개 중에서 탐색 = O(M*lgN)
- 총합: ((N+M)lgN) > 가능

3. 자료구조
- N개 숫자: int[]
- M개 숫자: int[]
"""

import sys
input = sys.stdin.readline                                          # 입력속도 개선

N = int(input())                                                    # 원본 숫자 개수 N
nums = list(map(int, input().split()))                              # N개의 숫자를 리스트로 입력받음
M = int(input())                                                    # 찾을 대상 개수 M
target_list = list(map(int, input().split()))                       # 찾을 대상 숫자들을 리스트로 입력받음

nums.sort()                                                         # 이진탐색 가능하려면 반드시 정렬돼 있어야 함

def search(st, en, target):                                         # [st, en] 범위 안에서 target을 재귀적으로 이진탐색
    if st == en:                                                    # 범위가 한 칸으로 좁혀지면 남은 후보는 nums[st] 하나뿐
        if nums[st] == target:                                      # 그 값이 target과 같은지 최종 확인
            print(1)                                                # 찾음
        else:
            print(0)                                                # 못 찾음
        return                                                      # 재귀 종료
    mid = (st+en)//2                                                # 현재 범위의 중간 인덱스
    if nums[mid] < target:                                          # 중간값이 target보다 작으면
        search(mid+1, en, target)                                   # target은 오른쪽 절반에만 있을 수 있음 (mid는 제외)
    else:                                                           # 중간값이 target 이상이면
        search(st, mid, target)                                     # target은 왼쪽 절반에 있을 수 있음 (mid 포함)

for each_target in target_list:                                     # 찾아야 할 값마다 반복
    search(0, N-1, each_target)                                     # 전체 범위 [0, N-1]에서 이진탐색 수행