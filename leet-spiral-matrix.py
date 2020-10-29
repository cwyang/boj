# https://leetcode.com/problems/spiral-matrix/
# 2020-10-30. Chul-Woong Yang
# enum을 어떻게 사용하나고민하다  결국 클래스 밖에 빼 버렸다.

from typing import List
TOP = 1
RIGHT = 2
BOTTOM = 3
LEFT = 0
class Solution:
    process = {
        TOP: lambda matrix: matrix.pop(0),
        BOTTOM: lambda matrix: reversed(matrix.pop()),
        RIGHT: lambda matrix: (i.pop() for i in matrix),
        LEFT: lambda matrix: reversed([i.pop(0) for i in matrix]),
        }
    @staticmethod
    def nextdir(dir: int) -> int:
        return (dir + 1) % 4

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dir = TOP
        r = []
        while matrix and matrix[0]:
            rr = Solution.process[dir](matrix)
            r.extend(rr)
            dir = Solution.nextdir(dir)
        return r
    
def test_solve():
    s = Solution()
    assert s.spiralOrder([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]]) == [1, 2, 3,
                                          6, 9, 8,
                                          7, 4, 5]
    assert s.spiralOrder([[1]]) == [1]
    assert s.spiralOrder([[1],[2]]) == [1, 2]
    assert s.spiralOrder([[1],[2],[3]]) == [1, 2, 3]
    assert s.spiralOrder([[1,2,3,4],
                          [5,6,7,8],
                          [9,10,11,12],
                          [13,14,15,16]]) == [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
