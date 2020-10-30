# https://www.acmicpc.net/problem/18158
# 2020-10-31 Chul-Woong Yang
# func[cmd](queue, *arg)에서 star operator의 type에 대해 모르고 쓰고있다.

import sys
from typing import Deque, Dict, Callable, Union
import collections

def mi():
    return map(int, sys.stdin.readline().split())
def milines():
    return map(int, sys.stdin.readlines())


Callback = Union[Callable[[Deque[int]], None],
                 Callable[[Deque[int], str], None]]
func: Dict[str, Callback] = {
    'push': lambda q, arg: q.append(int(arg)),
    'pop': lambda q: print(q.popleft() if q else -1),
    'size': lambda q: print(len(q)),
    'empty': lambda q: print(int(not q)),
    'front': lambda q: print(q[0] if q else -1),
    'back': lambda q: print(q[-1] if q else -1),
}

def solve(queue: Deque[int], cmd: str, *arg: str) -> None:
    func[cmd](queue, *arg)

def main() -> None:
    n, = mi()
    queue: Deque[int] = collections.deque()
    for _ in range(n):
        cmd, *arg = sys.stdin.readline().split()
        solve(queue, cmd, *arg)

def test_solve() -> None:
    pass

if __name__ == '__main__':
    main()

INPUT = '''
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
'''

OUTPUT = '''
1
2
2
0
1
2
-1
0
1
-1
0
3
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

