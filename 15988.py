# https://www.acmicpc.net/problem/15988
# 2020-11-11 Chul-Woong Yang
import sys
from typing import Tuple, List, NamedTuple

def mi():
    return map(int, sys.stdin.readline().split())

def solve(n):
    a,b,c = 1,0,0
    for i in range(n):
        a,b,c = a+b+c,a,b
    return a
    
def main() -> None:
    n, = mi()
    board = []
    for _ in range(n):
        print(solve(int(input())))

def test_solve() -> None:
    pass

if __name__ == '__main__':
    main()
INPUT = '''
3
4
7
10
'''

OUTPUT = '''
7
44
274
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

