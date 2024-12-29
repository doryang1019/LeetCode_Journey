# Runtime 34ms
# Beats 83.69%

# Memory 18.78MB
# Beats 6.92%

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Create new nodes mixed with the original nodes
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        # Set the random pointers for the new nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Separate the new list from the original list
        old_current = head
        new_head = head.next
        new_current = new_head

        while old_current:
            old_current.next = old_current.next.next
            if new_current.next:
                new_current.next = new_current.next.next
            old_current = old_current.next
            new_current = new_current.next

        return new_head