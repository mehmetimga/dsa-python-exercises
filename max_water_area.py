from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
    
# Example usage:
solution = Solution()
heights1 = [1,8,6,2,5,4,8,3,7]
print(solution.maxArea(heights1))  # Output: 49
heights2 = [1,1]
print(solution.maxArea(heights2))  # Output: 1