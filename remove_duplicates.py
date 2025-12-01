# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        write_index = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1
                
        return write_index
    
# Example usage:
solution = Solution()
nums1 = [1, 1, 2]
length1 = solution.removeDuplicates(nums1)
print(length1)  # Output: 2
print(nums1[:length1])  # Output: [1, 2]
nums2 = [0,0,1,1,1,2,2,3,3,4]
length2 = solution.removeDuplicates(nums2)
print(length2)  # Output: 5
print(nums2[:length2])  # Output: [0, 1, 2, 3, 4]
