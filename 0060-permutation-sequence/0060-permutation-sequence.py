class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        d ={}
        d_list = [1,1,2, 6, 24, 120, 720, 5040, 40320, 362880]
        for i in range(0,10):
            d[i] = d_list[i]

        numbers_str_list = "123456789"

        numbers_str_list = list(numbers_str_list[:n])

        final_str = ""
        for i in range(n,0,-1):
            print(k,d[i-1], numbers_str_list, (k/d[i-1])-1)
            if(k%d[i-1]!=0):
                final_str += numbers_str_list[k/d[i-1]]
                del numbers_str_list[k/d[i-1]]
                if((k>d[i-1])):
                    k = k%d[i-1]
            else:
                final_str += numbers_str_list[(k/d[i-1])-1]
                del numbers_str_list[k/d[i-1]-1]
                k = d[i-1]
            print(k, d[i-1], final_str)

            print(k)
            if(k<=0):
                break

        final_str = final_str+"".join(numbers_str_list) 

        return final_str




