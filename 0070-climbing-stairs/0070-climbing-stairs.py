class Solution(object):
    def climbStairsMemo(self, memo, n):
        if(n in memo):
            return memo[n]
        else:
            memo[n] = self.climbStairsMemo(memo, n-1) + +self.climbStairsMemo(memo, n-2)
            
        return memo[n]
    
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {} 
        memo[1] = 1
        memo[2] = 2
        
        return self.climbStairsMemo(memo, n)