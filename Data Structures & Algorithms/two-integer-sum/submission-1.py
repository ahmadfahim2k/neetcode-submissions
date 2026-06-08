class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, el in enumerate(nums):
            if target - el in hm:
                # found pair
                return [hm[target-el], i]
            else:
                hm[el] = i