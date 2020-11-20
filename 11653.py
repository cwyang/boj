# https://www.acmicpc.net/problem/11653
# 2020-11-20 Chul-Woong Yang
import sys
def factor(n,s):
    if n == 1:
        return
    for i in range(s,int(n**0.5)+1):
        if n % i == 0:
            print(i)
            factor(n // i, i)
            return
    print(n)
    return
def main():    
    n=int(input())
    factor(n,2)

if __name__ == '__main__':
    main()
INPUT = '''
17
'''

OUTPUT = '''
2
2
2
3
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
