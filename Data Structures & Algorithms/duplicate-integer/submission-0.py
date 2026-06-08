class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vis = set()
        for el in nums:
            if el in vis:
                return True
            vis.add(el)
        return False