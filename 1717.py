# https://www.acmicpc.net/problem/1717
# 2020-11-4 Chul-Woong Yang

class UnionFind:
    def __init__(self, n: int):
        self.rank = [0] * n
        self.p = [i for i in range(n)]
    def find_set(self, i):
        if self.p[i] == i:
            return i
        else:
            self.p[i] = self.find_set(self.p[i])
            return self.p[i]
    def eq(self, i, j):
        return self.find_set(i) == self.find_set(j)
    def join(self, i, j):
        if not self.eq(i, j):
            x, y = self.find_set(i), self.find_set(j)
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1   # break tie

import sys

def mi():
    return map(int, sys.stdin.readline().split())
def milines():
    return map(int, sys.stdin.readlines())

def main() -> None:
    n, = mi()
    m, = mi()
    uf = UnionFind(n+1)
    for i in range(m):
        for j, v in enumerate(mi()):
            if v == 1:
                uf.join(i + 1, j + 1)
    l = list(mi())
    print(l)
    if all(uf.eq(l[i], l[i+1]) for i in range(m-1)):
        print("YES")
    else:
        print("NO")

def test_solve() -> None:
    pass

if __name__ == '__main__':
    main()

INPUT = '''
3
3
0 1 0
1 0 1
0 1 0
1 2 3
'''

OUTPUT = '''
YES
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

def test_UnionFind():
    uf = UnionFind(5)
    uf.join(0, 1)
    uf.join(2, 3)
    uf.join(2, 4)
    assert uf.eq(0, 1)
    assert uf.eq(2, 4)
    assert not uf.eq(0, 2)
