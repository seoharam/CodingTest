"""
0. 개념
- DFS (Depth-First Search): 그래프 탐색 (Vertex + Edge) -> 한 계층씩 끝까지 훑고 다른 분기로 넘어감
- Stack 자료형 = LIFO(Last-In-First-Out): 먼저 들어간게 나중에 나오는 구조
- 재귀 함수 (Recursive): 자기 자신을 다시 호출하는 함수 / 회귀 분석 (Regression): 변수들 간의 관계를 함수 형태로 추정
   ㄴ 종료되는 시점이 반드시 명시, 재귀 함수의 깊이가 너무 깊어지면 Stack Overflow -> 재귀 함수 호출할 때마다 호출 정보가 call stack에 쌓이는데, 이게 계속해서 쌓이고 공간이 없어지면 Stack Overflow라고 함 (일반적으로 파이썬에서는 1000번 정도로 설정)
   ㄴ Backtracking에서도 주로 사용: 재귀로 가능한 경우를 탐색하다가 안되면 되돌아가는 기법

1. 아이디어
- 2중 for문, 값 1 && 방문 X => DFS
- DFS를 통해 찾은 값을 저장 후 정렬 해서 출력

2. 시간복잡도
- DFS: O(V+E)
- V, E: N^2, 4N^2
- V+E: 5N^2 ~= N^2 ~= 625 >> 가능 (2억보다 낮음)

3. 자료구조
- 그래프 저장: int[][]
- 방문여부: bool[][]
- 결과값: int[]
"""

import sys
input = sys.stdin.readline                                           # 시스템 도구 모음 -> 표준 입력 -> 한 줄을 읽는다 (입력속도 개선)

N = int(input())                                                     # 정사각형 격자의 한 변 크기 N 입력
map = [list(map(int, input().strip())) for _ in range(N)]            # strip을 통해 줄바꿈 문자열도 제거 후, 공백 없이 붙어있는 숫자 문자열을 한 글자씩 리스트로 쪼개 int로 변환 -> N x N 격자 생성
                                                                     # 주의: 이 줄 실행 후 'map'은 파이썬 내장 함수가 아니라 이 2차원 리스트를 가리키게 됨(이름 겹침)
chk = [[False] * N for _ in range(N)]                                # 방문 여부를 저장할 N x N 배열, 전부 False로 초기화
result = []                                                          # 각 덩어리(그림)의 크기를 담을 리스트
each = 0                                                             # 현재 탐색 중인 덩어리 하나의 크기(칸 수)를 셀 전역 변수

# 시계방향 설정
dy = [0,1,0,-1]                                                      # 상하좌우 이동 중 y(행) 변화량
dx = [1,0,-1,0]                                                      # 상하좌우 이동 중 x(열) 변화량, dy와 같은 인덱스끼리 짝지어 한 방향을 표현

def dfs(y: int, x: int) -> int:                                      # (y, x)에서 시작해 재귀로 연결된 칸을 끝까지 파고드는 함수
    global each
    # 전역 변수 사용
    each += 1                                                        # 현재 칸을 덩어리 크기에 포함(+1)
    for k in range(4):                                               # 네 방향을 순서대로 확인 (엣지 방향)
        ny = y + dy[k]                                               # 이동 후의 y좌표
        nx = x + dx[k]                                               # 이동 후의 x좌표
        if 0<=ny<N and 0<=nx<N:                                      # 격자 범위를 벗어나지 않는지 확인
            if map[ny][nx] == 1 and chk[ny][nx] == False:            # 그림 칸(1)이면서 아직 방문하지 않았다면
                chk[ny][nx] = True                                   # 방문 처리(중복 방문 방지) - 재귀 호출 전에 먼저 표시해야 같은 칸으로 무한 재귀 안 함
                # 재귀 호출
                dfs(ny, nx)                                          # 그 칸으로 이동해서 다시 깊이 파고듦 (호출 정보가 콜 스택에 쌓임 = LIFO)

for j in range(N):                                                   # 모든 행을 순회
    for i in range(N):                                               # 모든 열을 순회
        if map[j][i] == 1 and chk[j][i] == False:                    # 아직 방문 안 한 그림 칸을 새 덩어리의 시작점으로 발견
            chk[j][i] = True                                         # 시작점 방문 처리
            each = 0                                                 # 새 덩어리를 셀 것이므로 크기 카운터 초기화
            dfs(j,i)                                                 # 재귀 DFS 시작, each가 이 덩어리의 전체 크기로 누적됨
            result.append(each)                                      # 완성된 덩어리 크기를 결과 리스트에 저장

result.sort()                                                        # 덩어리 크기들을 오름차순 정렬
print(len(result))                                                   # 전체 덩어리(그림) 개수 출력
for i in result:                                                     # 정렬된 크기를 하나씩
    print(i)                                                         # 작은 것부터 순서대로 출력
