class Solution(object):
    def newpow(self,x,n,array):
        if(n==0):
            return 1
        if(n==1):
            print("abcD",x,n,array)
            for each in array:
                x = x*each
            print(type(x))
            return x

        if(n>0):
            if(n%2==0):
                return self.newpow( x*x, n/2,array)
            if(n%2==1):
                array.append(x)
                return self.newpow( x*x, n/2,array)


    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        print(x,n)
        if(n>0):
            val = self.newpow(x,n,[])
        else:
            val = self.newpow(1/x,n*-1,[])
        print(val)
        return val