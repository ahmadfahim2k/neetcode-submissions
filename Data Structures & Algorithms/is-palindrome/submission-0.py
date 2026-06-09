class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join(c for c in s if c.isalnum()).lower()
        l, r = 0, len(st)-1

        while l < r:
            if st[l] == st[r]:
                l += 1
                r -= 1
            else:
                return False
        return True