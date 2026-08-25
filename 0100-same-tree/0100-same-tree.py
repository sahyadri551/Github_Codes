# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        s1=[p]
        s2=[q]
        while s1 and s2:
            i=s1.pop()
            j=s2.pop()
            if i.val != j.val:
                return False
            if i.left and j.left:
                s1.append(i.left)
                s2.append(j.left)
            elif i.left or j.left:
                return False

            if i.right and j.right:
                s1.append(i.right)
                s2.append(j.right)
            elif i.right or j.right:
                return False
        if s1 or s2:
            return False
        return True
            
            
        