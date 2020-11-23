# https://www.acmicpc.net/problem/7662
# 2020-11-23 Chul-Woong Yang
# after Security@KAIST

import sys
import heapq
from collections import Counter

def mi():
    return map(int, sys.stdin.readline().split())
def main() -> None:
    t, = mi()
    for _ in range(t):
        k, = mi()
        minheap, maxheap = [], []
        mindels, maxdels = Counter(), Counter()
        cnt = 0
        for _ in range(k):
            op, _n = input().split()
            n = int(_n)
            if op == 'I':
                cnt += 1
                heapq.heappush(minheap, n)
                heapq.heappush(maxheap, -n)
            elif cnt == 0:  # empty heap
                pass
            else:
                def delheap(heap, dels, otherdels, sign):
                    item = sign * heapq.heappop(heap)
                    while dels[item]:
                        dels[item] -= 1
                        item = sign * heapq.heappop(heap)
                    otherdels[item] += 1
                cnt -= 1
                if n == -1: # 'delete min'
                    delheap(minheap, mindels, maxdels, 1)
                else: # 'delete max'
                    delheap(maxheap, maxdels, mindels, -1)
        if cnt:
            def cleanup(heap, dels, sign):
                item = sign * heapq.heappop(heap)
                while dels[item]:
                    dels[item] -= 1
                    item = sign * heapq.heappop(heap)
                return item
            maxitem = cleanup(maxheap, maxdels, -1)
            minitem = cleanup(minheap, mindels, 1)
            print(maxitem, minitem)
        else:
            print('EMPTY')

def test_solve() -> None:
    pass

if __name__ == '__main__':
    main()
INPUT = '''
3
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
4
I 100
D -1
I 100
I 10
'''

OUTPUT = '''
EMPTY
333 -45
100 10
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

