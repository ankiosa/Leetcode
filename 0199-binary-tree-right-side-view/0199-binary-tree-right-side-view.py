# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        q = deque()
        if root:    
            q.append(root)
            

        final_array = []
        while len(q):
            new_q = deque()
            abcd = []
            for i in range(len(q)):
                each = q.popleft()
                abcd.append(each.val)
                if(each.left):
                    new_q.append(each.left)
                if(each.right):
                    new_q.append(each.right)
            q = new_q
            final_array.append(abcd[-1])
        return final_array