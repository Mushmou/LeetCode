# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #check left or both p and q
        #Check right of both p and q
        if p == None and q == None:
            return True
        
        if (p == None or q == None) or p.val != q.val:
            return False
        
        
        return ( self.isSameTree(p.left, q.left) ) and ( self.isSameTree(p.right, q.right) )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         #Check left
#         p_left = p
#         p_right = p
        
#         q_left = q
#         q_right = q
        
#         while p_left != None and q_left != None:
#             print(p_left.val, q_left.val)
#             if p_left.val != q_left.val:
#                 return False
#             p_left = p_left.left
#             q_left = q_left.left
            
#         while p_right != None and q_right != None:
            
#             if p_right.val != q_right.val:
#                 return False
#             p_right = p_right.right
#             q_right = q_right.right
#         return True
    
    
    
