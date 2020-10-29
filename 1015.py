# https://www.acmicpc.net/problem/1015
# 2020-10-29 Chul-Woong Yang
# operator.itemgetter를 사용해보았다.

import sys
import operator


def mi():
    return map(int, sys.stdin.readline().split())


def solve(n, lst):
    r = []
    for i, t in enumerate(sorted(zip(lst, range(n)),
                                 key=operator.itemgetter(0))):
        r.append((i, t[1]))
    r.sort(key=operator.itemgetter(1))
    return [x for x, _ in r]


def main() -> None:
    n, = mi()
    lst = mi()
    print(*solve(n, lst))


def test_solve() -> None:
    assert solve(3, [2, 3, 1]) == [1, 2, 0]
    assert solve(3, [20, 30, 10]) == [1, 2, 0]


if __name__ == '__main__':
    main()
