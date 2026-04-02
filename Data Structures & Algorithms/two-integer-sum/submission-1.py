class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # result = []

        # for i in range(len(nums)):
        #     # print("nums[i]",nums[i])
        #     for j in range(i+1,len(nums)):
        #         # print("nums[j]",nums[j])
        #         diff = target - nums[j]
        #         # print("diff",diff)
        #     if (nums[i] == diff):
        #         result.append(i)   
        #         result.append(j)
        #         # print("result",result)
        # return result

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (target-nums[i] == nums[j]):
                    return [i,j]


        