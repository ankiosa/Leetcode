class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor =0
        for i in nums:
            xor = xor^i
        for i in range(len(nums)+1):
            xor = xor^i
        
        return xor
            
        