class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashh = {}
        maxx = 0
        majority = 0

        for i in nums:

            hashh[i] = hashh.get(i, 0) + 1

            if (maxx < hashh[i]):
                maxx = hashh[i]
                majority = i

        return majority

