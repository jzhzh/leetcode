class Solution:
    def twoSum(self, nums, target):
        for index, i in enumerate(nums):
            for j in range(index+1, len(nums)):
                if (i + nums[j]) == target:
                    print([index, j])
                    return [index, j]


nums = [2,7,11,15]
target = 9
x = Solution()
x. twoSum(nums, target)