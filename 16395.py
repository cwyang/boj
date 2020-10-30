# https://www.acmicpc.net/problem/16395
# 2020-10-30 Chul-Woong Yang

import sys
import itertools
from typing import List

def mi():
    return map(int, sys.stdin.readline().split())


def solve(n: int) -> List[int]:
    r = [1]
    for _ in range(1, n):
        r = list(map(lambda x: x[0]+x[1],
                     itertools.zip_longest(r, [0]+r, fillvalue=0)))
    return r


def main() -> None:
    n, k = mi()
    print(solve(n)[k - 1])


def test_solve() -> None:
    assert solve(1) == [1]
    assert solve(2) == [1, 1]
    assert solve(3) == [1, 2, 1]
    assert solve(6) == [1, 5, 10, 10, 5, 1]


if __name__ == '__main__':
    main()
