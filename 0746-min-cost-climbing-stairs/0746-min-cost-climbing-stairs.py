class Solution(object):
    
    costsum = {}
    def costCounting(self, cost, index):
        if(index>len(cost)):
            return ;
        self.costsum[index] = min(self.costsum[index-1]+cost[index-1], self.costsum[index-2]+cost[index-2])
        self.costCounting(cost, index+1)
    
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        self.costsum[0] = 0
        self.costsum[1] = 0
        self.costCounting(cost, 2)
        return self.costsum[len(cost)]
        