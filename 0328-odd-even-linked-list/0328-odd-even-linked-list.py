# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        odd_head = ListNode(10**20)
        even_head = ListNode(10**20)
        curr = head
        i = 1
        while curr:
            if (i%2==1):
                if odd_head.val == 10**20:
                    new_odd_head = ListNode(curr.val)
                    odd_head = new_odd_head
                    tail_odd = new_odd_head

                else:
                    new_node = ListNode(curr.val)
                    tail_odd.next = new_node
                    tail_odd = tail_odd.next
            else:
                if even_head.val == 10**20:
                    new_even_head = ListNode(curr.val)
                    even_head = new_even_head
                    tail_even = new_even_head
                else:
                    new_node = ListNode(curr.val)
                    tail_even.next = new_node
                    tail_even = tail_even.next
            
            i += 1
            curr = curr.next
        
        tail_odd.next = even_head
        return odd_head
        
        