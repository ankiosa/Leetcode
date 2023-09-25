# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root==None):
            return 0
        if((root.left!=None) and (root.right!=None)):
            maxdepth = 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
        elif(root.left!=None):
            maxdepth = 1+self.maxDepth(root.left)
        elif(root.right!=None):
            maxdepth = 1+self.maxDepth(root.right)
        else:
            return 1
        return maxdepth