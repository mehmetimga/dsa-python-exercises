class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        i = n - 2
        
        # Find the first decreasing element from the end
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        if i >= 0:
            j = n - 1
            # Find the element just larger than nums[i]
            while nums[j] <= nums[i]:
                j -= 1
            # Swap them
            nums[i], nums[j] = nums[j], nums[i]
            
        # Reverse the elements after index i
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
# Example usage:
solution = Solution()
nums = [1, 2, 3]
solution.nextPermutation(nums)
print(nums) # Output: [1, 3, 2]
nums = [3, 2, 1]
solution.nextPermutation(nums)
print(nums) # Outpout: [1, 2, 3]
nums = [1, 1, 5]
solution.nextPermutation(nums)
print(nums) # Output: [1, 5, 1]
        
       