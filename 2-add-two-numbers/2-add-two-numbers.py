# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_1 = 0
        num_2 = 0

        pow = 1
        while l1:
            # print(f'node val {l1.val}')
            num_1 += l1.val * pow
            pow *= 10
            l1 = l1.next

        pow = 1
        while l2:
            num_2 += l2.val * pow
            pow *= 10
            l2 = l2.next

        dummy = ListNode(None)
        tail = dummy
        outputInt = str( num_1 + num_2)

        for char in range(len(outputInt)-1, -1, -1):
            tail.next = ListNode( int( outputInt[char]) ) 
            tail = tail.next
        return dummy.next    