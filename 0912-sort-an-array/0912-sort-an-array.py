# implement merge sort

class Solution(object):
    
    def merge(self, first_half_array, second_half_array):
        
        i = 0
        j = 0
        
        array_rebuild = []

        while((i<len(first_half_array)) and (j<len(second_half_array))):
            if(first_half_array[i]<=second_half_array[j]):
                array_rebuild.append(first_half_array[i])
                i+=1
            else:
                array_rebuild.append(second_half_array[j])
                j+=1
        while(i<len(first_half_array)):
              array_rebuild.append(first_half_array[i])
              i+=1
        while(j<len(second_half_array)):
              array_rebuild.append(second_half_array[j])
              j+=1
        return array_rebuild
            
            
    
    def mergesort(self, num):
        
        start = 0
        end = len(num)
              
        first_half_array = num[start:end/2]
             
        second_half_array = num[end/2:end]
        
        
        if((len(first_half_array)==1) and (len(second_half_array)==1)):
              if(first_half_array[0]<second_half_array[0]):
                    return [first_half_array[0],second_half_array[0]]
              else:
                    return [second_half_array[0], first_half_array[0]]
             
        if((len(first_half_array)==0) and (len(second_half_array)==1)):
              return [second_half_array[0]]
        if((len(first_half_array)==1) and (len(second_half_array)==0)):
              return [first_half_array[0]]
        
        
        first_half_array = self.mergesort(first_half_array)
              
        second_half_array = self.mergesort(second_half_array)   
 

        
        return self.merge(first_half_array, second_half_array)
             
    
    
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.mergesort(nums)
        