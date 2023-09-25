class Solution {
public:
    int search(vector<int>& nums, int target, int start, int end){
        if(start>end) return -1;
        
        cout << start << " " << end << endl;
        int mid = (start+end)/2;
        cout << mid << endl;
        if(nums[mid]>target){
            end = mid-1;
            return search(nums, target, start, end);
        }
        else if(nums[mid]<target){
            start = mid+1;
            return search(nums, target, start, end);
        }
        else  if(nums[mid]==target) return mid;
        return -1;
    }
    
    int search(vector<int>& nums, int target) {
        int s=0;
        int e = nums.size()-1;
        int val = search(nums, target, s, e);
        cout << val << endl;
        return val;
    }
};