class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        t = 0

        hs = set()

        for i, el in enumerate(nums):
            if target - el in hs:
                # found pair
                res.append(i)
                t = target - el
                break
            else:
                hs.add(el)
        
        for i, el in enumerate(nums):
            if el == t:
                res.append(i)
                break
        
        return res[::-1]