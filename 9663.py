# https://www.acmicpc.net/problem/9663
# 2020-11-05 Chul-Woong Yang
# n-queen

import sys
from typing import List

def mi():
    return map(int, sys.stdin.readline().split())

def solve(n: int) -> int:
    def pboard() -> None:
        for i in range(n):
            if board[i] == -1:
                print('.'*n)
            print('.' * board[i] + 'Q' + '.' * (n - board[i] - 1))
        print()
    def valid(row: int, col: int) -> bool:
        return True
    def _solve(i: int) -> int:
        s = 0
        q = []
        for j in range(n):
            for r in range(0, i):
                if abs(board[r] - j) in (0, i - r):
                    break
            else:
                q.append(j)
        for j in q:
            board[i] = j
            if i + 1 == n:
                #pboard()
                s += 1
            else:
                s += _solve(i + 1)
        return s
    board = [ -1 * n for _ in range(n)]
    return _solve(0)

def main() -> None:
    n = 11 #, = mi()
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

