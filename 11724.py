# https://www.acmicpc.net/problem/11724
# 2020-11-23 Chul-Woong Yang

import sys

def input():
    return sys.stdin.readline().strip()
def main():
    def root(u):
        r = u
        while vertex[r] != r:
            r = vertex[r]
        while vertex[u] != r:
            p = vertex[u]
            vertex[u] = r
            u = p
        return r
    def join(u, v):
        ru, rv = root(u), root(v)
        vertex[rv] = ru
    n, m = map(int, input().split())
    vertex = [x for x in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        join(u, v)
    for i in range(1, n+1):
        vertex[i] = root(i)
    print(len(set(vertex[1:])))

if __name__ == '__main__':
    main()
INPUT = '''
6 5
1 2
2 5
5 1
3 4
4 6
'''

OUTPUT = '''
2
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
