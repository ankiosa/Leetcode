# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from numpy import inf

class Solution(object):
    
    def checkValidBST(self, node,less_than, greater_than):
        print(less_than,node.val,greater_than)
        if(less_than<node.val<greater_than):
            if(node.left):
                val_check = self.checkValidBST(node.left,less_than, node.val)
                if(val_check==False):
                    return False
            if(node.right):
                val_check =  self.checkValidBST(node.right, node.val, greater_than)
                if(val_check==False):
                    return False
        else:
            print "ok"
            return False
            print "cool"
        return True
            
        
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root==None):
            return False
        val = self.checkValidBST(root, -inf, inf)
        print val
        return val