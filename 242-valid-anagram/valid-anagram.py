class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashh = {}
        for letter in s:
            if letter in hashh:
                hashh[letter] += 1
            else:
                hashh[letter] = 1
        
        for j in t:
            if j not in hashh:
                return False
            
            hashh[j] -= 1

            if hashh[j] < 0:
                return False

        return True