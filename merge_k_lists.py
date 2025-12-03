from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        
        min_heap = []
        counter = 0
        
        # Initialize the heap with the head of each list
        for l in lists:
            if l:
                heapq.heappush(min_heap, (l.val, counter, l))
                counter += 1
                
        dummy = ListNode(0)
        current = dummy
        
        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next
            
            if node.next:
                heapq.heappush(min_heap, (node.next.val, counter, node.next))
                counter += 1
            
        return dummy.next
    
# Example usage:
solution = Solution()
# Creating linked lists for testing
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))
merged_list = solution.mergeKLists([list1, list2, list3])
# Print merged linked list
current = merged_list
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> None

                               
        