# Runtime 45ms
# Beats 57.85%

# Memory 19.42MB
# Beats 20.80%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        # For empty or having only 1 node
        if slow == None or slow.next == None:
            return False

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # If there is a cycle, the fast and slow will meet
            if slow == fast:
                return True

        return False