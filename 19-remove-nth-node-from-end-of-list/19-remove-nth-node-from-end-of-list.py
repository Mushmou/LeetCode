# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        
        p1 = dummy
        length = 0
        while p1 != None:
            print(p1.val)
            length += 1
            p1 = p1.next
        
        p1 = dummy
        if n > length:
            return dummy.next
        else:
            for i in range(1, length-n):
                p1 = p1.next
            p1.next = p1.next.next
            return dummy.next