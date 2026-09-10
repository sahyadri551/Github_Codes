# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.matching_nodes = 0
        
        def traverse(current_node):
            if not current_node:
                return 0, 0
            
            left_total, left_nodes = traverse(current_node.left)
            right_total, right_nodes = traverse(current_node.right)
            
            subtree_sum = left_total + right_total + current_node.val
            subtree_size = left_nodes + right_nodes + 1
            
            if (subtree_sum // subtree_size) == current_node.val:
                self.matching_nodes += 1
                
            return subtree_sum, subtree_size

        traverse(root)
        return self.matching_nodes
