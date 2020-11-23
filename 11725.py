# https://www.acmicpc.net/problem/2206
# 2020-11-24 Chul-Woong Yang
# bfs

import sys
from collections import deque

def mi():
    return map(int, sys.stdin.readline().split())
def main() -> None:
    n, = mi()
    adj = [[] for _ in range(n+1)]
    parent = [0] * (n+1)
    for _ in range(n-1):
        u, v = mi()
        adj[u].append(v)
        adj[v].append(u)
    q = deque([1])
    while len(q):
        v = q.popleft()
        for i in adj[v]:
            if parent[i] == 0:
                parent[i] = v
                q.append(i)
    for i in range(2, n+1):
        print(parent[i])
def test_solve() -> None:
    pass

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

