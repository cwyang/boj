# https://www.acmicpc.net/problem/19941
# 2020-11-11 Chul-Woong Yang

import sys

def mi():
    return map(int, sys.stdin.readline().split())
def milines():
    return map(int, sys.stdin.readlines())

def main() -> None:
    def next_thing(idx, mark):
        idx += 1
        while idx < n:
            if l[idx] == mark:
                break
            idx += 1
        return idx
    n,k = map(int, input().split())
    l = input()
    person = next_thing(-1, 'P')
    burger = next_thing(-1, 'H')
    cnt = 0
    while person < n and burger < n:
        if burger < person:
            if person - burger <= k:
                cnt += 1
                person = next_thing(person, 'P')
            burger = next_thing(burger, 'H')
        elif person < burger:
            if person - burger >= -k:
                cnt += 1
                burger = next_thing(burger, 'H')
            ~person = next_thing(person, 'P')
    print(cnt)

if __name__ == '__main__':
    main()

INPUT = '''
4 1
PHPH
20 1
HHPHPPHHPPHPPPHPHPHP
'''

OUTPUT = '''
8
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

