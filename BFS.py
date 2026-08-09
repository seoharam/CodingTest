"""
0. 개념
- BFS (Breadth-Frist Search): 그래프 탐색 (Vertex + Edge) -> 한 계층씩 다 훑고 더 깊은 계층 탐색 / 보통 최소 거리 찾을 때 많이 씀 > A* > Dijkstra
- Queue 자료형 = FIFO(First-In-First-Out): 먼저 들어간게 먼저 나오는 구조 (= 줄서기)

* list로 표현하든 numpy로 표현하든 둘 다 행렬(matrix)는 맞고, 보통 numpmy는 격자 전체에 수학 연산을 걸 때 유용해서 굳이 지금은 쓸 필요 X

1. 아이디어
- 2중 for문 => 값 1 && 방문 X => BFS
- BFS 돌면서 그램 개수 +1, 최대값을 갱신

2. 시간복잡도
- BFS : O(V+E)
- V : 500 * 500                  # m과 n 최대값 기준
- E : 4 * 500 * 500              # Edge는 Vertex 당 최대 4개 연결되어 있었음
- V+E : 5 * 250000 = 100만       # CPU는 1초 보통 2억개 연산 >> 가능  -> 이게 알고리즘 선택 타당성 기준

3. 자료구조
- 그래프 전체 지도: int[][]
- 방문 : bool[][]
- Queue(BFS)
"""

import sys
from collections import deque
input = sys.stdin.readline                                         # 입력속도 개선

n, m = map(int, input().split())                                   # 세로 n, 가로 m 크기 입력 / split은 공백을 기준으로 문자열을 자름
grid = [list(map(int, input().split())) for _ in range(n)]         # 입력된 첫 줄 이후 나머지 n줄을 읽어 n x m 격자(그림 정보) 생성
chk = [[False] * m for _ in range(n)]                              # 방문 여부를 저장할 n x m 배열, 전부 False로 초기화

dy = [0,1,0,-1]                                                    # 상하좌우 이동 중 y(행) 변화량
dx = [1,0,-1,0]                                                    # 상하좌우 이동 중 x(열) 변화량, dy와 같은 인덱스끼리 짝지어 한 방향을 표현
def bfs(y: int, x: int) -> int:                                   # (y, x)에서 시작해 연결된 덩어리의 크기를 구하는 함수
    rs = 1                                                         # 시작 칸 자신을 포함해 크기 1로 시작
    q = deque([(y, x)])                                            # 탐색 대기열에 시작 좌표 삽입 (양 끝 삽입/삭제가 O(1)인 deque 사용)
    while q:                                                       # 대기열이 빌 때까지 반복
        ey, ex = q.popleft()                                       # 맨 앞에서 꺼냄(FIFO) → 진짜 BFS 동작
        # print(f"방문: ({ey}, {ex})")    
        for k in range(4):                                         # 네 방향을 순서대로 확인 (엣지 방향)
            ny = ey + dy[k]                                        # 이동 후의 y좌표
            nx = ex + dx[k]                                        # 이동 후의 x좌표
            if 0<=ny<n and 0<=nx<m:                                # 격자 범위를 벗어나지 않는지 확인
                if grid[ny][nx] == 1 and chk[ny][nx] == False:     # 그림 칸(1)이면서 아직 방문하지 않았다면
                    rs += 1                                        # 덩어리 크기 1 증가
                    chk[ny][nx] = True                             # 방문 처리(중복 방문 방지)
                    # print(f"  대기열(=큐)에 넣음: ({ny}, {nx})")
                    q.append((ny, nx))                             # 다음에 탐색할 좌표로 대기열에 추가
    return rs                                                      # 이 덩어리에 속한 칸의 총 개수 반환

cnt = 0                                                             # 전체 그림(덩어리) 개수
maxv = 0                                                            # 가장 큰 그림의 크기
for j in range(n):                                                  # 모든 행을 순회
    for i in range(m):                                              # 모든 열을 순회
        if grid[j][i] == 1 and chk[j][i] == False:                  # 아직 방문 안 한 그림 칸을 새 덩어리의 시작점으로 발견
            chk[j][i] = True                                        # 시작점 방문 처리
            # 전체 그림 갯수를 +1
            cnt += 1                                                # 새로운 덩어리를 하나 찾았으므로 개수 증가
            # BFS > 그림 크기를 구해주고, 최대값 갱신
            maxv = max(maxv, bfs(j,i))                              # 이 덩어리의 크기를 구해 지금까지의 최댓값과 비교 갱신

print(cnt)                                                          # 전체 그림 개수 출력
print(maxv)                                                         # 가장 큰 그림의 크기 출력