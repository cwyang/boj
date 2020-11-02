# https://www.acmicpc.net/problem/7579
# 2020-11-2 Chul-Woong Yang
# 0-1 knapsack with large weight
#
# DP[i][w] = max v  --> DP[i][v] = min w

import sys
from typing import List, NamedTuple, Tuple
from collections import namedtuple

def mi():
    return (map(int, sys.stdin.readline().split()))
def milines():
    return map(int, sys.stdin.readlines())

class Item(NamedTuple):
    weight: int
    value: int

def knapsack_largeweight(l: List[Item], capacity:int) -> int:
    """l = (weight, value), Sum(weight) >= capacity, minimize total value."""
    # dp represents the minimum weight to get a value of at least v
    value_sum = sum(x.value for x in l)
    dp = [[-1] * (value_sum + 1) for _ in range(len(l))]
        
    def calc(idx: int, value: int) -> int:
        if value <= 0:
            return 0
        if idx == len(l):
            return sys.maxsize
        if dp[idx][value] >= 0:
            return dp[idx][value]
        w = min(calc(idx + 1, value - l[idx].value) + l[idx].weight,
                calc(idx + 1, value))
        dp[idx][value] = w
        return w
    for v in range(value_sum +1):
        val = calc(0, v)
        if val != sys.maxsize and val >= capacity:
            return v
    raise Exception('Oops')

def main() -> None:
    n, k = mi()
    memory = list(mi())
    cost = list(mi())
    l = [Item(*x) for x in zip(memory, cost)]
    zero_value_sum = sum(x.weight for x in l if x.value == 0)
    ll = [x for x in l if x.value != 0]
    print(knapsack_largeweight(ll, k - zero_value_sum))

def test_knapsack() -> None:
    assert knapsack_largeweight(list(map(lambda x: Item(*x),
                                         [(10, 1), (5, 2)])), 0) == 0
    assert knapsack_largeweight(list(map(lambda x: Item(*x),
                                         [(1, 1)])), 0) == 0

if __name__ == '__main__':
    main()

INPUT = '''
5 60
30 10 20 35 40
3 0 3 5 4
'''

OUTPUT = '''
6
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

