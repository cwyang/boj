# https://www.acmicpc.net/problem/2565
# 2020-10-31 Chul-Woong Yang
# LIS

import sys
from typing import List

def mi():
    return map(int, sys.stdin.readline().split())
def milines():
    return map(int, sys.stdin.readlines())

def lis(l: List[int]) -> int:
    ll = len(l)
    dp = [1] * ll
    for i in range(1, ll):
        dp[i] = 1 + max((0, *(dp[j] for j in range(0, i) if l[j] < l[i])))
    return max(dp)

def main() -> None:
    n, = mi()
    l = []
    for _ in range(n):
        l.append(tuple(mi()))
    print(len(l) - lis(list(map(lambda x: x[1], sorted(l)))))

def test_lis() -> None:
    assert lis([-7, 10, 9, 2, 3, 8, 8, 1]) == 4

if __name__ == '__main__':
    main()

INPUT = '''
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6
'''

OUTPUT = '''
3
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

