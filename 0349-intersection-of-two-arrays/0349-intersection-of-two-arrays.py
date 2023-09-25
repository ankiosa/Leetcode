class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        common_array = []
        hash_dict = {}
        for each in nums1:
            if(each%30 in hash_dict):
                hash_dict[each%30].append(each) 
            else:
                hash_dict[each%30] = [each]
        for each in nums2:
            if((each%30 in hash_dict) and (each in hash_dict[each%30])):
                if(each not in common_array):
                    common_array.append(each)
        return common_array
        
            
        