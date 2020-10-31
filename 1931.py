# https://www.acmicpc.net/problem/1931
# 2020-11-1 Chul-Woong Yang
# 끝난 회의보다 이전에 시작한 회의는 버린다

import sys
from typing import List, Tuple

def mi():
    return map(int, sys.stdin.readline().split())
def milines():
    return map(int, sys.stdin.readlines())

def solve(l: List[Tuple[int,int]]) -> int:
    cnt, start_limit = 0, 0
    for time_start, time_end in sorted(l, key=lambda x: (x[1], x[0])):
        if time_start >= start_limit:
            cnt += 1
            start_limit = time_end
    return cnt


def main() -> None:
    input()
    l = [tuple(map(int, x.split())) for x in sys.stdin.readlines()]
    print(solve(l))
    
def test_solve() -> None:
    pass

if __name__ == '__main__':
    main()

INPUT = '''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''

OUTPUT = '''
4
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

