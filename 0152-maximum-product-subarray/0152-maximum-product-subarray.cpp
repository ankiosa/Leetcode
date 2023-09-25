class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int currmax =1, maxtillnow = INT_MIN;
        int currmin =1, mintillnow = INT_MIN;
        int oldcurrmax = currmax;

        for(auto x:nums){
            currmax = max(max(x,currmax*x), currmin*x);
            currmin = min(min(x,currmin*x), oldcurrmax*x);
            maxtillnow = max(currmax, maxtillnow);
            oldcurrmax = currmax;
            cout << currmax << "\t" << currmin << "\t" << maxtillnow <<"\n";
        }
        return maxtillnow;
    }
};