# https://www.acmicpc.net/problem/2407
# 2020-11-23 Chul-Woong Yang

import sys

def mi():
    return map(int, sys.stdin.readline().split())

        
def main() -> None:
    n, m = mi()
    dp = [[0]*(m+1) for _ in range(n+1)]
    def choose(n, m):
        if m == 0 or m == n:
            return 1
        else:
            if dp[n][m]:
                return dp[n][m]
            dp[n][m] = choose(n-1,m) + choose(n-1,m-1)
            return dp[n][m]
    print(choose(n,m))
    

if __name__ == '__main__':
    main()

INPUT = '''
100 6
'''

OUTPUT = '''
1192052400
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

