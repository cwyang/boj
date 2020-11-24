# https://www.acmicpc.net/problem/13549
# 2020-11-24 Chul-Woong Yang
# sssp single source shortest path with 0-1BFS
import sys
from collections import deque

def mi():
    return map(int, sys.stdin.readline().split())
    
def main() -> None:
    MAX=100_000
    n, k = mi() # 0 <= n, k <= 100_000
    q = deque()
    d = [MAX+1] * (MAX+1)
    d[n] = 0
    q.append(n)
    while len(q):
#        print(q)
        item = q.popleft()
        if item == k:
            print(d[item])
            return
        for i in [item-1, item+1]:
            if i < 0 or i > MAX:
                continue
            if d[item] + 1 < d[i]:
                d[i] = d[item] + 1
                q.append(i)
        if item*2 < 0 or item*2 > MAX:
            continue
        if d[item] < d[item*2]:
            d[item*2] = d[item]
            q.appendleft(item*2)
    print(-1)
        

def test_solve() -> None:
    pass

if __name__ == '__main__':
    main()
INPUT = '''
5 17
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

