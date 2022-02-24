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
    public ListNode sortList(ListNode head) {
        ArrayList<Integer> numbers = new ArrayList<>();
        ListNode headHolder = head;
        while(head!=null) {
            numbers.add(head.val);
            head = head.next;
        }
        
        Collections.sort(numbers);
        head = headHolder;
        
        for(Integer n : numbers) {
            head.val = n;
            head = head.next;
        }
        
        return headHolder;
           
        
    }
}