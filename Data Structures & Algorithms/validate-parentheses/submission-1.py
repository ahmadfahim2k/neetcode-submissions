class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        hm = {
            "}": "{",
            ")": "(",
            "]": "[",
        }

        for c in s:
            # print(stk)
            if c not in hm:
                stk.append(c)
            else:
                if len(stk) > 0 and stk[-1] == hm[c]:
                    stk.pop()
                else:
                    return False
        return len(stk) == 0