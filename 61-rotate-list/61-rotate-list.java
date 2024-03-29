/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    
    public int getLength(ListNode head) {
        int len = 0;
        while(head!=null) {
            len++;
            head = head.next;
        }
        
        return len;
    }
    
    
    public ListNode rotateRight(ListNode head, int k) {
         if(head == null)   return head;
        
        // calculate length and update k
        int len = getLength(head);
        k = k % len;
        
        // get the required nodes
        ListNode fast = head, slow = head;
        while(k != 0) {
            fast = fast.next;
            k--;
        }
        while(fast.next != null) {
            slow = slow.next;
            fast = fast.next;
        }
        
        // form the new links
        fast.next = head;
        head = slow.next;
        slow.next = null;
        
        return head;
      
    }
}