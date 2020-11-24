# https://www.acmicpc.net/problem/14494
# 2020-11-11 Chul-Woong Yang
# 끙끙

import sys
from typing import List

def mi():
    return map(int, sys.stdin.readline().split())
def milines():
    return map(int, sys.stdin.readlines())

def solve(n, m):
    dp = [ [1] * m for _ in range(n) ]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]) % 1_000_000_007
    return dp[n-1][m-1]

def main() -> None:
    n, m = mi()
    print(solve(n,m))

def test_solve() -> None:
    pass

if __name__ == '__main__':
    main()

INPUT = '''
3 2
'''

OUTPUT = '''
5
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

