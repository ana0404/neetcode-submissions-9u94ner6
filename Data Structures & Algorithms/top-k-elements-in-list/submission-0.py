class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n,0)+1

        sorted_arr = sorted(count.items(),key=lambda x:x[1],reverse = True)

        res = []
        for i,cnt in sorted_arr[:k]:
            res.append(i)
        return res
        
        
        