class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        final_pro = []  
        pro = 1
        after_pro = []
        for each_index in range(len(nums)-1,-1,-1):
            after_pro.append(pro)
            pro = nums[each_index]*pro
        print(after_pro)   
        pro = 1
        before_pro = []
        for each_index in range(len(nums)):
            before_pro.append(pro)
            
            print(before_pro[each_index],after_pro[len(nums)-each_index-1])
            final_pro.append(before_pro[each_index]*after_pro[len(nums)-each_index-1])
            pro = nums[each_index]*pro
            
        return final_pro
            