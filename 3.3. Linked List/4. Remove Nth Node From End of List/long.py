# Runtime 0ms
# Beats 100.00%

# Memory 17.16MB
# Beats 14.63%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, second = head, head
        for i in range(n):
            first = first.next

        # The second will be the n-th element before the first
        while first is not None and first.next is not None:
            first = first.next
            second = second.next

        # Remove the first element because the second did not move
        if first is None:
            head = second.next
        else:
            temp = second
            second = second.next
            temp.next = second.next

        return head