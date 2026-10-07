class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        prefix = 1
        suffix = 1
        res = [0] * n
        for i in range (n):
            res[i] = prefix
            prefix *= nums[i]
        
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
