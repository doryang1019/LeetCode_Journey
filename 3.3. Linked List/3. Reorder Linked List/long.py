# Runtime 0ms
# Beats 100.00%

# Memory 22.40MB
# Beats 81.13%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, quick = head, head.next

        # Reach the slow to middle of the linked list
        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next

        # Separate into two Linked Lists by dividing in half
        second = slow.next
        first = head
        slow.next = None

        # Reverse the second Linked List
        previousNode = None
        while second:
            nextNode = second.next
            second.next = previousNode
            previousNode = second
            second = nextNode
        second = previousNode # Head of the second node

        # Merge two Linked List together
        while second:
            tempFirst = first.next
            tempSecond = second.next

            first.next = second
            second.next = tempFirst

            first = tempFirst
            second = tempSecond

