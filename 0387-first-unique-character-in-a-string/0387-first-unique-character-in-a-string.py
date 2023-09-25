class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_table_one = {}
        hash_table_two = {}
        i = 0
        for ele in s:
            if(ele in hash_table_one):
                hash_table_one[ele] = hash_table_one[ele]+ 1
            else:
                hash_table_one[ele] = 1
            if(ele not in hash_table_two):
                hash_table_two[ele] = i
            i+=1
        print(hash_table_one)
        for ele in s:
            if(hash_table_one[ele]==1):
                return hash_table_two[ele]
        return -1
            
            
                
        