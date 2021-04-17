#Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
#Notice that you may not slant the container.

#Example 1:
#Input: height = [1,8,6,2,5,4,8,3,7]
#Output: 49
#Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

#Example 2:
#Input: height = [1,1]
#Output: 1

#Example 3:
#Input: height = [4,3,2,1,4]
#Output: 16

#Example 4:
#Input: height = [1,2,1]
#Output: 2

#Constraints:
#n == height.length
#2 <= n <= 105
#0 <= height[i] <= 104

#PYTHON
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        if len(height) <= 1:
            return max_area
        left = 0 
        right = len(height) - 1
        while (left < right):
            length = min(height[left],height[right])
            width = right-left
            area = length * width
            if area > max_area: 
                max_area = area
            if height[left] > height[right]:
                right -= 1
            else: 
                left += 1
        return max_area
