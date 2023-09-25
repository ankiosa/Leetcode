from heapq import heappop, heappush
class Solution(object):

            
        
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ele = 1
        heap = [1]
        seen = set([1])
        for _ in range(n):
            ele = heappop(heap)
            for each in [ele*2,ele*3,ele*5]:
                if(each not in seen):
                    seen.add(each)
                    heappush(heap, each)
        return ele
                    
        
        
    
    
    
    
    
    
    
    
            