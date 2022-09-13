# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        
        
        
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
            
        if n == length:
            return head.next
        
        current = head
        k = length-n
        i=1
        while i<k:
            current = current.next
            i += 1
        
        if current.next:
            current.next = current.next.next
        else:
            current.next = None
        
        return head
            
        