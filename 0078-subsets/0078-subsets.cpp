class Solution {
private:
    void powerset(vector<int> nums,vector<int> output,int index, vector<vector<int>>& ans)
    {
        if(index>=nums.size())
        {
            ans.push_back(output);
            return;
        }
        //exclusion
        powerset(nums,output,index+1,ans);
        //inclusion
        int ele=nums[index];
        output.push_back(ele);
        powerset(nums,output,index+1,ans);
    }
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>>ans;
        vector<int>output;
        int index=0;
        powerset(nums,output,index,ans);
        return ans;
    }
};