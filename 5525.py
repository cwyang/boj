# https://www.acmicpc.net/problem/5525
# 2020-11-22 Chul-Woong Yang

import sys
import math
from typing import List

def mi():
    return map(int, sys.stdin.readline().split())
def milines():
    return map(int, sys.stdin.readlines())

def solve(n, m, s):
    cnt, run = 0, 0
    def nextc():
        return 'I' if run % 2 == 0 else 'O'
    def update_score(r):
        sc = (r-1) // 2
        if sc >= n:
            return sc - n + 1
        else:
            return 0
    for c in s:
        if nextc() == c:
            run += 1
        else:
            cnt += update_score(run)
            if c == 'I':
                run = 1
            else:
                run = 0
    cnt += update_score(run)
    return cnt

def main() -> None:
    n, = mi()
    m, = mi()
    s = sys.stdin.readline().strip()
    print(solve(n, m, s))

def test_solve() -> None:
    pass

if __name__ == '__main__':
    main()

INPUT = '''
1
13
OOIOIOIOIIOII
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

