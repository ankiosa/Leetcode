class Solution(object):

    def subsequnces_sum_K(self, array, index, K, array_sum, new_array, array_of_array):
        if(array_sum==K):
            #new_array.sort()
            print(new_array)
            array_of_array.append(new_array)
            return
        if(index>=len(array) or array_sum>K):
            return

            
        
        
        new_checker =[]
        new_array_check = new_array[:]
        array_sum_check = array_sum
        
        for new_index in range(index, len(array)):
            if(array[new_index]>K):
                continue
            if(array[new_index] not in new_checker):   
                new_checker.append(array[new_index])
                new_array.append(array[new_index])
                array_sum = array_sum+array[new_index]
                #print(new_array)
                self.subsequnces_sum_K(array, new_index+1, K, array_sum, new_array, array_of_array)
                new_array = new_array_check[:]
                array_sum = array_sum_check

        
        
                        
        return array_of_array
    

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.subsequnces_sum_K(candidates,0, target,0, [],[])