class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for el in nums:
            if el not in hm:
                hm[el] = 0
            hm[el] += 1
        
        rev_hm = {}

        for ke, v in hm.items():
            if v not in rev_hm:
                rev_hm[v] = []
            rev_hm[v].append(ke)
        
        srt_k = sorted(rev_hm.keys(), reverse=True)

        res = []

        for i in range(len(srt_k)):
            if(len(res) == k):
                break
            ke = srt_k[i]
            for el in rev_hm[ke]:
                res.append(el)

        return res


