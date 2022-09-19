# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        def getLength(node):
            size = 0
            while node:
                if node == None:
                    return 
                node = node.next 
                size += 1
                
            return size
        
        lengthA = getLength(headA)
        lengthB = getLength(headB)
        if lengthA != lengthB:
            shorter = headA if lengthA < lengthB else headB
            longer = headA if lengthA > lengthB else headB
            diff = lengthA - lengthB if lengthA > lengthB else lengthB - lengthA
        else:
            shorter = headA
            longer = headB
            diff = 0
        for _ in range(diff):
            longer = longer.next
        
        while shorter is not longer:
            shorter = shorter.next
            longer = longer.next
        
        return longer
        