class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        running_sum =0
        prefix_count = {0:1}

        for num in nums:
            running_sum += num
            needed_sum = running_sum - k
            if needed_sum in prefix_count:
                count+= prefix_count[needed_sum]
            prefix_count[running_sum] = prefix_count.get(running_sum,0) +1

        return count