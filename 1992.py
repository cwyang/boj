# https://www.acmicpc.net/problem/1992
# 2020-11-10 Chul-Woong Yang
import sys
from typing import Tuple, List, NamedTuple

def mi():
    return map(int, sys.stdin.readline().split())

class Pos(NamedTuple):
    x: int
    y: int
    def add(self, x, y) -> "Pos":
        return Pos(self.x + x, self.y + y)

def solve(board: List[List[int]],
          pos: Pos,
          n: int) -> str:
    s = sum(sum(board[x][y] for x in range(pos[0], pos[0]+n)) for y in range(pos[1], pos[1]+n))
    if s == 0:
        return "0"
    elif s == n*n:
        return "1"
    else:
        ns = n >> 1
        return ("(" +
                solve(board, pos, ns) +
                solve(board, pos.add(0, ns), ns) +
                solve(board, pos.add(ns, 0), ns) +
                solve(board, pos.add(ns, ns), ns) +
                ")")
    
def main() -> None:
    n, = mi()
    board = []
    for _ in range(n):
        board.append(list(map(int, list(input()))))
    print(solve(board, Pos(0,0), n))

def test_solve() -> None:
    pass

if __name__ == '__main__':
    main()
INPUT = '''
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011
'''

OUTPUT = '''
((110(0101))(0010)1(0001))
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

