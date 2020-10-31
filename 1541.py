# https://www.acmicpc.net/problem/1931
# 2020-11-1 Chul-Woong Yang

import sys
import re

def mi():
    return map(int, sys.stdin.readline().split())
def milines():
    return map(int, sys.stdin.readlines())

def solve(l: str) -> int:
    minus_state, running_sum = False, 0
    for token in re.findall(r'\d+|\+|-', l):
        if token == '-':
            minus_state = True
        elif token != '+':
            running_sum += -int(token) if minus_state else int(token)
    return running_sum


def main() -> None:
    print(solve(sys.stdin.readline().strip()))
    
def test_solve() -> None:
    pass

if __name__ == '__main__':
    main()

INPUT = '''
55-50+40
'''

OUTPUT = '''
-35
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

