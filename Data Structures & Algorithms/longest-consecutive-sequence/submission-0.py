class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        res = 0

        for el in s:
            if el-1 not in s:
                longest = 1
                nxt = el+1
                while nxt in s:
                    longest += 1
                    nxt += 1
                res = max(res, longest)
        
        return res