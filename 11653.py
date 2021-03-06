# https://www.acmicpc.net/problem/11653
# 2020-11-20 Chul-Woong Yang
import sys
def solve(n):
    s = 0
    for i in range(2, n+1):
        if i < 5:
            continue
        while i % 5 == 0:
            s += 1
            i //= 5
        print(s)
    return s
def main():    
    n=int(input())
    print(solve(n))

if __name__ == '__main__':
    main()
INPUT = '''
6
'''

OUTPUT = '''
2
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
