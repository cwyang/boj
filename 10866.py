# https://www.acmicpc.net/problem/10866
# 2020-11-22 Chul-Woong Yang

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
    'push_front': lambda q, arg: q.appendleft(int(arg)),
    'push_back': lambda q, arg: q.append(int(arg)),    
    'pop_front': lambda q: print(q.popleft() if q else -1),
    'pop_back': lambda q: print(q.pop() if q else -1),
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
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front
'''

OUTPUT = '''
2
1
2
0
2
1
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

