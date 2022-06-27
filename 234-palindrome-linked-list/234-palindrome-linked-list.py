# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tail = head

        temp = []
        while tail != None:
            temp.append(tail.val)
            tail = tail.next

        right = len(temp)-1
        left = 0

        while left < right:
            # print(f'INDEX{left} {right}')
            # print(f'NUMS {temp[left]} {temp[right]}')
            if temp[left] != temp[right]:
                return False
            right -= 1
            left += 1
        return True