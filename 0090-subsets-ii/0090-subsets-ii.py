class Solution(object):

    def subsets(self,array, index, new_array, array_of_array):

        if(index>=len(array)):
            array_of_array["_".join(map(str,new_array))] = 1
            return

            
        org_array = new_array[:]
        new_array = new_array[:]
        new_array.append(array[index])
        self.subsets(array, index+1, org_array, array_of_array)
        self.subsets(array, index+1, new_array, array_of_array)
        
        
        keys = array_of_array.keys()     
        new_array_array = []

        for key in keys:
            if((key=="")):
                new_array_array.append([])
            else:
                new_array_array.append(map(int,key.split("_")))        
        return new_array_array


    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.subsets(nums, 0, [], {})