# https://www.acmicpc.net/problem/1874
# 2020-10-31 Chul-Woong Yang
# 끙끙

import sys
from typing import List

def mi():
    return map(int, sys.stdin.readline().split())
def milines():
    return map(int, sys.stdin.readlines())

def solve(l: List[int], n: int) -> List[str]:
    def push(stack, n, ops):
        stack.append(n)
        ops.append('+')
    def pop(stack, ops):
        ops.append('-')
        n = stack.pop()
        return n
        
    stack: List[int] = []
    ops: List[str] = []
    it = iter(range(1, n+1))
    for elem in l:
        while not stack or stack[-1] < elem:
            try:
                i = next(it)
            except StopIteration:
                return ['NO']
            push(stack, i, ops)
        if stack[-1] == elem:
            pop(stack, ops)
        else:
            return ['NO']
    return ops

def main() -> None:
    n, = mi()
    l = milines()
    print('\n'.join(solve(l, n)))

def test_solve() -> None:
    pass

if __name__ == '__main__':
    main()

INPUT = '''
8
4
3
6
8
7
5
2
1
'''

OUTPUT = '''
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-
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

