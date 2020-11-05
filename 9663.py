# https://www.acmicpc.net/problem/9663
# 2020-11-05 Chul-Woong Yang
# n-queen

import sys
from typing import List

def mi():
    return map(int, sys.stdin.readline().split())

def solve(n: int) -> int:
    def pboard() -> None:
        trans = list(zip(*board))
        for i in range(n):
            print(*list(map(lambda x: 'Q' if x else '.', trans[i])))
        print()
    def valid(i: int, j: int) -> bool:
        if any(board[k][j] for k in range(0, i)):
            return False
        for k in range(0, i):
            d = i-k
            if (j-d >= 0 and board[k][j-d] or
                j+d < n and board[k][j+d]):
                return False
        return True
    def _solve(i: int) -> int:
        if i >= n:
            #pboard()
            return 1
        def step(x, y):
            board[x][y] = True
            r = _solve(x + 1)
            board[x][y] = False
            return r
        return sum(step(i, j) for j in range(n) if valid(i, j))
    board = [[False] * n for _ in range(n)]
    return _solve(0)

def main() -> None:
    n, = mi()
    print(solve(n))

def test_solve() -> None:
    pass

if __name__ == '__main__':
    main()

INPUT = '''
8
'''

OUTPUT = '''
92
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

