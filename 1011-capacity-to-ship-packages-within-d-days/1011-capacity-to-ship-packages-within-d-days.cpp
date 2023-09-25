#include <numeric>

class Solution {
public:
    bool feasible(vector<int>& weights, int thres, int days){
        int sum = 0;int days_thres = 1;
        for(int i=0;i<weights.size();i++){
            sum += weights[i];
            if(sum>thres){
                sum = weights[i];
                days_thres +=1;
                if(days_thres>days){
                    return false;
                }
            }
        }
    return true;
    }
    
    int shipWithinDays(vector<int>& weights, int days) {
        int weight_len = weights.size();
        int sum = accumulate(weights.begin(), weights.end(), 0);
        auto it = std::minmax_element(weights.begin(), weights.end());
        int max = *it.second;
        int left = max; int right = sum;
            
        while(left<right){
            int mid = left+(right-left)/2;
            if(feasible(weights, mid, days)){
                right = mid;
            }
            else{
                left =mid+1;
            }
            
        }
        return left;
    }
};