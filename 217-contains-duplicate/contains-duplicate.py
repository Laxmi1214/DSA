class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        Abhi_set = set()
        for num in nums:
            if num in Abhi_set:
                return True
            Abhi_set.add(num)
        
        return False