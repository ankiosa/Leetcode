class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

        unordered_set<int> numsset(nums.begin(), nums.end());
        if(numsset.size()==nums.size()){
            return false;
        }
        return true;
        
    }
};