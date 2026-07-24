class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        n = len(nums)
        for i in nums:
            hashmap[i] = hashmap.get(i,0) +1
        for key, val in hashmap.items():
            if val > n/2:
                return key
        return -1
        