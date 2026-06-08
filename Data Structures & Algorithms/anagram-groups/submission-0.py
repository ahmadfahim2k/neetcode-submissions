class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for st in strs:
            s = "".join(sorted(st))
            if s not in hm:
                hm[s] = [st]
            else:
                hm[s].append(st)
        
        res = []
        for k, v in hm.items():
            res.append(v)
        return res