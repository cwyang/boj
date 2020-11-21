# 2020-11-21 Chul-Woong Yang
# find kth, timeit
# c.f. https://www.geeksforgeeks.org/timeit-python-examples/

import sys
import random

def mi():
    return map(int, sys.stdin.readline().split())
def find_kth(k, A):
    def swap(a, i, j):
        a[i], a[j] = a[j], a[i]
    def partition(left, right, pivot):
        pivot_val = A[pivot]
        new_pivot = left
        swap(A, pivot, right)
        for i in range(left, right):
            if A[i] <= pivot_val:
                swap(A, i, new_pivot)
                new_pivot += 1
        swap(A, right, new_pivot)
        return new_pivot
    left, right = 0, len(A) - 1
    while left <= right:
        pivot_idx = random.randint(left, right)
        new_pivot_idx = partition(left, right, pivot_idx)
        if new_pivot_idx == k - 1:
            return A[new_pivot_idx]
        elif new_pivot_idx > k - 1:
            right = new_pivot_idx - 1
        else:
            left = new_pivot_idx + 1
    return find_kth()
def main():
    k = int(input())
    l = list(mi())
    print(find_kth(k, l))

import timeit    

def test_solve() -> None:
    SETUP_CODE = 'from find_kth import find_kth;v=list(range(1_000_000,1,-1))+list(range(1_000_000,1,-1))'

    v = list(range(1000000))
    assert find_kth(100000, v) == 99999
    print(timeit.timeit(setup=SETUP_CODE,
                        stmt='print(find_kth(1000_000, v))',
                        number=1))
    print(timeit.timeit(setup=SETUP_CODE,
                        stmt='v.sort();print(v[1000_000])',
                        number=1))

if __name__ == '__main__':
    main()

INPUT = '''
3
9 8 1 2 3 4 7 3
'''

OUTPUT = '''
3
'''

# pytest
import sys                              # noqa: E402
import io                               # noqa: E402
def test_main(capsys) -> None:          # noqa: E302
    test_solve()
    sys.stdin = io.StringIO(INPUT.strip())
    main()
    sys.stdin = sys.__stdin__
    out, err = capsys.readouterr()
    print(out)
    eprint(err)
    assert out == OUTPUT.lstrip()
def eprint(*args, **kwargs):            # noqa: E302
    print(*args, file=sys.stderr, **kwargs)
