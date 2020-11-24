# https://www.acmicpc.net/problem/10250
# Nov 22 2020 Chul-Woong Yang

import sys
def mi():
    return map(int, sys.stdin.readline().split())

def main() -> None:
    for _ in range(int(input())):
        h,w,n = mi()
        print(f'{(n-1)%h+1}{(n-1)//h+1:02d}')
            
if __name__ == "__main__":
    main()

def test_solve() -> None:
    pass


INPUT = '''
2
6 12 10
30 50 72
'''

OUTPUT = '''
402
1203
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


