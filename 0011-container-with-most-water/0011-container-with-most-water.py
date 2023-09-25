class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        current_max_left_height = height[i]
        current_max_right_height = height[j]
        max_water = (j-i)*min(height[i], height[j])

        if(j==1):
            return max_water 

        while(i<=j):
            print(i,j)

            if(current_max_left_height<current_max_right_height):
                i += 1
                current_max_left_height = height[i]

            else:
                j -= 1
                current_max_right_height = height[j]
            max_water = max(max_water,(j-i)*min(height[i], height[j]))

        return max_water
            
            
            

        