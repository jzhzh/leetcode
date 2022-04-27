# Self
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
x.twoSum(nums, target)


# Solution 1
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


# Solution 2
class Solution:
    def twoSum(self, nums, target):
        hashmap = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 

# Solution 3
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i