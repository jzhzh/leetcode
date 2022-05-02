# self
class Solution:
    def maxArea(self, height):
        max_area = 0
        for  i in range(len(height)):
            for j in range(i+1, len(height)):
                area = min(height[i], height[j]) * (j - i)
                if area > max_area:
                    max_area = area
        
        return max_area

# height = [1,8,6,2,5,4,8,3,7]
# x = Solution()
# print(x.maxArea(height))

# Solution 1
class Solution:
    def maxArea(self, height):
        maxarea = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                width = right - left
                maxarea = max(maxarea, min(height[left], height[right]) * width)

        return maxarea

# Solution 2
class Solution:
    def maxArea(self, height):
        maxarea = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
        return maxarea