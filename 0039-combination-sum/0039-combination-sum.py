class Solution(object):


    def subsequnces_sum_K(self, array, index, K, array_sum, new_array, array_of_array):
        if(array_sum==K):
            if(new_array not in array_of_array):
                array_of_array.append(new_array)
            return
        if(index>=len(array) or (array_sum>K)):
            return

            
        org_array = new_array[:]
        new_array = new_array[:]
        new_array.append(array[index])

        self.subsequnces_sum_K(array, index, K, array_sum+array[index], new_array, array_of_array)
        self.subsequnces_sum_K(array, index+1, K, array_sum, org_array, array_of_array)
        #self.subsequnces_sum_K(array, index+1, K, array_sum+array[index], new_array, array_of_array)
        
        
        
                        
        return array_of_array
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        return self.subsequnces_sum_K(candidates,0, target,0, [],[])


