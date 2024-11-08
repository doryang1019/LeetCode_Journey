# Runtime 0ms
# Beats 100.00%

# Memory 17.50MB
# Beats 92.33%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # previousNode: Keeps track of the node that comes before the currentNode
        # currentNode: Being processed
        # nextNode: Keep track of where to move currentNode in the next iteration
        previousNode, currentNode, nextNode = None, head, None
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = previousNode

            previousNode = currentNode
            currentNode = nextNode
        return previousNode