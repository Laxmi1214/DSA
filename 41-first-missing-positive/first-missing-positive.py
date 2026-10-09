class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        
        sett = set(nums)
        n = len(nums)

        for i in range (0, n + 1):
            if i+1 not in sett:
                return i+1
        
        return n + 1