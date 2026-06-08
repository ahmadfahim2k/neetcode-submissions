class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        for char in s:
            if char not in hm:
                hm[char] = 0
            hm[char] += 1
        
        for char in t:
            if char not in hm:
                return False
            hm[char] -= 1
        
        for k, v in hm.items():
            if v != 0:
                return False

        return True
            