#include <map>
#include <algorithm>
class Solution {
public:
    bool isAnagram(string s, string t) {
        
        unordered_map<char, int> counts;
        unordered_map<char, int> countt;

        for(auto x:s){
            counts[x]++;
        }
        for(auto x:t){
            countt[x]++;
        }

        if(counts!=countt){
            return false;
        }
        else{
            return true;
        }
    }
};