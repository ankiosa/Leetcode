from collections import deque
from numpy import inf
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid), len(grid[0])
        Q = deque([])
        cnt = 0
        
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==2):Q.append((i,j))
                if(grid[i][j]==1):cnt += 1
                    
        res =0
        while Q:
            for _ in range(len(Q)):
                i,j = Q.popleft()
                for x,y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                    if((0<=x<m) and (0<=y<n) and (grid[x][y]==1)):
                        grid[x][y]=2
                        cnt -= 1
                        Q.append((x,y))
            res += 1
            
        return max(0, res-1) if cnt==0 else -1
        
        
