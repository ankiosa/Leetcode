#include <limits.h>
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int least_price = INT_MAX;
        int profit  = 0;
        int new_profit;

        for(int i =0; i<prices.size();i++){
            if(prices[i]<least_price){
                least_price = prices[i];
            }
            new_profit = prices[i]-least_price;
            if(new_profit>profit){
                profit = new_profit;
            }
        }
        return profit;

    }
};