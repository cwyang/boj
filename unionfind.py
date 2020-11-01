# UnionFind
# 2020-11-3 Chul-Woong Yang

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

def test_UnionFind():
    uf = UnionFind(5)
    uf.join(0, 1)
    uf.join(2, 3)
    uf.join(2, 4)
    assert uf.eq(0, 1)
    assert uf.eq(2, 4)
    assert not uf.eq(0, 2)
    
