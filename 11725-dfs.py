# https://www.acmicpc.net/problem/11725
# 2020-11-24 Chul-Woong Yang

import sys
sys.setrecursionlimit(10**9)
def input():
    return sys.stdin.readline().strip()
def main():
    def dfs(v):
        for c in adjList[v]:
            if visited[c] == 0:
                visited[c] = v
                dfs(c)
    n, = map(int, input().split())
    adjList = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for _ in range(n-1):
        u, v = map(int, input().split())
        adjList[u].append(v)
        adjList[v].append(u)
    visited[1] = 1
    dfs(1)
    for i in range(2,n+1):
        print(visited[i])

if __name__ == '__main__':
    main()
INPUT = '''
7
1 6
6 3
3 5
4 1
2 4
4 7
'''

OUTPUT = '''
4
6
1
3
1
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
