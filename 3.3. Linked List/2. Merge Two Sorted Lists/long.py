# Runtime 0ms
# Beats 100.00%

# Memory 16.58MB
# Beats 64.07%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        head = merged
        while list1 or list2:
            newNode = ListNode()
            # list2 is None: Completed all list2
            if list2 is None or (list1 is not None and list1.val < list2.val):
                newNode.val = list1.val
                list1 = list1.next
            else:
                newNode.val = list2.val
                list2 = list2.next
            merged.next = newNode 
            merged = merged.next      
        return head.next # Skip the first element because it is the initial value