from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total_power = sum(batteries)
        left, right = 1, total_power // n
        
        while left < right:
            mid = (left + right + 1) // 2
            required_power = mid * n
            available_power = sum(min(battery, mid) for battery in batteries)
            if available_power >= required_power:
                left = mid
            else:
                right = mid - 1
                
        return left
# Example usage:
solution = Solution()
print(solution.maxRunTime(2, [3, 3, 3]))  # Output: 4
print(solution.maxRunTime(3, [1, 1, 1, 1])) # Output: 1
