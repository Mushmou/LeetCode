# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current_node = root
        
        while current_node != None:
            #If they are both greater than current node, then go to the right subtree
            if p.val > current_node.val and q.val > current_node.val:
                current_node = current_node.right
            #If they are both less than current node, then go to the left subtree
            elif p.val < current_node.val and q.val < current_node.val:
                current_node = current_node.left
            #If split occurs, or if it found p or q
            else:
                return current_node