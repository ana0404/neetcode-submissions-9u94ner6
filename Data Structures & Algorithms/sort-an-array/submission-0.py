class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        left_sorted = self.sortArray(left_half)
        right_sorted = self.sortArray(right_half)

        return self.merge(left_sorted, right_sorted)

    def merge(self, left, right):          # fix 1: added self
        result = []
        i, j = 0, 0                        # fix 2: 0, 0 not 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result