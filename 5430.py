# https://www.acmicpc.net/problem/5430
# 2020-11-22 Chul-Woong Yang

import sys
from collections import deque

def mi():
    return map(int, sys.stdin.readline().split())

def solve(p, n, ll):
    l = deque(ll)
    left = True
    for c in p:
        if c == 'R':
            left = not left
        else:
            if not l:
                print('error')
                return
            if left:
                l.popleft()
            else:
                l.pop()
    if not left:
        l.reverse()
    sys.stdout.write(f'[{",".join(map(str,l))}]\n')
def main() -> None:
    for _ in range(int(input())):
        p = sys.stdin.readline().strip()
        n = int(sys.stdin.readline())
        ll = sys.stdin.readline().strip()
        if len(ll) > 2:
            l = list(map(int, ll[1:-1].split(',')))
        else:
            l = []
        solve(p, n, l)

def test_solve() -> None:
    pass

if __name__ == '__main__':
    main()

INPUT = '''
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
'''

OUTPUT = '''
[2,1]
error
[1,2,3,5,8]
error
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

