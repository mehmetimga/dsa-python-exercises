# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                return True
        return False

# Example usage:
# Creating a linked list with a cycle for testing
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creates a cycle here
solution = Solution()
print(solution.hasCycle(node1))  # Output: True
# Creating a linked list without a cycle for testing
nodeA = ListNode(1)
nodeB = ListNode(2)
nodeA.next = nodeB
solution = Solution()
print(solution.hasCycle(nodeA))  # Output: False
