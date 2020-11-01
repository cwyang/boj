# https://www.acmicpc.net/problem/4195.py
# 2020-11-4 Chul-Woong Yang

class UnionFind:
    def __init__(self):
        self.rank = dict()
        self.p = dict()
        self.count = dict()
    def get_count(self, i):
        return self.count[self.find_set(i)]
    def find_set(self, i):
        if i not in self.p:
            self.p[i] = i
            self.rank[i] = 0
            self.count[i] = 1
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
                self.count[x] += self.count[y]
            else:
                self.p[x] = y
                self.count[y] += self.count[x]
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1   # break tie

import sys

def mi():
    return map(int, sys.stdin.readline().split())

def solve() -> None:
    m, = mi()
    uf = UnionFind()
    for i in range(m):
        a, b = input().split()
        uf.join(a, b)
        print(uf.get_count(a))

    
def main() -> None:
    n, = mi()
    for _ in range(n):
        solve()

def test_solve() -> None:
    pass

if __name__ == '__main__':
    main()

INPUT = '''
2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty
'''

OUTPUT = '''
2
3
4
2
2
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

def test_UnionFind():
    uf = UnionFind()
    uf.join(0, 1)
    uf.join(2, 3)
    uf.join(2, 4)
    assert uf.eq(0, 1)
    assert uf.eq(2, 4)
    assert not uf.eq(0, 2)
