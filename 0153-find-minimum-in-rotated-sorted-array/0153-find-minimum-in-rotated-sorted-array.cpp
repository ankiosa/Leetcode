#include <iostream>
#include <vector>

class Solution {
public:
    int findMin(vector<int>& nums) {
        return findminval(nums, 0, nums.size() - 1);
    }

    int findminval(vector<int>& numscheck, int l, int r) {
        if (l == r) {
            return numscheck[l]; // Base case: single element
        }

        int mid = l + (r - l) / 2;

        if (numscheck[mid] > numscheck[r]) {
            return findminval(numscheck, mid + 1, r);
        } else if (numscheck[l] > numscheck[mid]) {
            return findminval(numscheck, l, mid);
        } else {
            // If neither of the above conditions are met, the array is sorted.
            // You can choose to return either numscheck[l] or numscheck[mid].
            // Since both values are equal, you can return either.
            return numscheck[l];
        }
    }
};
