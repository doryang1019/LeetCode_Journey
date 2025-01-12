# Runtime 3ms
# Beats 71.64%

# Memory 17.51MB
# Beats 8.10%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        buffer = 0
        head = ListNode()
        current = head
        while l1 is not None or l2 is not None:
            first, second = 0, 0
            if l1 is not None:
                first = l1.val
                l1 = l1.next
            if l2 is not None:
                second = l2.val
                l2 = l2.next
            
            total = first + second + buffer
            if total > 9:
                total -= 10
                buffer = 1
            else:
                buffer = 0

            node = ListNode(total)
            current.next = node
            current = current.next

        if buffer == 1:
            node = ListNode(buffer)
            current.next = node

        return head.next