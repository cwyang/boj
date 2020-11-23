# https://www.acmicpc.net/problem/2206
# 2020-11-24 Chul-Woong Yang
# bfs

import sys
from collections import deque

def mi():
    return map(int, sys.stdin.readline().split())
def main() -> None:
    n, m = mi()
    board = []
    for _ in range(n):
        board.append(input())
    visited = [[2]*(m+1) for _ in range(n+1)]
    q = deque([(0,0,0),(-1,-1,-1)]) # (-1,-1,-1) is mark for count increase
    visited[0][0] = 0
    cnt = 1
    dir_r = [-1,1,0,0]
    dir_c = [0,0,-1,1]
    def check(r, c, z):
        if r < 0 or r >= n or c < 0 or c >= m:
            return (False, 0)
        if visited[r][c] <= z:
            return (False, 0)            
        if board[r][c] == '0':
            return (True, z)
        elif z == 1:
            return (False, 0)
        else:
            return (True, 1)
    processed = 0
    while len(q):
#        print(q)
        r,c,z = q.popleft()
        if (r,c) == (n-1,m-1):
            print(cnt)
            return
        if r == -1 and c == -1:
            if processed == 0:
                break
            q.append((-1,-1,-1))
            cnt += 1
            processed = 0
            continue
        for i in range(4):
            canmove, destroy = check(r+dir_r[i], c+dir_c[i], z)
            if canmove:
                visited[r+dir_r[i]][c+dir_c[i]] = destroy
                q.append((r+dir_r[i], c+dir_c[i], destroy))
                processed += 1
    print(-1)

def test_solve() -> None:
    pass

if __name__ == '__main__':
    main()

INPUT = '''
6 4
0100
1110
1000
0000
0111
0000
'''

OUTPUT = '''
15
'''

# pytest
import sys                              # noqa: E402
import io                               # noqa: E402
def test_main(capsys) -> None:          # noqa: E302
    sys.stdin = io.StringIO(INPUT.strip())
    main()
    sys.stdin = sys.__stdin__
    out, err = capsys.readouterr()
    print(out)
    eprint(err)
    assert out == OUTPUT.lstrip()
def eprint(*args, **kwargs):            # noqa: E302
    print(*args, file=sys.stderr, **kwargs)

