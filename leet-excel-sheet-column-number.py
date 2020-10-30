# https://leetcode.com/problems/excel-sheet-column-number
# 2020-10-30. Chul-Woong Yang

import functools
class Solution:
    def titleToNumber(self, s: str) -> int:
        return functools.reduce(lambda acc, x: acc*26 + ord(x) - 64, s, 0)
    
def test_solve():
    s = Solution()
    assert s.titleToNumber('A') == 1
    assert s.titleToNumber('AB') == 28
    assert s.titleToNumber('ZY') == 701
