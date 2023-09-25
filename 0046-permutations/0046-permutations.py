class Solution(object):

    def permute_check(self, nums, permut_array, index):

        if(index==len(nums)):
            return permut_array

        new_arr = permut_array[:]
        for each_arr in new_arr:
            for i in range(0,index):
                lst = each_arr[:]
                lst[i], lst[index] = lst[index], lst[i]
                permut_array.append(lst)
        
        return self.permute_check(nums,permut_array, index+1)

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums)<2):
            return [nums]
        else:
            val = self.permute_check(nums, [nums], 1)
            print(val)
            return val

        
