class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd_head = head
        even_head = head.next
        odd_tail = odd_head
        even_tail = even_head

        while even_tail and even_tail.next:
            # Link the tail of the odd list to the head of the even list
            odd_tail.next = even_tail.next
            # Advance the tail of the odd list
            odd_tail = odd_tail.next
            # Link the tail of the even list to the head of the odd list
            even_tail.next = odd_tail.next
            # Advance the tail of the even list
            even_tail = even_tail.next

        # Link the tail of the odd list to the head of the even list
        odd_tail.next = even_head

        # Return the head of the odd list, since it is the new head of the reordered list
        return odd_head
        