
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next =next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev. next.next:
            first = prev.next
            second = prev.next.next
            
            # Swapping
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move prev to the next pair
            prev = first
        return dummy.next
    
# Example usage:
solution = Solution()
# Creating linked list for testing: 1 -> 2 -> 3 -> 4
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
swapped_head = solution.swapPairs(head)
# Print swapped linked list
current = swapped_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")  # Output: 2 -> 1 -> 4 -> 3
