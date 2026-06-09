class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1 for _ in nums]
        suff = [1 for _ in nums]

        #prefix
        prod = 1
        for i in range(1, len(nums)):
            pre[i] = nums[i-1] * prod
            prod = pre[i]

        #suffix
        prod = 1
        for i in range(len(nums)-2, -1, -1):
            suff[i] = nums[i+1] * prod
            prod = suff[i]

        res = [p*s for p,s in zip(pre, suff)]

        return res