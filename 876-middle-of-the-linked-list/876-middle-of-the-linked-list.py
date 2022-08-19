# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        length = 0
        fast = head
        
        while fast:
            length +=1
            fast = fast.next
        print(length)
        
        i = 0
        slow = head
        while i < length//2:
            slow = slow.next
            i += 1
        return slow