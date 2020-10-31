# https://www.acmicpc.net/problem/16586
# 2020-10-31 Chul-Woong Yang
# 백만년만의 링크드리스트라 어려웠다.

from typing import List, Tuple, Any
import sys

def mi():
    return map(int, sys.stdin.readline().split())

class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.prev = None
        self.next = next_node
    def remove(self) -> None:
        assert self.prev
        self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
    def insert(self, node: 'ListNode') -> None:
        # insert node after self
        node.prev = self
        node.next = self.next
        if self.next:
            self.next.prev = node
        self.next = node
    def find(self, data, head) -> Tuple['ListNode', int, bool]:
        node, cnt = (self, 0)
        wrapped = False
        while node.data != data:
            node = node.next
            if not node:
                wrapped = True
                node = head
            cnt += 1
        return (node, cnt, wrapped)
    def to_list(self) -> List[Any]:
        head = self
        r = []
        while head:
            r.append(head.data)
            head = head.next
        return r

def solve(dummy_head: ListNode, a: ListNode, b: int, n: int) -> int:
    # move a to the immediate right of Node(b) and returns moved distance
    target, cnt, wrapped = a.find(b, dummy_head.next)
    a.remove()
    target.insert(a)
    return cnt - n + 1 if wrapped else cnt


def main() -> None:
    n, q = mi()

    index: List[Any] = [None] * (n + 1)
    tail = None
    for i in range(n):
        tail = ListNode(n - i, tail)
        index[n - i] = tail
    dummy_head = ListNode(0, tail)
    for i in range(2, n + 1):
        index[i].prev = index[i-1]
    index[1].prev = dummy_head
    for _ in range(q):
        a, b = mi()
        print(solve(dummy_head, index[a], b, n))

    print(' '.join(map(str, dummy_head.next.to_list())))


if __name__ == '__main__':
    main()

def test_solve() -> None:
    tail = None
    for i in range(3):
        tail = ListNode(3 - i, tail)
    dummy_head = ListNode(0, tail)
    assert dummy_head.next.to_list() == [1 ,2, 3]

INPUT = '''
10 2
2 7
10 7
'''

OUTPUT = '''
5
-3
1 3 4 5 6 7 10 2 8 9
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

