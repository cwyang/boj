# https://www.acmicpc.net/problem/1780
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
          n: int) -> Tuple[int,...]:
    elem = board[pos.x][pos.y]
    if all(board[x][y] == elem for x in range(pos.x, pos.x+n) for y in range(pos.y, pos.y+n)):
        if elem == -1:
            return (1, 0, 0)
        elif elem == 0:
            return (0, 1, 0)
        else:
            return (0, 0, 1)
    ns = n // 3
    return tuple(sum(x) for x in zip(solve(board, pos, ns),
                                     solve(board, pos.add(0, ns), ns),
                                     solve(board, pos.add(0, ns*2), ns),
                                     solve(board, pos.add(ns, 0), ns),
                                     solve(board, pos.add(ns, ns), ns),
                                     solve(board, pos.add(ns, ns*2), ns),
                                     solve(board, pos.add(ns*2, 0), ns),
                                     solve(board, pos.add(ns*2, ns), ns),
                                     solve(board, pos.add(ns*2, ns*2), ns)))
    
def main() -> None:
    n, = mi()
    board = []
    for _ in range(n):
        board.append(list(mi()))
    print(*solve(board, Pos(0, 0), n), sep='\n')

def test_solve() -> None:
    pass

if __name__ == '__main__':
    main()
INPUT = '''
9
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1
'''

OUTPUT = '''
10
12
11
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

