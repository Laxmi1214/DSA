class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        hashmapp = {}
        reach = len(nums) // 2

        for i in nums:
            hashmapp[i] = hashmapp.get(i, 0) + 1
            if hashmapp[i] > reach :
                return i
        return -1