// Runtime 113ms
// Beats 11.99%

// Memory 48.81MB
// Beats 20.96%

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
 
public class Solution {
    public bool HasCycle(ListNode head) {
        HashSet<ListNode> seen = new HashSet<ListNode>();
        ListNode curr = head;

        while(curr != null) {
            if(seen.Contains(curr)) {
                return true;
            }
            seen.Add(curr);
            curr = curr.next;
        }
        return false;
    }
}