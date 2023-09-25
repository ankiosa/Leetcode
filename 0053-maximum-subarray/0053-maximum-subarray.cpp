class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        

       int curmax = 0, maxtillNow = INT_MIN;
       for(auto x:nums){
           curmax = max(x, curmax+x);
           maxtillNow = max(maxtillNow, curmax);
       }
       return maxtillNow;
    }
};