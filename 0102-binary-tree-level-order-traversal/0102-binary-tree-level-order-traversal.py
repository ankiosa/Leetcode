# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(root is None):
            return []
        array = []
        global array 
        def levelordertraversal(array_checkl):
            global array
            array.append([array_checkl[1],array_checkl[2]])
            if(array_checkl[0].left!=None):
                levelordertraversal([array_checkl[0].left,array_checkl[0].left.val, array_checkl[2]+1])
            if(array_checkl[0].right!=None):
                levelordertraversal([array_checkl[0].right,array_checkl[0].right.val, array_checkl[2]+1])
            return 
        levelordertraversal([root, root.val,0])
        array_array = []
        level_checker =[]
        for each_array in array:
            if(each_array[1] not in level_checker):
                array_array.append([each_array[0]])
                level_checker.append(each_array[1])
            else:
                array_array[each_array[1]].append(each_array[0])
        return array_array
            
            
            
            
            
        
        