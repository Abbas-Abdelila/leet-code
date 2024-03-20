# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # find (a-1)th node
        pre_ath_node = list1
        head = list1
        for _ in range(a-1):
            pre_ath_node = pre_ath_node.next
        
        
        
        # find bth node
        after_bth_node = pre_ath_node.next
        for _ in range(b-a+1):
            after_bth_node = after_bth_node.next
            
        #find end of list2
        list2_end_node = list2
        while list2_end_node.next:
            list2_end_node = list2_end_node.next
        
        pre_ath_node.next = list2
        list2_end_node.next = after_bth_node
        return list1