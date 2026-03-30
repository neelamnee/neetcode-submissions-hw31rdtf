from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s, res = set(nums), 0
        for n in s:
            if n - 1 not in s:     # sequence start
                x = n
                while x in s:
                    x += 1
                res = max(res, x - n)
        return res
