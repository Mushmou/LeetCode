# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        tail = head
        length = 1
        
        while tail.next:
            length += 1
            tail = tail.next
        
        k = k % length
        if k == 0: 
            return head
        
        #Move to the pivot point
        current = head
        for num in range(length - k - 1):
            current = current.next
        
        print(current.val)
        
        newHead = current.next
        current.next = None
        tail.next = head
        
        return newHead