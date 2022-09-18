# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first = p1 = ListNode()
        second = p2 = ListNode()
        
        current = head
        while current:
            if current.val < x:
                p1.next = current
                p1 = p1.next
            else:
                p2.next = current
                p2 = p2.next
            
            current = current.next
        
        p2.next = None
        p1.next = second.next
        
        return first.next
        
        