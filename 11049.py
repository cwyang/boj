# https://www.acmicpc.net/problem/11049
# 2020-11-20 Chul-Woong Yang
# Runtime Error
import sys
def mi():
    return map(int, sys.stdin.readline().split())
def main() -> None:
    def solve(start, end):
        if start == end:
            return 0
        if dp[start][end]:
            return dp[start][end]
        dp[start][end] = min(solve(start,i) + solve(i+1,end) +
                             l[start][0]*l[i][1]*l[end][1]
                             for i in range(start, end))
        return dp[start][end]
    n, = mi()
    dp = [[0] * (n+1) for _ in range(n+1)]
    l = []
    for _ in range(n):
        l.append(tuple(map(int, input().split())))
    print(solve(0, n-1))
if __name__ == '__main__':
    main()
INPUT = '''
3
5 3
3 2
2 6
'''

OUTPUT = '''
90
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
