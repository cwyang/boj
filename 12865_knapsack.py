# https://www.acmicpc.net/problem/12865
# 2020-11-1 Chul-Woong Yang
# 0-1 knapsack

import sys
#from typing import List, NamedTuple
from collections import namedtuple

def mi():
    return map(int, sys.stdin.readline().split())
def milines():
    return map(int, sys.stdin.readlines())

class Item(NamedTuple):
    weight: int
    value: int

def knapsack(l: List[Item], capacity:int) -> int:
    """l = (weight, value), Sum(weight) <= capacity, maximize total value"""
    dp = [[-1 for _ in range(capacity + 1)]
          for _ in range(len(l))]

    def calc(id: int, rem_capacity: int) -> int:
        if id == len(l) or rem_capacity <= 0:
            return 0
        if dp[id][rem_capacity] >= 0:
            return dp[id][rem_capacity]
        if l[id].weight > rem_capacity:
            v = calc(id + 1, rem_capacity)
        else:
            v = max(calc(id + 1, rem_capacity - l[id].weight) + l[id].value,
                    calc(id + 1, rem_capacity))
        dp[id][rem_capacity] = v
        return v
    return calc(0, capacity)

def main() -> None:
    n, k = mi()
    l = [Item(*mi()) for _ in range(n)]
    print(knapsack(l, k))

def test_knapsack() -> None:
    assert knapsack(list(map(lambda x: Item(*x),
                             [(6, 13), (4, 8), (3, 6), (5, 12)])), 7) == 14

if __name__ == '__main__':
    main()

INPUT = '''
4 7
6 13
4 8
3 6
5 12
'''

OUTPUT = '''
14
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

